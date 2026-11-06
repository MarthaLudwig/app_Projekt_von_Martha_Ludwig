import streamlit as st
from zahlen import*

class Script_Ggt:

    def scriptggt(self):

        # Eingabefelder
        a = st.number_input("Zahl A", value = 12, step = 1)
        b = st.number_input("Zahl B", value = 18, step = 1)

        if st.button("Berechnen ggt"):

            ergebnis = ggt(a, b)
            st.success(f"Größter gemeinsamer Teiler (GGT): {ergebnis}")