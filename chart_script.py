import plotly.express as px
import pandas as pd

# Create the data from the JSON
indicadores_data = [
    {"codigo": "C1", "nome": "Mais Acesso APS", "categoria": "Acesso"},
    {"codigo": "C2", "nome": "Cuidado Desenvolv", "categoria": "Cuidado"},
    {"codigo": "C3", "nome": "Cuidado Gestante", "categoria": "Cuidado"},
    {"codigo": "C4", "nome": "Cuidado Diabetes", "categoria": "Cuidado"},
    {"codigo": "C5", "nome": "Cuidado Hiperten", "categoria": "Cuidado"},
    {"codigo": "C6", "nome": "Cuidado Idosa", "categoria": "Cuidado"},
    {"codigo": "C7", "nome": "Cuidado Cancer", "categoria": "Cuidado"},
    {"codigo": "B1", "nome": "1a Consulta Prog", "categoria": "Saúde Bucal"},
    {"codigo": "B2", "nome": "Tratamento Concl", "categoria": "Saúde Bucal"},
    {"codigo": "B3", "nome": "Taxa Exodontia", "categoria": "Saúde Bucal"},
    {"codigo": "B4", "nome": "Escovacao Super", "categoria": "Saúde Bucal"},
    {"codigo": "B5", "nome": "Proced Prevent", "categoria": "Saúde Bucal"},
    {"codigo": "B6", "nome": "Trat Restaurador", "categoria": "Saúde Bucal"},
    {"codigo": "M1", "nome": "Media Atend eMu", "categoria": "Multiprofissional"},
    {"codigo": "M2", "nome": "Acoes Interprof", "categoria": "Multiprofissional"}
]

# Create DataFrame
df = pd.DataFrame(indicadores_data)

# Add dummy values for bar length
df['valor'] = 1

# Create labels with code and name
df['label'] = df['codigo'] + ': ' + df['nome']

# Define color mapping according to user requirements
color_map = {
    'Cuidado': '#2E8B57',        # Green
    'Saúde Bucal': '#1FB8CD',    # Blue (cyan)  
    'Multiprofissional': '#DB4545', # Red
    'Acesso': '#9370DB'          # Purple
}

# Create horizontal bar chart
fig = px.bar(df, 
             x='valor', 
             y='label',
             color='categoria',
             orientation='h',
             color_discrete_map=color_map,
             title='Indicadores APS por Categoria')

# Update layout
fig.update_layout(
    showlegend=True,
    legend=dict(orientation='h', yanchor='bottom', y=1.05, xanchor='center', x=0.5),
    xaxis_title='',
    yaxis_title=''
)

# Hide x-axis since we just want to show categories
fig.update_xaxes(showticklabels=False, showgrid=False)

# Save the chart
fig.write_image('indicadores_aps.png')