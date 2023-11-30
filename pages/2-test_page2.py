import streamlit as st


emplois1=st.session_state["emplois1"]
emplois2=st.session_state["emplois2"]


col1, col2 = st.columns(2)
col1.table(emplois1.describe())

col2.table(emplois2.describe())
