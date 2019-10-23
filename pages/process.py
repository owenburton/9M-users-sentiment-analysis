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

            HERE'S CODE SHOWING HOW THE TEXT IS CLEANED

            HERE'S CODE SHOWING THE TOKENIZING/VECTORIZER FUNCTIONS

            HERE'S A SNIPPET OF CODE SHOWING LGBMCLASSIFIER

            CAN YOU FIGURE OUT HOW TO USE SPACY'S CNN TEXT CLASSIFIER?


            """
        ),

    ],
)

layout = dbc.Row([column1])