
import streamlit as st
import pandas as pd
st.markdown("<p style='font-size:12px;'>Texto pequeño en Streamlit</p>", unsafe_allow_html=True)
st.markdown("# Datos historicos del indice bursatil S&P_500") 
st.header("Aqui vemos los datos historicos del indice bursatil s&p 500")
datos = pd.read_csv("Datos_históricos_del_S&P_500.csv")

st.bar_chart(datos)
