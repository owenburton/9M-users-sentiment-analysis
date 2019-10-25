import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
# New imports
import plotly.graph_objects as go
import plotly.express as px
import plotly.figure_factory as ff
import pandas as pd

from app import app

# Confusion Matrix
z_string = [['761,486','932,601'],['333,213','6,870,150']]
z = [[761486,932601],[333213,6870150]]

colorscale=[[0, 'pink'], [1, 'red']]
font_colors = ['black', 'pink']
y=['Actual-neg','Actual-pos']
x=['Pred-neg','Pred-pos']
x_labels=['Predicted Negative','Predicted Positive']
y_labels=['Actual Negative','Actual Positive']
hovertext = list()
for yi, yy in enumerate(y_labels):
    hovertext.append(list())
    for xi, xx in enumerate(x_labels):
        hovertext[-1].append('{}<br />{}<br />{}'.format(xx, yy, z[yi][xi]))

fig1 = ff.create_annotated_heatmap(z, x=x, y=y, xgap = 2, ygap = 2, 
                                   hoverinfo="text", text=hovertext, annotation_text=z_string, 
                                   colorscale=colorscale, font_colors=font_colors)

fig1.update_layout(title='Most of the prediction errors were false positives.',
                   xaxis = dict(ticks = ""),
                   yaxis = dict(ticks = "")) 

index = ['Negative', 'Positive', 'macro avg', 'weighted avg']
columns = ['Precision', "Recall", "f1-Score"]
observations = [[0.70, 0.45, 0.55],[0.88, 0.95, 0.92],[0.79, 0.70, 0.73],[0.85, 0.86, 0.85]]
cr = pd.DataFrame(index=index, data=observations, columns=columns)

fig2 = go.Figure(data=[go.Table(
    columnwidth = [400,300,300,300],
    header=dict(values=[''] + list(cr.columns),
                align='left'),
    cells=dict(values=[['Negative', 'Positive','macro avg', 'weighted avg'], cr['Precision'], cr['Recall'], cr['f1-Score']],
               align='left',
               height=60))
])

fig2.update_layout(title='Classification Report for Binary Book Review Classifier')

column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## **Insights**

            ********

            ##### **Is the app guessing correctly?**

            The model I used to predict your book review's tone has limits. Out of nine million reviews, 
            it guessed the correct feeling 86% of the time. If you had guessed the most common type, "positive",
            then you'd be right for 81% of your guesses. 
            
            Look at the red and pink confusion matrix to see where most of the model's predictions were wrong.

            ##### **Why are some predictions wrong?**
            
            There's way more positive than negative reviews, but I accounted for imbalanced class weights in the model.
            For simplicity, I also made this a binary classification problem: negative or positive. The trade-off's 
            that it's harder to explain the model's results. Are these really all negative, or are some neutral, three-star
            reviews?

            The model is also distracted by noise, or words that aren't helpful for determining the feeling of a review.
            I address this by removing stop-words like "and" or "it".

            Another reason for the inaccuracies is that I'm using a simple way to change words to numbers. Part of the funnel
            counts all the words in each review, adjusts their relevance by how often they occur in the text, and associates
            sentiment to each word. It's not taking into account more complex relationships in the syntax.
            I could use a more complex model, but this would slow down the time it took to get a rating for your review.

            """
        ),

        dcc.Graph(figure=fig2, style={'marginTop': '2.5em'}),
        # dcc.Graph(figure=fig1, style={'marginTop': '3em'}),
    ],
    md=6,
)

column2 = dbc.Col(
    [
        # dcc.Graph(figure=fig2, style={'marginTop': '2.5em'}),
        dcc.Graph(figure=fig1, style={'marginTop': '3em'}),

        dcc.Markdown(
            """
            ##### **How else can the model be improved?**
            
            If the cost made sense, it's exciting to know there are many, easy ways this model can be improved.
            If it was in the business's best interest, I could manually add specific common words used in
            the reviews to the list of removed stop-words. I could train the model on more data, use
            more accurate ways to represent the meaning of words as numbers, or use a more complex model.

            It depends how much money we want to spend to get more accurate results.

            ##### **Is this app useful?**

            It's mostly for demostration purposes, not a production environment, but with a pipeline that
            collects and feeds in reviews in real-time, the model becomes useful. It can be trained on reviews of
            different products to become more adaptable. 
            
            Also, this process doesn't only have to detect sentiment. It can be trained to detect anomalies in text.
            Large companies like Lockheed Martin are using a similar process in a pipeline that aggregates tweets
            from businesses along their supply chain to predict potential costly disruptions.

            Head over to the "Process" page for the details behind the model I used.

            """
        ),
    ],
    md=6,
)

layout = dbc.Row([column1, column2])