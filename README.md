# Vehicle Price Predictor

A machine learning web application that predicts the estimated price of a used vehicle based on its specifications and usage details.

The application compares two regression models:

- Random Forest
- Gradient Boosting

## Live Demo

Live Application: <streamlit-app-url>

## Project Notebook

The complete data analysis, preprocessing, feature engineering, model training, and evaluation process is available in the Google Colab notebook:

[View the Google Colab Notebook](<https://colab.research.google.com/drive/1N_3db8Uenbni0TK3QT_e53RYUIGEQWny?usp=sharing>)

## Features

- Used vehicle price prediction
- Random Forest and Gradient Boosting predictions
- Side-by-side model comparison
- Interactive prediction graph
- Model performance comparison
- Responsive Streamlit interface

## Input Features

The application uses the following vehicle attributes:

- Brand
- Model Year
- Transmission Type
- Engine Capacity
- Maximum Power
- Maximum Torque
- Mileage
- Kilometres Driven
- Kerb Weight
- Seller Type
- Car Segment

Additional features are engineered during preprocessing:

- Vehicle Age
- Age × Mileage
- Power-to-Weight Ratio

## Models

Two regression models were trained and evaluated:

- **Random Forest Regressor**
- **Gradient Boosting Regressor**

The models were trained using the processed vehicle dataset and the
feature engineering/preprocessing pipeline documented in the notebook.

The Gradient Boosting model is included directly in this repository:

`models/gradient_boosting.pkl`

The Random Forest model is hosted separately on Hugging Face because
the trained model file exceeds GitHub's 100 MB file-size limit:

[Random Forest Model](https://huggingface.co/Nastel123/vehicle-price-random-forest/tree/main)

The Streamlit application automatically retrieves the Random Forest
model when required.

## Model Evaluation

The models were evaluated using:

- R² Score
- Root Mean Squared Error (RMSE)
- Mean Absolute Error (MAE)

Based on the test-set evaluation, Gradient Boosting performed better than Random Forest.

| Metric | Gradient Boosting |
|---|---:|
| R² Score | 0.6586 |
| RMSE | ₹6,24,888 |
| MAE | ₹2,72,115 |

## Dataset

The original dataset used in this project was obtained from Kaggle:

[Used Cars Dataset (CarDekho) — Kaggle](https://www.kaggle.com/datasets/sukritchatterjee/used-cars-dataset-cardekho)

The dataset contains used-car listings from CarDekho, including vehicle
specifications, seller information, and listing prices.

The original data was cleaned and transformed as part of this project.
Feature selection and feature engineering were then performed before
training the machine learning models.

### Data Sources

- Original Dataset: [Kaggle – Used Cars Dataset (CarDekho)](https://www.kaggle.com/datasets/sukritchatterjee/used-cars-dataset-cardekho)
The dataset was cleaned and transformed as part of this project.
This included data cleaning, feature engineering, and preparation of
the final features used for model training.
