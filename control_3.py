import streamlit as st
import pandas as pd


datos = pd.read_csv("Datos_históricos_del_S&P_500.csv")
print(datos)
st.area_chart(datos)
st.markdown("# datos historicos del indice bursatil S&P_500")
