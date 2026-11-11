import streamlit as st
from zahlen import*

class Script_Ggt:

    def scriptggt(self):

        # Eingabefelder
        st.subheader("Größter gemeinsamer Teiler (GGT)")
        a_ggt = st.number_input("Zahl A", value = 12, step = 1, key = "input_a_ggt")
        b_ggt = st.number_input("Zahl B", value = 18, step = 1, key = "input_b_ggt")

        if st.button("Berechnen ggt", key = "btn_ggt"):

            ergebnis = ggt(a_ggt, b_ggt)
            st.success(f"GGT von {a_ggt} und {b_ggt} ist: {ergebnis}")