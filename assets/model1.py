#!/usr/bin/env python
# coding: utf-8

# In[15]:


import pandas as pd
df = pd.read_csv('c:/Users/Owen/10k_books.csv')


# In[16]:


small = df.sample(1000)
feature = 'reviewText'
target = 'overall'

small = small[['reviewText', 'overall']]


# In[17]:


import string
import spacy
from spacy.lang.en import English

punctuations = string.punctuation
stop_words = spacy.lang.en.stop_words.STOP_WORDS
parser = English()

def spacy_tokenizer(sentence):
    mytokens = parser(sentence)
    mytokens = [word.lemma_.lower().strip() if word.lemma_ != '-PRON-'
                else word.lower_ for word in mytokens]
    mytokens = [word for word in mytokens if word not in stop_words
                and word not in punctuations]
    return mytokens


# In[18]:


from sklearn.model_selection import train_test_split

X = small[feature]
y = small[target]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, 
                                                    stratify=y, random_state=1)


# In[19]:


from sklearn.feature_extraction.text import TfidfVectorizer

tfidf_vec = TfidfVectorizer(tokenizer = spacy_tokenizer,
                            ngram_range = (1,1),
                            max_df = 0.5,
                            min_df = 2)

X_train_vecs = tfidf_vec.fit_transform(X_train)
X_test_vecs = tfidf_vec.transform(X_test)


# In[20]:


from lightgbm import LGBMClassifier

model = LGBMClassifier(objective='binary', is_unbalance=True, n_iterations=1571, 
                             max_bin=696, num_leaves=993, num_jobs=-1, seed=0)

model.fit(X_train_vecs, y_train);

