# App von Martha Ludwig

from zahlen import*
import streamlit as st

st.title("App von Martha Ludwig")

# Eingabefelder
a = st.number_input("Zahl A", value = 12, step = 1)
b = st.number_input("Zahl B", value = 18, step = 1)

if st.button("Berechnen ggT"):

    ergebnis = ggt(a, b)

    st.success(f"Größter gemeinsamer Teiler (GGT): {ergebnis}")

if st.button("Berechnen kgV"):

    ergebnis = kgv(a, b)

    st.success(f"Kleinstes gemeinsames Vielfache (KGV): {ergebnis}")