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
        
            ## Insights

            ********

            When is this model useful? When is it not useful? Why is it useful? Why is it not useful?

            HERE'S A CONFUSION MATRIX

            HERE'S A CLASSIFICATION REPORT

            HERE'S A RANDOM REVIEW

            HERE'S A DIFFERENT KIND OF PRODUCT REVIEW

            """
        ),
    ],
    md=4,
)


column2 = dbc.Col(
    [
        
    ]
)

layout = dbc.Row([column1, column2])