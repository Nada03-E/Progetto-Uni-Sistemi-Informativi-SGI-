import os
import sys
import pickle
import streamlit as st
import pandas as pd
from streamlit_folium import st_folium
import folium

sys.path.append(os.path.abspath("..")) 
from src import config

#python -m streamlit run UI.py

# carichiamo il modello scelto
model_path = os.path.join(config.MODELS_PATH, "random_forest.pkl")
with open(model_path, 'rb') as file:
    model = pickle.load(file)


st.title(" Previsione Prezzi Immobiliari")
st.markdown(""" 
inserisci manualmente la logitudine e latitudine o premi un punto sulla mappa.
""")

#inserimento manuale:
col1, col2 = st.columns(2)

with col1:
    latitude = st.number_input("Latitudine", value=24.95, format="%.5f")
with col2:
    longitude = st.number_input("Longitudine", value=121.54, format="%.5f")

# Maoppa cliccabile:

st.markdown("### Oppure clicca su una posizione nella mappa:")
map_center = [latitude, longitude]
m = folium.Map(location=map_center, zoom_start=15)
m.add_child(folium.LatLngPopup())
output = st_folium(m, width=700, height=400)

#se l'utente preme sulla mappa la latyitudine e lonmgitudine vengono aggiornate automaticamente.
if output and output.get("last_clicked"):
    latitude = output["last_clicked"]["lat"]
    longitude = output["last_clicked"]["lng"]
    st.success(f"Coordinate selezionate: {latitude:.5f}, {longitude:.5f}")

#pulsante di invuio richiesta
if st.button("Prevedi Prezzo"):
    input_df = pd.DataFrame({"latitude": [latitude], "longitude": [longitude]})
    prediction = model.predict(input_df)[0]
    st.markdown(f"### Prezzo stimato: **{prediction:.2f}** per unità di superficie")
