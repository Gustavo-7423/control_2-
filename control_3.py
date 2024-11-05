
import streamlit as st
import pandas as pd


st.sidebar.title("Esta es una prueba")
st.sidebar.header("Hola esto es una barra lateral")
st.sidebar.write("Barra lateral ")

st.sidebar.image("madrir.png")

if st.sidebar.button("Clik en la barra lateral "):
    st.sidebar.write("Hice un boton lateral ")
user_input = st.sidebar.text_input("escribe algo en la barra ") # esto hace que el usuario ingrese palabra y aparezcan en la barra lateral 
st.sidebar.write("Escribiste en la barra:  ", user_input)
st.title("Esta es mi primera pagina")
st.header("MI primera página")
st.image("madrir.png")

import streamlit as st
import plotly.express as px
import numpy as np

# Crear algunos datos
x = np.linspace(0, 10, 100)
y = np.cos(x)

# Crear el gráfico usando Plotly
fig = px.line(x=x, y=y, title="Gráfico de Coseno")
fig.update_layout(xaxis_title="X", yaxis_title="cos(X)")

# Mostrar el gráfico en Streamlit
st.title("Gráfico usando Plotly en Streamlit")
st.plotly_chart(fig)
