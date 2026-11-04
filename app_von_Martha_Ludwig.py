# App von Martha Ludwig

import streamlit as st

st.title("App von Martha Ludwig")

# Eingabefelder
a = st.number_input("Zahl A", value = 12, step = 1)
b = st.number_input("Zahl B", value = 18, step = 1)

if st.button("Berechnen"):

    ergebnis = a + b

    st.success(f"Summe: {ergebnis}")