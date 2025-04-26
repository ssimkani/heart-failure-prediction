import streamlit as st
import pandas as pd
import numpy as np
import joblib
import json
import utils.predictions as pred
import utils.risk_level as rl

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
    sex = df_encodings["Sex"].get(sex)

    # Chest Pain Type
    chest_pain_type = st.selectbox(
        "Chest Pain Type",
        ["Atypical Angina", "Non-Anginal Pain", "Asymptomatic", "Typical Angina"],
        placeholder="Select Chest Pain Type",
        index=None,
    )
    chest_pain_type = df_encodings["ChestPainType"].get(chest_pain_type)

    # Resting Blood Pressure
    resting_blood_pressure = st.slider("Resting Blood Pressure (mmHG)", 0, 200, 120)

    # Serum Cholesterol
    serum_cholesterol = st.slider("Serum Cholesterol (mg/dl)", 0, 600, 200)

    # Maximum Heart Rate
    max_heart_rate = st.slider("Maximum Heart Rate", 0, 250, 150)

    # Exercise Induced Angina
    exercise_induced_angina = st.selectbox(
        "Exercise Induced Angina",
        ["No", "Yes"],
        placeholder="Exercise Induced Angina?",
        index=None,
    )
    exercise_induced_angina = df_encodings["ExerciseAngina"].get(exercise_induced_angina)

    # Oldpeak
    oldpeak = st.slider("Oldpeak (mm)", 0.0, 10.0, 2.0)

    # ST Slope
    st_slope = st.selectbox(
        "ST Slope",
        ["Up", "Flat", "Down"],
        placeholder="Select ST Slope",
        index=None,
    )
    st_slope = df_encodings["ST_Slope"].get(st_slope)

    # Make sure all fields are filled
    all_fields_filled = (
    sex is not None and
    chest_pain_type is not None and
    exercise_induced_angina is not None and
    st_slope is not None
    )

    if all_fields_filled:
        if st.button("Predict Heart Disease Risk"):
            # Create a DataFrame for the input data
            input_data = pd.DataFrame({
                "Age": [age],
                "Sex": [sex],
                "ChestPainType": [chest_pain_type],
                "RestingBP": [resting_blood_pressure],
                "Cholesterol": [serum_cholesterol],
                "MaxHR": [max_heart_rate],
                "ExerciseAngina": [exercise_induced_angina],
                "Oldpeak": [oldpeak],
                "ST_Slope": [st_slope]
            })

            # Make prediction
            prediction = pred.predict(model, input_data)
            risk_level = rl.risk_level(prediction)
            st.success(f"Predicted Risk: {(prediction * 100):.2f}%")
            st.success(risk_level)

if __name__ == "__main__":
    main()
