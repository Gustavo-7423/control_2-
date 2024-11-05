
import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar el archivo CSV
uploaded_file = '/mnt/data/Datos históricos del S&P 500.csv'
data = pd.read_csv(uploaded_file)

# Asegurarse de que la columna de fecha esté en el formato de fecha correcto
data['Fecha'] = pd.to_datetime(data['Fecha'], errors='coerce')

# Eliminar filas con fechas inválidas
data = data.dropna(subset=['Fecha'])

# Ordenar datos por fecha
data = data.sort_values(by='Fecha')

# Verificar si el archivo contiene la columna de máximos
if 'Máximos' in data.columns:
    # Crear el gráfico de barras con Plotly
    fig = px.bar(data, x='Fecha', y='Máximos', title='Máximos del S&P 500 a lo largo del tiempo')
    
    # Mostrar gráfico en Streamlit
    st.plotly_chart(fig)
else:
    st.write("La columna 'Máximos' no se encontró en el archivo CSV.")

"""
st.markdown("# Datos historicos del indice bursatil S&P_500") 

datos = pd.read_csv("Datos_históricos_del_S&P_500.csv",sep",")
print(datos)
st.bar_chart(datos)"""
