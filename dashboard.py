import streamlit as st
import pandas as pd
import plotly.graph_objects as go

linear_data = {
    "Modèle": ["Elastic Net", "Random Forest Regressor", "SVM"],
    "MAE": [0.417259, 0.099317, 0.415443],
    "RMSE": [0.904976, 0.994616, 0.905801],
    "R2": [1.0, 0.238023, 0.995648]
}
df_linear = pd.DataFrame(linear_data)

lstm_data = {
    "Modèle": ["LSTM Simple (2016)", "LSTM Simple (2015-present)", "LSTM Empilé (2015-present)", "Snapshot Ensemble (2015-present)"],
    "MAE": [0.09488454437605992, 0.0394, 0.0395, 0.0403],
    "RMSE": [0.1568012656256108, 0.0716, 0.0753, 0.0717],
    "R2": [0.20403372760140126, 0.7516, 0.7249, 0.7509]
}
df_lstm = pd.DataFrame(lstm_data)

df_combined = pd.concat([df_linear, df_lstm], ignore_index=True)

st.title("Dashboard de Preuve de Concept - Modélisation")

st.header("Performances des Modèles")
st.write("**Résultats combinés des modèles de régression linéaire et LSTM**")
st.dataframe(df_combined)

st.subheader("Performances des Modèles de Régression Linéaire")
fig_linear = go.Figure()
fig_linear.add_trace(go.Bar(name='MAE', x=df_linear['Modèle'], y=df_linear['MAE'], marker_color='skyblue'))
fig_linear.add_trace(go.Bar(name='RMSE', x=df_linear['Modèle'], y=df_linear['RMSE'], marker_color='orange'))
fig_linear.update_layout(
    title="Comparaison des Performances (MAE et RMSE) - Régression Linéaire",
    xaxis_title="Modèles",
    yaxis_title="Valeurs",
    barmode='group'
)
st.plotly_chart(fig_linear)

fig_linear_r2 = go.Figure()
fig_linear_r2.add_trace(go.Bar(name='R2', x=df_linear['Modèle'], y=df_linear['R2'], marker_color='green'))
fig_linear_r2.update_layout(
    title="Comparaison des Scores R2 - Régression Linéaire",
    xaxis_title="Modèles",
    yaxis_title="R2"
)
st.plotly_chart(fig_linear_r2)

st.subheader("Performances des Modèles LSTM")
fig_lstm = go.Figure()
fig_lstm.add_trace(go.Bar(name='MAE', x=df_lstm['Modèle'], y=df_lstm['MAE'], marker_color='skyblue'))
fig_lstm.add_trace(go.Bar(name='RMSE', x=df_lstm['Modèle'], y=df_lstm['RMSE'], marker_color='orange'))
fig_lstm.update_layout(
    title="Comparaison des Performances (MAE et RMSE) - LSTM",
    xaxis_title="Modèles",
    yaxis_title="Valeurs",
    barmode='group'
)
st.plotly_chart(fig_lstm)

fig_lstm_r2 = go.Figure()
fig_lstm_r2.add_trace(go.Bar(name='R2', x=df_lstm['Modèle'], y=df_lstm['R2'], marker_color='green'))
fig_lstm_r2.update_layout(
    title="Comparaison des Scores R2 - LSTM",
    xaxis_title="Modèles",
    yaxis_title="R2"
)
st.plotly_chart(fig_lstm_r2)

st.subheader("Comparaison Globale des Modèles")
fig_combined = go.Figure()
fig_combined.add_trace(go.Bar(name='MAE', x=df_combined['Modèle'], y=df_combined['MAE'], marker_color='skyblue'))
fig_combined.add_trace(go.Bar(name='RMSE', x=df_combined['Modèle'], y=df_combined['RMSE'], marker_color='orange'))
fig_combined.update_layout(
    title="Comparaison des Performances (MAE et RMSE) - Tous les Modèles",
    xaxis_title="Modèles",
    yaxis_title="Valeurs",
    barmode='group'
)
st.plotly_chart(fig_combined)

fig_combined_r2 = go.Figure()
fig_combined_r2.add_trace(go.Bar(name='R2', x=df_combined['Modèle'], y=df_combined['R2'], marker_color='green'))
fig_combined_r2.update_layout(
    title="Comparaison des Scores R2 - Tous les Modèles",
    xaxis_title="Modèles",
    yaxis_title="R2"
)
st.plotly_chart(fig_combined_r2)
