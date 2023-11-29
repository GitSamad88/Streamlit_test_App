import streamlit as st
import datetime as dt
import pandas as pd

if "emplois" not in st.session_state:
    st.session_state["emplois"]=pd.DataFrame()
example = pd.read_csv(
            "https://docs.google.com/spreadsheets/d/1tWMj4Lfe22t2aUuLiromCUhAN5bsXA4OFPI_sXz6ELQ/gviz/tq?tqx=out:csv&sheet=emplois_3_4")
st.info("Emplois du temps de 3 et 4 aep: ")
st.table(example)
st.session_state["emplois"]=example