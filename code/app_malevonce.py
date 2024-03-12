from operator import mod
import streamlit as st

import pickle
from bs4 import BeautifulSoup
import regex as re
from nltk.stem.porter import PorterStemmer
import pandas as pd

# @st.cache
def load_model():
    with open('model_base.pkl', 'rb') as f: #reading bytes
        the_model = pickle.load(f)
    return the_model

model = load_model()

def document_words(raw_document):

    document_text = BeautifulSoup(raw_document, features="lxml").get_text()
    letters_only = re.sub("[^a-zA-Z0-9]", " ", document_text)
    words = letters_only.split()
    words = [w.lower() for w in words]
    p_stemmer = PorterStemmer()
    stemmed_words = [p_stemmer.stem(i, to_lowercase=False) for i in words]
    return(" ".join(stemmed_words))

def prob_scanner_account(df, thresh_2=.58, thresh_1=.83, one_response=3):
    overall = 1
    try:
        count_2s = df['pred'].value_counts()[2]
        thresh_2 -= .05 * max(count_2s-1,0) #Eh, could have simplified in one line, but whatever.
        print(thresh_2)
        if df[df['prob']==df['prob'].max()].iloc[0]['p_2'] > thresh_2 and df[df['prob']==df['prob'].max()].iloc[0]['pred'] == 2:
            return "calling the principal AND your guardians"
    except:
        pass
    count_1s = 0
    try:
        count_1s += df['pred'].value_counts()[1]
    except:
        pass
    try:
        count_1s += df['pred'].value_counts()[2]
    except:
        pass
    thresh_1 -= .02 * max(0,count_1s-one_response)
    if df[df['pred']!=0]['1_prob'].mean() > thresh_1 and count_1s >= one_response:
        return "calling the principal"
    else:
        return "free...for now"
###############################################
###############################################
###############################################
#Inserts for dictionary

st.title('Hate Speech Analyzer')

st.subheader('Please use the app to recommend if a series of posts should require human inspection for inappropriate behavior.')
st.subheader('Note, the model used focuses on individual posts; the app pieces togethe individual probabilities to determine the liklihood of intervening..')
st.subheader("By default in the app, only three or more 'mild' hate speech comments will get a student called to the principal's office; just one 'extreme' comment on the other hand ...")


txt = st.text_area('Write your posts here; pleasee delineate them with a semi-colon (;).').strip()

if st.button('Submit'):
    posts=txt.split(';')
    sample = pd.DataFrame({'post':posts})
    sample['cleaned_post'] = sample['post'].apply(document_words)
    
    preds = model.predict(sample['cleaned_post'])
    preds_prob = model.predict_proba(sample['cleaned_post'])
    sample_pred_comparer = pd.DataFrame({
        'post':sample['post']
        ,'pred':preds
        ,'p_0':preds_prob[:,0]
        ,'p_1':preds_prob[:,1]
        ,'p_2':preds_prob[:,2]
    })
    sample_pred_comparer['prob'] = round(sample_pred_comparer[['p_0','p_1','p_2']].max(axis=1),3)
    sample_pred_comparer['1_prob'] = [sample_pred_comparer.loc[i, 'p_1'] if sample_pred_comparer.loc[i, 'pred'] == 0
                                                      else (1-sample_pred_comparer.loc[i, 'p_0'])
                                                      for i in range(sample_pred_comparer.shape[0])]
    st.write(prob_scanner_account(sample_pred_comparer))
    st.write("And here are their respective predictions and probabilities:")
    st.write(sample_pred_comparer.sort_values('prob', ascending=False).sort_values('pred', ascending=False).loc[:,["post","pred","prob"]])
    
            
#   if len(txt) > 0:
#     pred = model.predict([txt])[0]
#     probs = list(model.predict_proba([txt])[0])
#     prob = probs[0] if pred == 'Edgar Allan Poe' else probs[1]
#     st.write('You write like ', pred)
#     st.metric('Probability', f'{100 * round(prob, 2)}%')
#   else:
#     st.write('Too pithy. Try writing something.')
###############################################
    ###############################################
###############################################
# sample_comments = [user1_logs[i]['comment'] for i in range(len(user1_logs))]
# sample = pd.DataFrame(data={'cleaned_comments':sample_comments})
# sample['cleaned_comments'] = sample['cleaned_comments'].apply(document_words)

# preds = trial_model.predict(sample['cleaned_comments'])
# preds_prob = trial_model.predict_proba(sample['cleaned_comments'])
# sample_pred_comparer = pd.DataFrame({
#     #'cleaned_text':X_test
#     #,'actual':y_test
#     'pred':preds
#     ,'p_0':preds_prob[:,0]
#     ,'p_1':preds_prob[:,1]
#     ,'p_2':preds_prob[:,2]
# })
# sample_pred_comparer['max_prob'] = sample_pred_comparer[['p_0','p_1','p_2']].max(axis=1)
# sample_pred_comparer['occur'] = [user1_logs[i]['occur'] for i in range(len(user1_logs))]
# #sample_pred_comparer

# prob_scanner_account(sample_pred_comparer)