# Malevolence Prevention
Released March of 2024

### WARNING: The following project contains sensitive topics. Reader discretion is advised.

## Introduction

A local middle school, concerned with the ongoing troubles of hate spech, menacing speech meant to intimidate, insult, and belittle members or even an individual of a particular group (typically by their race, religion, origin, gender, sexuality, age, and/or disability). Such differences have been a concern for all of time. Unfortunately, they have been exasperated by the proliferation of the internet and social media, exposing children to ideas and giving them an anonymous platform to comment and act in their stereotypical immature manner. However, when such "jokes" are in the realm of hate speech, particular attention needs to be adhered to lest erroneous views get taken to far. Far too often "playing around" is the defense to abhorrent actions that never should have occurred.

In hopes of preventing malevolence, the school board reached out to you, a well known data scientist, to construct a Natural Language Processor (NLP) that the school could use to analyze their students' social media accounts, looking for posts that are deemed hateful. Although the human touch would be nice, it's beyond unreasonable to expect somebody to go through every single post a student makes to see if it's hateful. So, they hope the model will be sensitive enough in identifying hate speech and only afterwards manually review the student's posts before action is taken. Furthermore, they insist in you making a model that will be able to classify multiple levels of hate speech, with a higher level category expecting for multiple members of the school to review and a default expectation that the student's parents would be brought to school to talk over the matter with them and their child, and a lower level category expecting just one member of the school to review the comments before talking over the matter with the students. Because the school will only be reviewing the posts after the model flags a student's account as problematic, the school is unconcerned about the specific methodology or explainability of how it determines if a post is hateful, however they would appreciate some sense of explanation in what trends can be detected in hate speech.

The data used for this project is from Kennedy, Bacon, Sahn, and von Vacano's 2020 paper "Constructing...a hate speech application" (see below). Data was gathered using Twitter, Reddit, and Youtube's APIs. Hence, discretion is advised when shifting from the epoch and place (from those platforms to public conversations and potentially even other online forums if it's expected that word usage will be different).

At the moment I'm inclined to include all of my notebooks in the push, however of special interest are the following (ipynb by default):
eda_i
modeling_i
fushion_ii
app_malevonce.py

## Summary

The task at hand called for multi-class classification, which seemed challenging in this case as "hate speech is hate speech" and skepticism was given to accurate a model would be. Unlike the original dataset, which was regressed on a scale (roughly from -10 to 10 for simplicity's sake, where -10 is defensive and 10 is quite vitriolic hate speech, with "< -1 is counter or supportive speech, and -1 to +0.5 is neutral or ambiguous" and "> 0.5 is approximately hate speech" (huggingface/berkeley). So, it would seem somewhat arbitrary to bisect the hate speech partition. However, such is what the project called for. The borderline between the two groups was placed at a hate speech score of 2, primarily because it approximates "extremes" representing 5% of the total data.

Another concern was the bulk of defensive and ambiguous speech, that often also had quite graphic and illicit messages in them. I was tempted to include one, but out of fear that the Github might parse it and flag my account, ironic considering the topic, however I'll leave that to anybody curious enough to go through the code or open the CSV. A final concern was the vast minority of more toxic hate speech (thankfully from a humanitarian perspective; unfortunate from a modeling point of view).

Ultimately, data was randomly resampled, tokenized via TfIdf Vectorizer and a logistic regression model, tuned and weighted to focus on the hate speech classes, performed by far the best. The weighted sensitivity was a meager 63%; however, a more general sensitivity, identifying if at least a post was hate speech to some degree, was 94% with the same model! Note, the team at Berkeley, and recall their different goals with this data, had a Mean Absolute Error of .85 in their final RoBERTa model. However, such is a different metric than ours, hence cautioun is begged when trying to compare the two, if that is at all possible.

Finally, per the school's requests. The model was subsequently applied to a student's social media accounts to parse them for hateful speech. And to clarify: The model is built off of the inspect of an individual comment; the final task (and subsequent product, demonstrated on Streamlit below) combines somewhat arbitrary thresholds for determining when a school employee(s) should manually review a student's posts. A sliding scale was applied, meaning that as more comments flagged as hate speech, whether "1" or "2" the confidence needed to beckon a staff member to review them decreased, accounting for the practicality of comments going "under the radar" as well as flexibility in changes in platform and language (however caution is still advised as time goes on to confirm that the model adequately picks up changes in such matters).

The project is currently (3/13/24) hosted at the following location, courtesy of Streamlit:

PLAEEPLAC PLACE for streamlit link/whatever

## Concluding Remarks

Hate speech is an evident problem to anybody that has morals. Although "words may not hurt" one, they can certainly bring "sticks ad stones" via incitement on all levels of society, including school children. At least in the more tender and friendly environment of a school, where education is theoretically valued, calling upon the original Latin "to bring up and forth" the innate good that can be fostered with proper guidance. Left uncheck it's latent to manifest in perverted and malevolent ways. Like with anything, there are positives and negatives with the proposed solution. Truthfully, a concern of having 'high-grade hate speech' repeatedly misclassified. Although per the current coding this has been mitigated (per the hierarchy of a 'high-grade' hate speech is at least as toxic as a 'low-grade' hate speech) with our aforementioned sensitivity of 94% in that regard, continued classification errors could still persist, however the likelihood of that is comfortably minimized for the present. Especially when the result of a flag is to call for a human to then manually review the comments, and likely personally dubbing them in the "high-level" category upon actually reading them. Given the presumed default "innocence" in children this assumption is comfortably made, primarily in an attempt to save the staff resources on false positives. Especially given the tendency of children, heightened by the anonymity and detachment of the internet, such behavior, although not appropriate, hopefully do not need to be taken seriously.

Continued work to be done, besides gathering more timely data would primarily be to train the data on unique comments, without relying on the usage of random resampling. Due to time constraints as well as suspicion to use synthetic data, especially in a topic as sensitive as this, is likely uncalled far. However, likely it's still an avenue worth exploring and at least trying. Another limit on that, mind you, and on the topic of adding more data in general, is that it would not be via the 'same' annotators used in the used comments, adding to potential changes in the inherent classifications.

The other major pragmatic thing to do would be to continue experimenting with Support Vector Machines (SVM) approaches. A mere scratch of their potential was unleashed (modeling_i) due to their inordinate operation times per cross-validation fold (7 minutes via Count Vectorizer; 19 minutes via TFIDF). So, with better computational resources availabile they would realistic options to pursue. On the topic, recurrent neural networks and the like would also be an avenue to explore.

## Sources & Acknowledgments

-[Constructing interval variables via faceted Rasch measurement and multitask deep learning: a hate speech application](https://arxiv.org/abs/2009.10277)(https://huggingface.co/datasets/ucberkeley-dlab/measuring-hate-speech)
-[Image of a child getting punishd](https://medium.com/@sonali.srijan.13/mommy-the-teacher-hit-me-my-experiences-with-corporal-punishment-a41f7b1ce101)
-[Image of a woman in jail](https://www.thecut.com/2016/08/incarcerated-women-held-in-jail.html)

Although not directly used in this project, I would still like to link the following website, the one that referenced this dataset as well as many others:
-[Hate Speech Data](https://hatespeechdata.com/)

Finally, I refuse to not thank in this document my instructors at General Assembly's Data Science Immersive: Misfiqur Rahman, Sonyah Seiden, and Eric Bayless.


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
