# App von Martha Ludwig

from scripte import*
import streamlit as st

st.title("Mathe-App von Martha Ludwig")
st.write("Wähle im Menü aus, welches Programm du starten möchtest:")

# Auswahlmenü auf der Startseite (oder st.sidebar für die Seitenleiste)
auswahl = st.selectbox("Programm auswählen", ["Startseite", "GGT berechnen", "KGV berechnen"])

if auswahl == "Startseite":

    st.info("Willkommen! Bitte wähle oben im Menü eine Funktion aus.")

elif auswahl == "GGT berechnen":

    script_ggt()

elif auswahl == "KGV berechnen":

    script_kgv()