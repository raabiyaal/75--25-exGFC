import pandas as pd
from dash import Dash, dcc, html
import plotly.graph_objects as go
import os

# Load data inside the app file
file_path = r"Data 75%-25%.xlsx"
df = pd.read_excel(file_path)
df['Period'] = pd.to_datetime(df['Period'])

app = Dash(__name__)

fig = go.Figure()

# Main spread line (no multiplication, raw decimal)
fig.add_trace(go.Scatter(
    x=df['Period'],
    y=df['Spread'],
    mode='lines',
    line=dict(color='green', width=2),
    name='Spot Spread: 75% – 25%',
    hovertemplate='%{x|%b %d, %Y} — %{y:.1%}<extra></extra>'
))

# Horizontal lines using add_hline with annotations and positions
fig.add_hline(
    y=df['x'].iloc[0],
    line=dict(color='green', dash='dash', width=2),
    annotation_text="Average Spread: x̄ (excluding GFC)",  # Added excluding GFC here
    annotation_position="top left",
    name="Average Spread: x̄ (excluding GFC)"
)
fig.add_hline(
    y=df['x + s'].iloc[0],
    line=dict(color='green', dash='dot', width=2),
    annotation_text="Average Spread: x̄ + σ",
    annotation_position="top left",
    name="Average Spread: x̄ + σ"
)
fig.add_hline(
    y=df['x – s'].iloc[0],
    line=dict(color='green', dash='dot', width=2),
    annotation_text="Average Spread: x̄ – σ",
    annotation_position="bottom left",
    name="Average Spread: x̄ – σ"
)

fig.update_layout(
    yaxis_title=r'Estimated Annual Interest Expense (k<sub>d</sub>)',
    yaxis=dict(range=[0, 0.1], tickformat=".0%", dtick=0.01),
    legend=dict(
        font=dict(size=12),
        bgcolor='rgba(255,255,255,0.8)',
        bordercolor='black',
        borderwidth=1,
        x=0.01,  # legend x position (near left)
        y=0.99,  # legend y position (near top)
        yanchor='top',
        xanchor='left'
    ),
    template='simple_white',
    showlegend=True,
    margin=dict(t=30, b=20, l=20, r=20)
)

app.layout = html.Div([
    dcc.Graph(figure=fig, style={'width': '90%', 'height': '80vh', 'margin': 'auto'})
])

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8050))
<<<<<<< HEAD
    app.run(host='0.0.0.0', port=port, debug=False, use_reloader=False)
=======
    app.run(host='0.0.0.0', port=port, debug=False, use_reloader=False)
>>>>>>> fd990ff3c58844a2424f3d6a4be4678a126d88a6
