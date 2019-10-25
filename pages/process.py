import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## **Process**

            ********

            ##### **How did you explore and clean the data?**
            
            I verified the shape matched the number of observations and features described in the source
            website: `link to original website`.
            Then, I removed some missing entries in the dataset after checking with: `df.isna().sum()`.
            For my iterative process, it would have taken too long to fit a baseline model on the nine million reviews,
            so I saved a sample of one million to work with: `smaller = df.sample(1000000, random_state=0)`.

            I wanted to know how long the reviews were:
            ```
            import numpy as np
            df['review_lengths'] = list(map(len, df.reviewText.str.split(' ')))
            df['review_lengths'].describe()
            ```
            To process the natural language in the reviews I used some tools within SpaCy's library.
            SpaCy also has built-in text cleaning for removing stop-words, finding the lemma of words,
            and changing text to lists of tokens that can be fed into a vectorizer:

            ```
            import string
            import spacy
            from spacy.lang.en import English

            # Create punctuation list.
            punctuations = string.punctuation

            # Create stopwords list.
            stop_words = spacy.lang.en.stop_words.STOP_WORDS

            # Load tokenizer, tagger, and parser.
            parser = English()

            # Create tokenizer function.
            def spacy_tokenizer(sentence):
                # Create token object, which is used to create documents with linguistic annotations.
                mytokens = parser(sentence)
    
                # For each token, lemmatize and change to lowercase.
                mytokens = [word.lemma_.lower().strip() if word.lemma_ != '-PRON-' else word.lower_ for word in mytokens]
                # Remove stop words.
                mytokens = [word for word in mytokens if word not in stop_words and word not in punctuations]
                # Return preprocessed list of tokens.
                return mytokens
            ```

            ##### **What was your baseline model?**

            After getting a majority class baseline, I used a bag-of-words method - `CountVectorizer()` - 
            to get my features matrix and pass that into scikit-learn's logistic regression classifier as
            a baseline model.

            Baseline accuracy with logistic regression beat the majority class baseline, but I wanted to 
            do some feature engineering to improve the predictions, so I looked at some of the most common
            words used to sway the classifications:

            ```
            import matplotlib.pyplot as plt

            # Look at the top 50 words from POSITIVE book reviews.
            plt.figure(figsize=(16,6))
            term_df_p.sum(axis=0).sort_values(ascending=False)[0:50].plot.bar(color='pink')
            plt.title('50 most frequent words in POSITIVE book reviews')
            plt.ylabel('frequency')
            plt.xticks(rotation=45)
            plt.show()
            ```
            """
        ),

    ],
    md=6,
)

column2 = dbc.Col(
    [
        dcc.Markdown(
            """
            ##### **Improving from baselines...**
            
            Using a more complex `TfidfVectorizer()`, I adjusted the threshold of allowable common words 
            associated with class predictions:

            ```
            from sklearn.feature_extraction.text import TfidfVectorizer

            tfidf_vec = TfidfVectorizer(tokenizer = None,
                                        ngram_range = (1,2),
                                        max_df = 0.5,
                                        min_df = 2)

            X_train_vecs = tfidf_vec.fit_transform(X_train)
            X_test_vecs = tfidf_vec.transform(X_test)
            ```

            I also used a gradient-boosting model, `LGBMClassifier()`, to improve accuracy:

            ```
            from lightgbm import LGBMClassifier
            classifier = LGBMClassifier(objective='multiclass', num_class=5, 
                                        metric='multi_error', num_jobs=-1, seed=0)

            pipe = make_pipeline(classifier)
            pipe.fit(X_train_vecs, y_train)
            ```

            ##### **How'd you tune your model and avoid over-fitting?**

            I used randomized search cross-validation and testing hold-out sets to ensure the model wasn't over-fitting:
            ```
            from sklearn.model_selection import RandomizedSearchCV
            from scipy.stats import randint

            model = LGBMClassifier(objective='binary', is_unbalance=True, num_jobs=-1, seed=0)

            params = { 
                    'model__num_leaves': randint(1, 1000), 
                    'model__max_bin': randint(254, 1000),  
            }

            search = RandomizedSearchCV(
                      model, 
                      param_distributions=params, 
                      n_iter=5, 
                      cv=3, 
                      scoring='f1', 
                      verbose=30, 
                      return_train_score=True, 
                      n_jobs=-1
            )

            search.fit(X_train_vecs, y_train);
            ```

            """
        ),
    ],
    md=6,
)

layout = dbc.Row([column1, column2])