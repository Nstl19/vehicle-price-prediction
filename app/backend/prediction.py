import os
import joblib
import streamlit as st
from huggingface_hub import hf_hub_download


# MODEL PATHS
RF_MODEL_PATH = "models/random_forest.pkl"
GB_MODEL_PATH = "models/gradient_boosting.pkl"

HF_REPO_ID = "Nastel123/vehicle-price-random-forest"
HF_RF_FILENAME = "random_forest.pkl"


# MODEL LOADING
@st.cache_resource
def load_models():

    if os.path.exists(RF_MODEL_PATH):

        # Local development
        rf_model_path = RF_MODEL_PATH

    else:

        # Streamlit Cloud
        rf_model_path = hf_hub_download(
            repo_id=HF_REPO_ID,
            filename=HF_RF_FILENAME
        )

    rf_model = joblib.load(rf_model_path)

    gb_model = joblib.load(GB_MODEL_PATH)


    return rf_model, gb_model


# PREDICTION
def predict_prices(user_features):

    rf_model, gb_model = load_models()

    rf_prediction = rf_model.predict(user_features)[0]

    gb_prediction = gb_model.predict(user_features)[0]

    return rf_prediction, gb_prediction