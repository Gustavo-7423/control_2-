# -*- coding: utf-8 -*-
"""stremalit.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-BeOnyKJxNIBSGDlFWcJAgNml6LfTr2_
"""

import streamlit as st
import pandas as pd
import matplotlib as plt
st.sidebar.title("esta es una prueba")
st.sidebar.header("hola esto es una barra lateral")
st.sitebar.write("barra lateral ")

st.sidebar.image("descargar.jpg")
if st.sidebar.button("clik en la barra lateral "):
    st.sidebar.write("hixe un boton lateral ")
user_input = st.sidebar.text_input("escribe algo en la barra ")
st.sidebar.write("Escribiste en la barra ", user_input)
