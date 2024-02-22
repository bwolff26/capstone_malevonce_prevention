# Clever Name for Project 

Dealing with threats and heat speach.

## Methodology

The plan, going forward, is to first convert all of raw dataframes into one giant data frame, preserving the 'original' text,
original dataset it was from, and potentially the time it was gathered. Note, that each dataset scored things differently, so I'd need to focus on each one individualls any convert them into a flexible neutral system to adapt them all. Ie the 02 dataset ranks thing on a scale of -8 to 8 (approx.)... At the moment, the plan is to have three classes: harmless, problematic, and concerning. Pragmatically, I think I'd make another new column called original ranking, which would natrually then be a mixed hybrid column with all the different scales, in case whatever my original judgement calls were off.

While the various features of each dataset would be interesting. To use them has several drawbacks: They're not consistent across all of them. While I could limit myself to just one, I don' want to. Besides lusting for more data, I am a bit circumspect that each one might be
per a specific group or culture - averaging them out across many differnet mediums would help limit though. Another consideation is the useage of language - potentially slang would be diminished (which I want as slang is relevant to the times and I'd like to focus on a mor obust timeless model - if possible at all, in general and especially re. languages).

Afterwards, I'd do various pre-processings and NLP techniques,akin to what we've dne before with other projects. However, where we'll deviate is after the initial modeling on just the words themselves: Various patterns outside the text themselves I'd like to examine. Ie is reddit a more toxic place than the baseline? Are longer texts more likely to be toxic? Are emojis slightly inclined towards abuse? Etc. A number of such questions have already been mentioned in the first presentation I gave re. my capstone; they're cuently very sloppily found at the bottom of this read me.

After that, I think I'd finally read through all of the documentatons and see if any relevant techniques they did to focus on trneds I culd as well. Besides applying those techniques, I liekly would have thought of additional features to generate.

And finally, of course, is the preperation of the presnation and the streamlit.

## Sources

The following base statistics, save the names of what I called those datasets in the data folder, were copied from the following website: https://hatespeechdata.com/
    On the topic, a big thanks to Sonyah Seiden for her dirction to this site.

01_ConvAbuse
Link to publication: https://aclanthology.org/2021.emnlp-main.587/
Link to data: https://github.com/amandacurry/convabuse
Task description: Hierarchical: 1. Abuse binary, Abuse severity 1,0,-1,-2,-3; 2. Directedness explicit, implicit Target group, individual–system, individual–3rd party, Type general, sexist, sexual harassment, homophobic, racist, transphobic, ableist, intellectual
Details of task: Abuse detection in conversational AI
Size of dataset: 4,185
Percentage abusive: c. 20%

02_MeasuringHateSpeach
Link to publication: https://arxiv.org/abs/2009.10277
Link to data: https://huggingface.co/datasets/ucberkeley-dlab/measuring-hate-speech
Task description: 10 ordinal labels (sentiment, (dis)respect, insult, humiliation, inferior status, violence, dehumanization, genocide, attack/defense, hate speech), which are debiased and aggregated into a continuous hate speech severity score (hate_speech_score) that includes a region for counterspeech & supportive speeech. Includes 8 target identity groups (race/ethnicity, religion, national origin/citizenship, gender, sexual orientation, age, disability, political ideology) and 42 identity subgroups.
Details of task: Hate speech measurement on social media in English
Size of dataset: 39,565 comments annotated by 7,912 annotators on 10 ordinal labels, for 1,355,560 total labels.

03_ToxicSpans
Link to publication: https://aclanthology.org/2021.semeval-1.6.pdf
Link to data: https://github.com/ipavlopoulos/toxic_spans
Task description: Binary toxic spans (toxic, non-toxic) & reading comprehension
Details of task: Predict the spans of toxic posts that were responsible for the toxic label of the posts.
Size of dataset: 10,629
Percentage abusive: 0.56

04_SlurCorpus
Towards a Comprehensive Taxonomy and Large-Scale Annotated Corpus for Online Slur Usage
Link to publication: https://www.aclweb.org/anthology/2020.alw-1.17.pdf
Link to data: https://github.com/networkdynamics/slur-corpus
Task description: 4 primary categories (derogatory, appropriate, non-derogatory/non-appropriate, homonyms, noise)
Details of task: Hate per se
Size of dataset: 39,811
Percentage abusive: 0.52

05_AutomatedHateSpeech
Automated Hate Speech Detection and the Problem of Offensive Language
Link to publication: [https://ojs.aaai.org/index.php/ICWSM/article/view/14955)
Link to data: https://github.com/t-davidson/hate-speech-and-offensive-language
Task description: Hierarchy (Hate, Offensive, Neither)
Details of task: Hate per se
Size of dataset: 24,802
Percentage abusive: 0.06

06_WhiteSupremacy
Link to publication: https://www.aclweb.org/anthology/W18-5102.pdf
Link to data: https://github.com/Vicomtech/hate-speech-dataset
Task description: Ternary (Hate, Relation, Not)
Details of task: Hate per se
Size of dataset: 9,916
Percentage abusive: 0.11

07_OnlineHateSpeech
Link to publication: https://arxiv.org/abs/1909.04251
Link to data: https://github.com/jing-qian/A-Benchmark-Dataset-for-Learning-to-Intervene-in-Online-Hate-Speech
Task description: Binary (hateful/not)
Details of task: Hate per se
Size of dataset: 33,776
Percentage abusive: 0.43

### Proposals re. specific ds problem

P1 - THe school Board

3 focus on sensitivity
    ie care of the kids

P2 - Police Force

3 focus on precision
    ie car eof resources

P3 - Twitter
    ovrall accuracy.... ie from lawsuits


## Features to Consider

#conssider: besides usual cvecs:
#presence of @
#presence of links
#Actually written properly?
#original word count
    #figure out re. links, emojis, etc.
#presecence of emojis
#presence of capital letters
    #i...mot of the time...
#presence of slang
    #liekly too hard to do for a computer.... ie could code t like 2...
#claned word count...
#Racial words
#Other deragoratry/assumed negative words, such as 'midget' 'miniscule' 'fat'
#change of words...



## challenges:

    might need more data
    missing time values
    just on the basis of the tweet - don't know anything abotut he persn...
    Potential backlash re. contacting a not at risk...
    [obviously] false negatives... esp. re suicide

demographics

bullying record

other tweets snet in past 24 hous..


All of them can easily incorpoate webapp via plug in a tweet, with custom approaches dpeending upon the response:


Ie combine borderline with othe factors - low age, minority, 'classic bully target', etc., home stability
    Ie perhaps also find other datasets re. risk factors, analyze though and say, "Hey, if they have a suss tweet plus...
    
Preventive action...

Sumit: if suicidal, maybe run it through a second model - scale ie resolv via school vs. police

Sonyah :degrees of scale.... and perhaps generalize by local sevices...