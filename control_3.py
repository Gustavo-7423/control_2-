
import streamlit as st
import pandas as pd

st.markdown("# Datos historicos del indice bursatil S&P_500") 
st.header("<p style='font-size:12px;'>Aqui vemos los datos historicos del indice bursatil s&p 500</p>", unsafe_allow_html=True)
datos = pd.read_csv("Datos_históricos_del_S&P_500.csv")

st.bar_chart(datos)
