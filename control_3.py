from PIL import Image
import streamlit as st
import pandas as pd

st.markdown("# Datos historicos del indice bursatil S&P_500") 
st.markdown("<p style='font-size24px;'>Aqui veremos un grafico con los datos historicos de indice bursatil S&P 500</p>", unsafe_allow_html=True)

st.image("Bolsa_de_ny.jpg", width=300 )
datos = pd.read_csv("Datos_históricos_del_S&P_500.csv")

st.bar_chart(datos)
