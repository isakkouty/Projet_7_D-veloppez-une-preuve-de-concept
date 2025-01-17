import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Charger les résultats des modèles avec vos données réelles
data = {
    "Modèle": ["LSTM Simple", "LSTM Empilé", "Snapshot Ensemble"],
    "MAE": [0.0098, 0.0083, 0.0443],
    "RMSE": [0.0233, 0.0231, 0.0344],
    "R2": [0.2126, 0.2276, -1.8445]
}
df_results = pd.DataFrame(data)

# Données des prédictions (exemple avec données fictives)
comparison_data = {
    "Index": list(range(100)),
    "Réel": [1.5 + 0.01 * i for i in range(100)],
    "LSTM Simple": [1.5 + 0.01 * i + 0.005 for i in range(100)],  # Exemple ajusté
    "LSTM Empilé": [1.5 + 0.01 * i + 0.002 for i in range(100)],  # Exemple ajusté
    "Snapshot Ensemble": [1.5 + 0.01 * i + 0.01 for i in range(100)]  # Exemple ajusté
}
df_comparison = pd.DataFrame(comparison_data)

# Titre principal
st.title("Dashboard de Preuve de Concept - Modélisation LSTM")

# Onglet : Performances des modèles
st.header("Performances des Modèles")

# Graphique 1 : MAE et RMSE
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

# Graphique 2 : R2
fig_r2 = go.Figure()
fig_r2.add_trace(go.Bar(name='R2', x=df_results['Modèle'], y=df_results['R2'], marker_color='green'))
fig_r2.update_layout(
    title="Comparaison des Scores R2",
    xaxis_title="Modèles",
    yaxis_title="R2"
)
st.plotly_chart(fig_r2)

# Onglet : Comparaison des prédictions
st.header("Comparaison des Prédictions")

fig_preds = go.Figure()
fig_preds.add_trace(go.Scatter(x=df_comparison["Index"], y=df_comparison["Réel"], mode='lines', name='Réel'))
fig_preds.add_trace(go.Scatter(x=df_comparison["Index"], y=df_comparison["LSTM Simple"], mode='lines', name='LSTM Simple'))
fig_preds.add_trace(go.Scatter(x=df_comparison["Index"], y=df_comparison["LSTM Empilé"], mode='lines', name='LSTM Empilé'))
fig_preds.add_trace(go.Scatter(x=df_comparison["Index"], y=df_comparison["Snapshot Ensemble"], mode='lines', name='Snapshot Ensemble'))
fig_preds.update_layout(
    title="Comparaison des Prédictions vs Réalités",
    xaxis_title="Index",
    yaxis_title="Valeurs"
)
st.plotly_chart(fig_preds)
