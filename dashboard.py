import streamlit as st
import pandas as pd
import plotly.graph_objects as go

data = {
    "Modèle": ["LSTM Simple", "LSTM Empilé", "Snapshot Ensemble"],
    "MAE": [0.0098, 0.0083, 0.0443],
    "RMSE": [0.0233, 0.0231, 0.0344],
    "R2": [0.2126, 0.2276, -1.8445]
}
df_results = pd.DataFrame(data)


st.title("Dashboard de Preuve de Concept - Modélisation LSTM")

st.header("Performances des Modèles")

fig_perf = go.Figure()
fig_perf.add_trace(go.Bar(name='MAE', x=df_results['Modèle'], y=df_results['MAE'], marker_color='skyblue'))
fig_perf.add_trace(go.Bar(name='RMSE', x=df_results['Modèle'], y=df_results['RMSE'], marker_color='orange'))
fig_perf.update_layout(
    title="Comparaison des Performances (MAE et RMSE)",
    xaxis_title="Modèles",
    yaxis_title="Valeurs",
    barmode='group'
)
st.plotly_chart(fig_perf)

fig_r2 = go.Figure()
fig_r2.add_trace(go.Bar(name='R2', x=df_results['Modèle'], y=df_results['R2'], marker_color='green'))
fig_r2.update_layout(
    title="Comparaison des Scores R2",
    xaxis_title="Modèles",
    yaxis_title="R2"
)
st.plotly_chart(fig_r2)