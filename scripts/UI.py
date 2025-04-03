import os
import sys
sys.path.append(os.path.abspath('..'))
from src import config  #streamlit run UI.py   python -m streamlit run UI.py
import streamlit as st
import pickle
import streamlit as st
from streamlit_option_menu import option_menu
print(f"Looking for model at: {config.MODELS_PATH}random_forest.pkl")

#load the model and vectorizer
with open(f"{config.MODELS_PATH}random_forest.pkl", 'rb') as file:
    model1 = pickle.load(file)
with open(f"{config.MODELS_PATH}logistic_regression.pkl", 'rb') as file:
    model2 = pickle.load(file)
#with open(f"{config.MODELS_PATH}naive_bayes.pkl", 'rb') as file:
 #   model3 = pickle.load(file)
with open(f"{config.MODELS_PATH}vectorizer.pkl", 'rb') as file:
    vectorizer = pickle.load(file)

st.title("Sentiment Analysis App")
user_input = st.text_area("Enter a tweet","")

with st.sidebar:
    selected = option_menu("Main Menu", ["random_forest", 'logistic_regression', 'naive_bayes'],default_index=1)
    selected

if st.button("Predict"):
    if user_input.strip() == "":
        st.write("Please enter a tweet.")
    else:
        #trasform imput and predict
        X=vectorizer.transform([user_input])
        if(selected == 'random_forest'):
            model = model1
        elif(selected == 'logistic_regression'):
            model = model2  
       # elif(selected == 'naive_bayes'):
         #   model = model3
        prediction = model.predict(X)[0]
        if prediction=='positive':
            st.success(f"Predicted class:{prediction}")
        elif prediction== 'negative':
            st.warning(f"Predicted class:{prediction}")
