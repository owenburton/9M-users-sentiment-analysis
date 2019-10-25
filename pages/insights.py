import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
# New imports
import plotly.graph_objects as go
import plotly.express as px
import plotly.figure_factory as ff

from app import app

# Confusion Matrix
z = [[761486,932601],[ 333213,6870150]]

colorscale=[[0, 'blue'], [1, 'pink']]
font_colors = ['white', 'black']
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
                                   hoverinfo="text", text=hovertext, annotation_text=z, 
                                   colorscale=colorscale, font_colors=font_colors)

fig1.update_layout(title='Confusion Matrix for Binary Book Review Classifier',
                   xaxis = dict(ticks = ""),
                   yaxis = dict(ticks = "")) 

df = pd.read_csv('https://raw.githubusercontent.com/owenburton/unit2_build1/notebooks/cr.csv', index_col=0)

fig2 = go.Figure(data=[go.Table(
    columnwidth = [400,300,300,300],
    header=dict(values=[''] + list(df.columns),
                align='left'),
    cells=dict(values=[['Negative', 'Positive','macro avg', 'weighted avg'], df['Precision'], df['Recall'], df['f1-Score']],
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

            ##### **Another title**

            This binary classifier has a majority class baseline of about 81%.
            The model I used has an accuracy of 85%, beating the baseline accuracy on a hold-out test set.

            HERE'S A SHAPLEY VALUES PLOT
            ********
            ##### **Another title**

            When is this model useful? When is it not useful? Why is it useful? Why is it not useful?

            HERE'S A CONFUSION MATRIX

            HERE'S A CLASSIFICATION REPORT

            HERE'S A RANDOM REVIEW

            HERE'S A DIFFERENT KIND OF PRODUCT REVIEW

            """
        ),

        dcc.Graph(figure=fig1, style={'marginTop': '3em'}),
    ],
    md=6,
)

column2 = dbc.Col(
    [
        # dcc.Graph(figure=fig2, style={'marginTop': '2.5em'}),

        dcc.Markdown(
            """
            ##### **This is a bunch of text about the visualization above**
            
            ********

            It's important to understand how customers feel about the products they're using, but 
            most businesses wouldn't spend the labor hours to manually read millions of reviews.
            
            With a simple example of book review analysis, 
            I'll show you one way user sentiment can be tracked automatically, quickly, and at scale.

            ##### **Not sure if I'll need this title**
            """
        ),
    ],
    md=6,
)

layout = dbc.Row([column1, column2])