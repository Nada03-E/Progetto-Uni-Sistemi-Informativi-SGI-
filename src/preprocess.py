import os
import sys
import pandas as pd
import nltk
import string
import emoji
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from urllib.parse import urlparse
from wordcloud import STOPWORDS
#import contractions
import sqlite3
sys.path.append(os.path.abspath('..'))  # Adds the parent directory to sys.path
from src import config

def preprocess_data():
    #Connessione al Database

    conn = sqlite3.connect(config.DATABASE_PATH)

    # Lettura della tabella inserita
    df = pd.read_sql_query(f"SELECT * FROM {config.RAW_TABLE}", conn)

    #Applicazione dei Preprocessing
    df.to_sql(config.PROCESSED_TABLE, conn, if_exists='replace', index=False)

    # Modifica del dataset
    conn.commit()
    conn.close()

    print(f'I dati sono puliti e conservati nella {config.PROCESSED_TABLE} tabella.')