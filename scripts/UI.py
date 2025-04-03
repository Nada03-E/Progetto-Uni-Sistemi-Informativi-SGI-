import os
import sys
import pickle
import streamlit as st
import pandas as pd

# Aggiungiamo la directory principale al path
sys.path.append(os.path.abspath("..")) #streamlit run UI.py   python -m streamlit run UI.py
from src import config

# Carica il modello
model_path = os.path.join(config.MODELS_PATH, "random_forest.pkl")
with open(model_path, 'rb') as file:
    model = pickle.load(file)

# Titolo dell'app
st.title("Previsione Prezzi Immobiliari")
st.markdown("Inserisci la **latitudine** e la **longitudine** per stimare il prezzo per unità di superficie.")

# Input utente
latitude = st.number_input("Latitudine", value=24.95, format="%.5f")
longitude = st.number_input("Longitudine", value=121.54, format="%.5f")

# Bottone per la previsione
if st.button("Prevedi Prezzo"):
    input_df = pd.DataFrame({"latitude": [latitude], "longitude": [longitude]})
    prediction = model.predict(input_df)[0]
    st.success(f"Prezzo stimato per unità di superficie: {prediction:.2f}")
