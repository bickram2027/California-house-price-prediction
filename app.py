import streamlit as st
import pandas as pd
import joblib


# Load the trained model
model_data = joblib.load("random_forest_model.pkl")

model = model_data["model"]
preprocessor = model_data["preprocessor"]


# Page title
st.title("California House Price Prediction")

st.write("Enter the house details below to predict the median house value.")


# Input fields

longitude = st.number_input(
    "Longitude",
    value=-122.23
)

latitude = st.number_input(
    "Latitude",
    value=37.88
)

housing_median_age = st.number_input(
    "Housing Median Age",
    value=30.0
)

total_rooms = st.number_input(
    "Total Rooms",
    value=2000.0
)

total_bedrooms = st.number_input(
    "Total Bedrooms",
    value=400.0
)

population = st.number_input(
    "Population",
    value=1000.0
)

households = st.number_input(
    "Households",
    value=300.0
)

median_income = st.number_input(
    "Median Income",
    value=4.0
)

ocean_proximity = st.selectbox(
    "Ocean Proximity",
    [
        "NEAR BAY",
        "<1H OCEAN",
        "INLAND",
        "NEAR OCEAN",
        "ISLAND"
    ]
)


# Prediction button

if st.button("Predict House Price"):

    input_data = pd.DataFrame({
        "longitude": [longitude],
        "latitude": [latitude],
        "housing_median_age": [housing_median_age],
        "total_rooms": [total_rooms],
        "total_bedrooms": [total_bedrooms],
        "population": [population],
        "households": [households],
        "median_income": [median_income],
        "ocean_proximity": [ocean_proximity]
    })

    # Apply the same preprocessing used during training
    input_data = preprocessor.transform(input_data)

    # Make prediction
    prediction = model.predict(input_data)

    # Display result
    st.success(
        f"Predicted House Price: ${prediction[0]:,.2f}"
    )