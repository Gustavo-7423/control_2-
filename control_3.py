import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Configuración de la barra lateral
st.sidebar.title("Esta es una prueba")
st.sidebar.header("Hola esto es una barra lateral")
st.sidebar.write("Barra lateral ")

# Mostrar una imagen en la barra lateral (asegúrate de tener 'madrir.png' en la misma carpeta)
st.sidebar.image("madrir.png")

# Botón en la barra lateral que muestra un mensaje cuando se hace clic
if st.sidebar.button("Clik en la barra lateral"):
    st.sidebar.write("Hice un botón lateral")

# Campo de texto en la barra lateral donde el usuario puede escribir algo
user_input = st.sidebar.text_input("Escribe algo en la barra")
st.sidebar.write("Escribiste en la barra:", user_input)

# Configuración de la página principal
st.title("Esta es mi primera página")
st.header("MI primera página")

# Mostrar la imagen en la página principal (asegúrate de tener 'madrir.png' en la misma carpeta)
st.image("madrir.png")

# Crear un gráfico con Matplotlib
x = np.linspace(0, 10, 100)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y, label="Seno de X", color="blue")
ax.set_title("Gráfico de Seno")
ax.set_xlabel("X")
ax.set_ylabel("sin(X)")
ax.legend()

# Mostrar el gráfico en Streamlit
st.pyplot(fig)
