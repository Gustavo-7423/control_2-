import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Configuración de la barra lateral
st.sidebar.title("Análisis de Datos del S&P 500")
st.sidebar.header("Opciones de visualización")

# Cargar archivo CSV
uploaded_file = st.file_uploader("Sube el archivo de datos históricos del S&P 500", type=["csv"])
if uploaded_file is not None:
    # Leer el archivo CSV
    df = pd.read_csv(uploaded_file, sep=';')
    
    # Convertir la columna 'fecha' a tipo datetime
    df['fecha'] = pd.to_datetime(df['fecha'], format='%Y-%m-%d')
    
    # Mostrar los datos del archivo CSV
    st.write("Datos del archivo CSV:")
    st.dataframe(df)

    # Selección de columnas para el gráfico
    st.write("Seleccione las columnas para el gráfico de precios:")
    x_column = "fecha"  # Columna de fechas para el eje X
    y_column = st.selectbox("Seleccione el valor a graficar", ["ultimo", "apertura"])

    # Crear el gráfico si ambas columnas están seleccionadas
    if x_column and y_column:
        fig, ax = plt.subplots()
        ax.plot(df[x_column], df[y_column], label=y_column, color="blue")
        ax.set_title(f"Evolución de {y_column.capitalize()} a lo largo del tiempo")
        ax.set_xlabel("Fecha")
        ax.set_ylabel(y_column.capitalize())
        ax.legend()

        # Mostrar el gráfico en Streamlit
        st.pyplot(fig)
