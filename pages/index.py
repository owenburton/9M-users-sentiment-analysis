import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
# New imports
from joblib import load
# import string
# import spacy
# from spacy.lang.en import English
# from assets.Uni2_build1_a import spacy_tokenizer

from app import app

# sm_url = "https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-2.1.0/en_core_web_sm-2.1.0.tar.gz"
# r = requests.get(sm_url, allow_redirects=True)
# open('sm.zip', 'wb').write(r.content)
# tar = tarfile.open('sm.zip', "r:gz")
# tar.extractall('down_sm')
# nlp = spacy.load("./down_sm/en_core_web_sm-2.1.0/en_core_web_sm/en_core_web_sm-2.1.0")

# # Create punctuation list.
# punctuations = string.punctuation

# # Create stopwords list.
# # nlp = spacy.load('en_core_web_lg')
# stop_words = spacy.lang.en.stop_words.STOP_WORDS

# # Load tokenizer, tagger, parser, NER, and word vectors.
# parser = English()

# # Create tokenizer function.
# def spacy_tokenizer(sentence):
#     # Create token object, which is used to create documents with linguistic annotations.
#     mytokens = parser(sentence)
    
#     # For each token, lemmatize and change to lowercase.
#     mytokens = [word.lemma_.lower().strip() if word.lemma_ != '-PRON-'
#                 else word.lower_ for word in mytokens]
#     # Remove stop words.
#     mytokens = [word for word in mytokens if word not in stop_words
#                 and word not in punctuations]
#     # Return preprocessed list of tokens.
#     return mytokens

# vectorizer = load('assets/vectorizer.joblib')
# model = load('assets/model.joblib')

column1 = dbc.Col(
    [
        dcc.Markdown(
            """
            ## How do nine million users feel?
            
            ********

            It's important to understand how customers feel about the products they're using, but 
            most businesses wouldn't spend the labor hours to manually read millions of reviews.
            
            With a simple example of book review analysis, 
            I'll show you one way user sentiment can be tracked automatically, quickly, and at scale.

            ##### Copy-paste or write a book review below.
            """
        ),
        dcc.Textarea(
            id='input-box',
            placeholder='Max length: 5000 words',
            value="I loved Excession. It's amazing how creative Iain Banks is. Incredible space opera with AI ethics questions? Gimme 1000 more.",
            cols=50,
            rows=3,
            maxLength=5000,
            style={'width': '100%', 'marginBottom': '1.2em'}
        ),
        dcc.Link(dbc.Button('Rate your review!', id='button', color='primary', 
                            style=dict(marginTop=5, marginBottom=10)), 
                            href='/predictions'),
        # html.Div(id='prediction-label', className='lead', style={'marginBottom': '3em', 'fontWeight': 'bold', 'fontSize': '20px'}),
    ],
    md=5,
)

column2 = dbc.Col(
    [
        html.Img(src='assets/books.jpg', className='img-fluid')
    ]
)

layout = dbc.Row([column1, column2])

# @app.callback(
#     [Output('prediction-label', 'children')],
#     [Input('button', 'n_clicks')],
#     [State('input-box', 'value')]
# )

# def predict(clicked, text):
#     if clicked:
#         text = [text]
#         text_vecs = vectorizer(text)
#         y_pred = model.predict(text_vecs)
#         if y_pred == 0:
#             y_pred = 'negative'
#         else:
#             y_pred = 'positive'
#         output = f'This is {y_pred} review.'
#     return output