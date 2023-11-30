import streamlit as st
import datetime as dt
import pandas as pd

if "emplois1" not in st.session_state:
    st.session_state["emplois"]=pd.DataFrame()
example1 = pd.read_csv(
            "https://docs.google.com/spreadsheets/d/1tWMj4Lfe22t2aUuLiromCUhAN5bsXA4OFPI_sXz6ELQ/gviz/tq?tqx=out:csv&sheet=emplois_3_4")
st.info("Emplois du temps de 3 et 4 aep: ")
st.table(example1)
st.session_state["emplois1"]=example1


if "emplois2" not in st.session_state:
    st.session_state["emplois2"]=pd.DataFrame()
example2 = pd.read_csv(r"C:\Users\hp\Downloads\2_emplois_3_4.csv")
st.info("Emplois du temps de 3 et 4 aep: ")
st.table(example2)
st.session_state["emplois2"]=example2
