import plotly.graph_objects as go
import plotly.express as px
import numpy as np

# Define table data with positions
tables = {
    "indicadores": {"pos": [200, 50], "color": "#1FB8CD"},
    "boas_praticas": {"pos": [200, 200], "color": "#DB4545"},
    "equipes": {"pos": [50, 350], "color": "#2E8B57"},
    "usuarios": {"pos": [250, 350], "color": "#5D878F"},
    "atendimentos": {"pos": [450, 350], "color": "#D2BA4C"},
    "procedimentos_realizados": {"pos": [650, 350], "color": "#B4413C"},
    "vacinacoes": {"pos": [450, 500], "color": "#964325"},
    "indicadores_resultados": {"pos": [200, 500], "color": "#944454"}
}

# Define relationships
relationships = [
    ("boas_praticas", "indicadores"),
    ("usuarios", "equipes"),
    ("atendimentos", "usuarios"),
    ("atendimentos", "equipes"),
    ("procedimentos_realizados", "atendimentos"),
    ("vacinacoes", "usuarios"),
    ("indicadores_resultados", "indicadores"),
    ("indicadores_resultados", "equipes")
]

fig = go.Figure()

# Add relationship lines
for rel in relationships:
    from_table, to_table = rel
    from_pos = tables[from_table]["pos"]
    to_pos = tables[to_table]["pos"]
    
    fig.add_trace(go.Scatter(
        x=[from_pos[0], to_pos[0]],
        y=[from_pos[1], to_pos[1]],
        mode='lines',
        line=dict(color='gray', width=2),
        showlegend=False,
        hoverinfo='skip',
        cliponaxis=False
    ))

# Add table nodes
table_names = []
x_pos = []
y_pos = []
colors = []

for table_name, table_info in tables.items():
    # Truncate table names to 15 characters
    display_name = table_name.replace('_', ' ')
    if len(display_name) > 15:
        if 'procedimentos' in display_name:
            display_name = 'Procedures'
        elif 'indicadores' in display_name and 'resultados' in display_name:
            display_name = 'Indic Results'
        elif 'boas' in display_name:
            display_name = 'Best Practices'
        else:
            display_name = display_name[:15]
    
    table_names.append(display_name.title())
    x_pos.append(table_info["pos"][0])
    y_pos.append(table_info["pos"][1])
    colors.append(table_info["color"])

fig.add_trace(go.Scatter(
    x=x_pos,
    y=y_pos,
    mode='markers+text',
    marker=dict(
        size=40,
        color=colors,
        line=dict(width=2, color='white')
    ),
    text=table_names,
    textposition="middle center",
    textfont=dict(size=9, color='white', family='Arial Black'),
    showlegend=False,
    hovertemplate='%{text}<extra></extra>',
    cliponaxis=False
))

fig.update_layout(
    title="Database ERD",
    xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
    yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
    plot_bgcolor='white'
)

fig.write_image("database_erd.png")