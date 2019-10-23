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
        
            ## Predictions

            ********

            This binary classifier has a majority class baseline of about 81%.
            The model I used has an accuracy of 85%, beating the baseline accuracy on a hold-out test set.

            HERE'S A SHAPLEY VALUES PLOT

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