pip install dash plotly pandas flask gunicorn

import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import pandas as pd

data = {
    "Modèle": ["LSTM Simple", "LSTM Empilé", "Snapshot Ensemble"],
    "MAE": [0.0098, 0.0083, 0.0443],
    "RMSE": [0.0233, 0.0231, 0.0344],
    "R2": [0.2126, 0.2276, -1.8445]
}
df_results = pd.DataFrame(data)


comparison_data = {
    "Index": list(range(100)),
    "Réel": [1.5 + 0.01 * i for i in range(100)],
    "LSTM Simple": [1.5 + 0.01 * i + 0.005 for i in range(100)], 
    "LSTM Empilé": [1.5 + 0.01 * i + 0.002 for i in range(100)],  
    "Snapshot Ensemble": [1.5 + 0.01 * i + 0.01 for i in range(100)]  
}
df_comparison = pd.DataFrame(comparison_data)

# App Dash
app = dash.Dash(__name__)
server = app.server 

# Layout du dashboard
app.layout = html.Div([
    html.H1("Dashboard de Preuve de Concept - Modélisation LSTM", style={'textAlign': 'center'}),
    dcc.Tabs([
        # Tab 1 : Visualisation des performances
        dcc.Tab(label='Performances des Modèles', children=[
            dcc.Graph(
                id='metrics-graph',
                figure={
                    'data': [
                        go.Bar(name='MAE', x=df_results['Modèle'], y=df_results['MAE'], marker_color='skyblue'),
                        go.Bar(name='RMSE', x=df_results['Modèle'], y=df_results['RMSE'], marker_color='orange'),
                    ],
                    'layout': go.Layout(
                        title='Comparaison des Performances (MAE et RMSE)',
                        barmode='group',
                        xaxis_title='Modèles',
                        yaxis_title='Valeurs',
                    )
                }
            ),
            dcc.Graph(
                id='r2-graph',
                figure={
                    'data': [
                        go.Bar(name='R2', x=df_results['Modèle'], y=df_results['R2'], marker_color='green'),
                    ],
                    'layout': go.Layout(
                        title='Comparaison des Scores R2',
                        xaxis_title='Modèles',
                        yaxis_title='R2',
                    )
                }
            )
        ]),

        # Tab 2 : Comparaison des prédictions
        dcc.Tab(label='Comparaison des Prédictions', children=[
            dcc.Graph(
                id='predictions-graph',
                figure={
                    'data': [
                        go.Scatter(
                            x=df_comparison["Index"], 
                            y=df_comparison["Réel"], 
                            mode='lines', 
                            name='Réel'
                        ),
                        go.Scatter(
                            x=df_comparison["Index"], 
                            y=df_comparison["LSTM Simple"], 
                            mode='lines', 
                            name='LSTM Simple'
                        ),
                        go.Scatter(
                            x=df_comparison["Index"], 
                            y=df_comparison["LSTM Empilé"], 
                            mode='lines', 
                            name='LSTM Empilé'
                        ),
                        go.Scatter(
                            x=df_comparison["Index"], 
                            y=df_comparison["Snapshot Ensemble"], 
                            mode='lines', 
                            name='Snapshot Ensemble'
                        ),
                    ],
                    'layout': go.Layout(
                        title='Comparaison des Prédictions vs Réalités',
                        xaxis_title='Index',
                        yaxis_title='Valeurs',
                    )
                }
            )
        ])
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True)