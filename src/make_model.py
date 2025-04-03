import sqlite3
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import os
import sys
import pickle

sys.path.append(os.path.abspath('..'))
from src import config
import logging


def load_data():
    conn = sqlite3.connect(config.DATABASE_PATH)
    query = f"SELECT `X5 latitude` as latitude, `X6 longitude` as longitude, `Y house price of unit area` as price FROM {config.PROCESSED_TABLE}"
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df


def train_model():
    logging.info("Loading data for training...")
    df = load_data()
    X = df[["latitude", "longitude"]]
    y = df["price"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestRegressor(random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    logging.info(f"Model evaluation - MSE: {mse}, R2: {r2}")

    # Save model
    os.makedirs(config.MODELS_PATH, exist_ok=True)
    with open(os.path.join(config.MODELS_PATH, "random_forest.pkl"), "wb") as f:
        pickle.dump(model, f)

    # Save predictions (optional)
    test_df = X_test.copy()
    test_df["actual"] = y_test.values
    test_df["predicted"] = y_pred

    conn = sqlite3.connect(config.DATABASE_PATH)
    test_df.to_sql(config.PREDICTIONS_TABLE, conn, if_exists="replace", index=False)
    conn.commit()
    conn.close()

    logging.info("Model training and saving completed.")

#finito si