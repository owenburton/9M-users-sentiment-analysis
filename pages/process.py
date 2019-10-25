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
        
            ## Process

            ********

            This is how I did it.
            ```
            from sklearn.feature_extraction.text import TfidfVectorizer

            tfidf_vec = TfidfVectorizer(tokenizer = None,
                                        ngram_range = (1,2),
                                        max_df = 0.5,
                                        min_df = 2)

            X_train_vecs = tfidf_vec.fit_transform(X_train)
            X_test_vecs = tfidf_vec.transform(X_test)
            ```

            HERE'S CODE SHOWING HOW THE TEXT IS CLEANED

            HERE'S CODE SHOWING THE TOKENIZING/VECTORIZER FUNCTIONS

            HERE'S A SNIPPET OF CODE SHOWING LGBMCLASSIFIER

            ```
            from lightgbm import LGBMClassifier

            model = LGBMClassifier(objective='binary', is_unbalance=True, n_iterations=1571, 
                             max_bin=696, num_leaves=993, num_jobs=-1, seed=0)

            model.fit(X_train_vecs, y_train);
            ```

            CAN YOU FIGURE OUT HOW TO USE SPACY'S CNN TEXT CLASSIFIER?


            """
        ),

    ],
)

layout = dbc.Row([column1])