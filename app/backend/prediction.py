import joblib


RF_MODEL_PATH = "models/random_forest.pkl"
GB_MODEL_PATH = "models/gradient_boosting.pkl"


def load_models():
    rf_model = joblib.load(RF_MODEL_PATH)
    gb_model = joblib.load(GB_MODEL_PATH)

    return rf_model, gb_model


def predict_prices(user_features):
    rf_model, gb_model = load_models()

    rf_prediction = rf_model.predict(user_features)[0]
    gb_prediction = gb_model.predict(user_features)[0]

    return rf_prediction, gb_prediction