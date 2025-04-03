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


    # Download necessary resources
    nltk.download('punkt')
    nltk.download('punkt_tab')
    nltk.download('stopwords')
    nltk.download('wordnet')

    # Connect to the database
    conn = sqlite3.connect(config.DATABASE_PATH)

    # Read a table into a Pandas DataFrame
    df = pd.read_sql_query(f"SELECT * FROM {config.RAW_TABLE}", conn)

    # Apply preprocessing

    df.to_sql(config.PROCESSED_TABLE, conn, if_exists='replace', index=False)

    # Commit and close the connection
    conn.commit()
    conn.close()

    print(f'I dati sono puliti e conservati nella {config.PROCESSED_TABLE} tabella.')