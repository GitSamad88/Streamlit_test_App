import streamlit as st


emplois=st.session_state["emplois"]

st.write("emplois description",emplois.describe())