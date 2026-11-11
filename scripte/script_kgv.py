import streamlit as st
from zahlen import*

class Script_Kgv:

    def scriptkgv(self):

        # Eingabefelder
        st.subheader("Kleinstes gemeinsames Vielfaches (KGV)")
        a_kgv = st.number_input("Zahl A", value = 12, step = 1, key = "a_kgv")
        b_kgv = st.number_input("Zahl B", value = 18, step = 1, key = "b_kgv")

        if st.button("Berechnen kgv", key = "btn_kgv"):

            ergebnis = kgv(a_kgv, b_kgv)
            st.success(f"KGV von {a_kgv} und {b_kgv} ist: {ergebnis}")