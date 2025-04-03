import sqlite3
import pandas as pd
import sys
import os

sys.path.append(os.path.abspath('..'))  # Adds the parent directory to sys.path
from src import config

import logging
# Set up logging

def load_data():
    logging.info('Opening Excel Files...')
    df = pd.read_excel(os.path.join(config.RAW_DATA_PATH, 'Real estate valuation data set.xlsx'),
    index_col=0  # Ignoriamo la prima colonna trattandola come indice
    )


    df = df[['transaction_date', 'house_age', 'distance_to_the_nearest_MRT_station', 'number_of_convenience_stores', 'latitude', 'longitude', 'price_per_unit_area']]
    df.columns = ['transaction_date', 'house_age', 'distance_to_the_nearest_MRT_station', 'number_of_convenience_stores', 'latitude', 'longitude', 'price_per_unit_area']

    df.reset_index(drop=True, inplace=True)
    

    # Create a connection to the SQLite database (or create if it doesn't exist)
    conn = sqlite3.connect(config.DATABASE_PATH)

    # Write the DataFrame to a table (replace 'my_table' with your desired table name)
    df.to_sql(config.RAW_TABLE, conn, if_exists='replace', index=False)

    # Commit and close the connection
    conn.commit()
    conn.close()

    logging.info(f"Data successfully written to {config.RAW_TABLE} table.")
