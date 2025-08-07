import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Page config
st.set_page_config(layout="wide")

# Load data
file_path = "Data 75%-25%.xlsx"  # Assumes file is in same directory
df = pd.read_excel(file_path)
df.columns = [col.strip(" `") for col in df.columns]
df['Period'] = pd.to_datetime(df['Period'])

# Preprocessing
df['Spread_mult100'] = df['Spread'] * 100
lines = {
    'Average Spread: x\u0304 (excluding GFC)': df['x'].iloc[0] * 100,
    'Average Spread: x\u0304 + σ': df['x + s'].iloc[0] * 100,
    'Average Spread: x\u0304 – σ': df['x – s'].iloc[0] * 100,
}

# Build Plotly figure
fig = go.Figure()

fig.add_trace(go.Scatter(
    x=df['Period'],
    y=df['Spread_mult100'],
    mode='lines',
    name='Spot Spread: 75% – 25%',
    line=dict(color='green'),
    hovertemplate='Spread: %{y:.2f}%<extra></extra>'
))

line_styles = {
    'Average Spread: x\u0304 (excluding GFC)': dict(dash='dash', width=2),
    'Average Spread: x\u0304 + σ': dict(dash='dot'),
    'Average Spread: x\u0304 – σ': dict(dash='dot'),
}

for label, y_val in lines.items():
    fig.add_trace(go.Scatter(
        x=[df['Period'].min(), df['Period'].max()],
        y=[y_val, y_val],
        mode='lines+text',
        name=label,
        line=dict(color='green', **line_styles[label]),
        text=[label, ''],
        textposition='top right',
        hoverinfo='skip'
    ))

fig.update_layout(
    title=dict(
        text=None,
        x=0.5,
        xanchor='center'
    ),
    yaxis=dict(
        title="Estimated Annual Interest Expense (k<sub>d</sub>)",
        ticks="outside",
        showgrid=True,
        zeroline=True,
        zerolinewidth=1,
        zerolinecolor='LightPink',
        ticksuffix="%",
    ),
    xaxis=dict(
        tickformat='%Y',
        dtick="M24",
        hoverformat='%Y-%m-%d'
    ),
    hovermode='x unified',
    template='plotly_white',
    legend=dict(y=0.99, x=0.01),
    margin=dict(t=60, l=60, r=40, b=60),
    height=600
)

# Render with Streamlit
st.plotly_chart(fig, use_container_width=True)
