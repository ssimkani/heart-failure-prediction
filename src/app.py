import streamlit as st
import pandas as pd
import numpy as np
import joblib
import json

# Streamlit UI
def main():

    # Set page config
    st.set_page_config(
        page_title="Heart Disease Risk Predictor",
        page_icon="❤️",
        layout="centered",
        initial_sidebar_state="collapsed",
    )

    # Load the trained model
    model = joblib.load("models/rf_model.pkl")

    # load the encoded df
    with open("data/processed/encodings.json", "r") as enc_file:
        df_encodings = json.load(enc_file)

    # Load Styles
    with open("style/style.css", "r") as css_file:
        css = css_file.read()

    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

    st.title("Heart Disease Risk Predictor")
    st.write("Predict the risk of heart disease based on various health metrics.")

    # Age
    age = st.slider("Age", 0, 120, 30)

    sex = st.selectbox("Sex", ["Female", "Male"], placeholder="Select Sex", index=None)

    # Chest Pain Type
    chest_pain_type = st.selectbox(
        "Chest Pain Type",
        ["Atypical Angina", "Non-Anginal Pain", "Asymptomatic", "Typical Angina"],
        placeholder="Select Chest Pain Type",
        index=None,
    )

    # Resting Blood Pressure
    resting_blood_pressure = st.slider("Resting Blood Pressure (mmHG)", 0, 200, 120)

    # Serum Cholesterol
    serum_cholesterol = st.slider("Serum Cholesterol (mg/dl)", 0, 600, 200)

    # Maximum Heart Rate
    max_heart_rate = st.slider("Maximum Heart Rate", 0, 250, 150)

    # Exercise Induced Angina
    exercise_induced_angina = st.selectbox(
        "Exercise Induced Angina",
        ["Yes", "No"],
        placeholder="Exercise Induced Angina?",
        index=None,
    )

    # Oldpeak
    oldpeak = st.slider("Oldpeak", 0.0, 10.0, 2.0)

    # ST Slope
    st_slope = st.selectbox(
        "ST Slope",
        ["Up", "Flat", "Down"],
        placeholder="Select ST Slope",
        index=None,
    )

    # Make sure all fields are filled
    all_fields_filled = (
    sex is not None and
    chest_pain_type is not None and
    exercise_induced_angina is not None and
    st_slope is not None
    )

    if all_fields_filled:
        if st.button("Predict Heart Disease Risk"):
            # Make prediction
            pass

if __name__ == "__main__":
    main()


def encode(decoded_input, df_encodings):
    """
    Encode the input data using the provided encodings.
    """
    encoded_data = {}
    for column, encoding in df_encodings.items():
        if column in input_data:
            encoded_data[column] = encoding.get(input_data[column], input_data[column])
    return encoded_data
