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

    document_text = BeautifulSoup(raw_document).get_text()
    letters_only = re.sub("[^a-zA-Z0-9]", " ", document_text)
    words = letters_only.split()
    words = [w.lower() for w in words]
    p_stemmer = PorterStemmer()
    stemmed_words = [p_stemmer.stem(i, to_lowercase=False) for i in words]
    return(" ".join(stemmed_words))

def prob_scanner_account(df, thresh_2=.58, thresh_1=.94, one_response=3):
    overall = 1
    count_2s = df['pred'].value_counts()[2]
    thresh_2 -= .05 * count_2s
    if df[df['max_prob']==df['max_prob'].max()].iloc[0]['p_2'] > thresh_2 and df[df['max_prob']==df['max_prob'].max()].iloc[0]['pred'] == 2:
        return "calling the principal AND your guardians"
    count_1s = df['pred'].value_counts()[1] + df['pred'].value_counts()[2]
    thresh_1 -= .03 * count_1s
    if df[df['pred']!=0]['1_prob'].mean() > thresh_1 and count_1s >= one_response:
        return "calling the principal"  
###############################################
###############################################
###############################################
#Inserts for dictionary

st.title('Hate Speach Analyzer')

st.subheader('Please use our app to recommend if a series of posts should require human inspection for inappropriate behavior.')
st.subheader('Note, our model focuses on individual posts; our app pieces together the individual probabilities to determine the liklihood of intervening..')

txt = st.text_area('Write your posts here; pleasee delineate them with a semi-colon (;).').strip()

if st.button('Submit'):
    demo_logs=txt.split(';')  
    sample = pd.DataFrame({'cleaned_comments':demo_logs})
    sample['cleaned_comments'] = sample['cleaned_comments'].apply(document_words)  
    
    preds = model.predict(sample['cleaned_comments'])
    preds_prob = model.predict_proba(sample['cleaned_comments'])
    sample_pred_comparer = pd.DataFrame({
    #'cleaned_text':X_test
    #,'actual':y_test
    'pred':preds
    ,'p_0':preds_prob[:,0]
    ,'p_1':preds_prob[:,1]
    ,'p_2':preds_prob[:,2]
    })
    sample_pred_comparer['max_prob'] = sample_pred_comparer[['p_0','p_1','p_2']].max(axis=1)
    sample_pred_comparer['1_prob'] = [sample_pred_comparer.loc[i, 'p_0'] if sample_pred_comparer.loc[i, 'pred'] == 0
                                                      else (1-sample_pred_comparer.loc[i, 'p_0'])
                                                      for i in range(sample_pred_comparer.shape[0])]
 
    st.write(prob_scanner_account(sample_pred_comparer))
    
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