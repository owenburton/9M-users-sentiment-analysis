#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import string
import spacy
from spacy.lang.en import English
# Create punctuation list.
punctuations = string.punctuation

# Create stopwords list.
# nlp = spacy.load('en_core_web_lg')
stop_words = spacy.lang.en.stop_words.STOP_WORDS

# Load tokenizer, tagger, parser, NER, and word vectors.
parser = English()

# Create tokenizer function.
def spacy_tokenizer(sentence):
    # Create token object, which is used to create documents with linguistic annotations.
    mytokens = parser(sentence)
    
    # For each token, lemmatize and change to lowercase.
    mytokens = [word.lemma_.lower().strip() if word.lemma_ != '-PRON-'
                else word.lower_ for word in mytokens]
    # Remove stop words.
    mytokens = [word for word in mytokens if word not in stop_words
                and word not in punctuations]
    # Return preprocessed list of tokens.
    return mytokens

