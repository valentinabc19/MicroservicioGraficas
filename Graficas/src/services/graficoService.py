import plotly.express as px
import pandas as pd

def generar_grafico_promedio_estudiante(datos):
    df = pd.DataFrame(datos)
    df_grouped = df.groupby('periodo')['nota'].mean().reset_index()
    
    fig = px.line(df_grouped, x='periodo', y='nota', markers=True, title='Promedio del Estudiante por Periodo')
    fig.show()  # Muestra el gráfico interactivo

