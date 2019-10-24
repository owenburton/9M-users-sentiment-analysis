import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

from app import app

"""
https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout

Layout in Bootstrap is controlled using the grid system. The Bootstrap grid has 
twelve columns.

There are three main layout components in dash-bootstrap-components: Container, 
Row, and Col.

The layout of your app should be built as a series of rows of columns.

We set md=4 indicating that on a 'medium' sized or larger screen each column 
should take up a third of the width. Since we don't specify behaviour on 
smaller size screens Bootstrap will allow the rows to wrap so as not to squash 
the content.
"""
# from joblib import load
# model = 

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
        dcc.Link(dbc.Button('Rate your review!', color='primary', 
                            style=dict(marginTop=5, marginBottom=10)), 
                            href='/predictions'),
    ],
    md=5,
)

column2 = dbc.Col(
    [
        html.Img(src='assets/books.jpg', className='img-fluid')
    ]
)

layout = dbc.Row([column1, column2])