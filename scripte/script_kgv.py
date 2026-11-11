import streamlit as st
from zahlen import*

class Script_Kgv:

    def scriptkgv(self):

        # Eingabefelder
        a = st.number_input("Zahl A", value = 12, step = 1, key = "a_kgv")
        b = st.number_input("Zahl B", value = 18, step = 1, key = "b_kgv")

        if st.button("Berechnen kgv"):

            ergebnis = kgv(a, b)
            st.success(f"Kleinstes gemeinsames Vielfaches (KGV): {ergebnis}")