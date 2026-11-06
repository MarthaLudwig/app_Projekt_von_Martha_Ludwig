import streamlit as st
from zahlen import*

class Script_KgV:

    def scriptkgv(self):

        # Eingabefelder
        a = st.number_input("Zahl A", value = 12, step = 1)
        b = st.number_input("Zahl B", value = 18, step = 1)

        if st.button("Berechnen kgv"):

            ergebnis = kgv(a, b)
            st.success(f"Kleinstes gemeinsames Vielfache (KGV): {ergebnis}")