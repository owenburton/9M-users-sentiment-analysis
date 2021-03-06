import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.express as px
from joblib import load

from app import app

vectorizer = load('assets/vectorizer.joblib')
model = load('assets/model.joblib')

column1 = dbc.Col(
    [
        dcc.Markdown(
            """
            ## **How do nine million users feel?**
            
            ********

            It's important to understand how customers feel about the products they're using, but 
            most businesses wouldn't spend the labor hours to manually read millions of reviews.
            
            With a book review analysis, I'll show you one way user sentiment can be tracked automatically, quickly, and at scale.
            Next, check out the Insights and Process pages to see how the underlying model can be changed
            to solve other business problems.
            

            ##### **Copy-paste or write a book review below.**
            """
        ),
        dcc.Textarea(
            id='input-box',
            placeholder='Max length: 5000 words',
            value="I loved Excession. It's amazing how creative Iain Banks is. Incredible space opera with AI ethics questions? Gimme 1000 more.",
            cols=50,
            rows=3,
            maxLength=5000,
            style={'width': '100%', 'marginBottom': '1.25em', 'marginTop':'1em'}
        ),
        dbc.Button('Rate your review!', id='button', n_clicks=1, color='primary', 
                   style=dict(marginTop=1.75, marginBottom=10)
        ),
        dcc.Markdown('##### Prediction:', style={'marginBottom': '0'}), 
        html.Div(id='prediction-label', className='lead', 
                 style={'marginBottom': '0', 'fontWeight': 'bold', 'fontSize': '18px'}),
    ],
    md=6,
)

column2 = dbc.Col(
    [
        html.Img(src='assets/books.jpg', className='img-fluid', style={'marginTop': '2.5em'})
    ],
    md=6,
)

layout = dbc.Row([column1, column2])

@app.callback(
    [Output('prediction-label', 'children')],
    [Input('button', 'n_clicks')],
    [State('input-box', 'value')]
)

def predict(clicked, text):
    if clicked:
        text = [text]
        text_vecs = vectorizer.transform(text)
        y_pred = model.predict(text_vecs)
        if y_pred[0] == 0.0:
            y_pred = 'negative'
        else:
            y_pred = 'positive'
        output = [f'That is a {y_pred} review.']
    return output

# y_preds = model.predict(X_test_vecs)
# y_preds = pd.DataFrame(y_preds)
# y_preds.columns = ['preds']
# print("Test Accuracy:", accuracy_score(y_test, y_preds))