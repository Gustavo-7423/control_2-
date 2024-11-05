import streamlit as st
import pandas as pd


st.markdown("# datos historicos del indice bursatil S&P_500")

datos = pd.read_csv("Datos_históricos_del_S&P_500.csv")
print(datos)
st.area_chart(datos)
