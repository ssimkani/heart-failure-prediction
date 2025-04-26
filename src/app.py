import streamlit as st
import pandas as pd
import numpy as np
import joblib
import json

# Streamlit UI
def main():

    # Set page config
    st.set_page_config(
        page_title="Heart Disease Risk Calculator",
        page_icon="❤️",
        layout="centered",
        initial_sidebar_state="collapsed",
    )

    # Load the trained model
    model = joblib.load("../models/rf_model.pkl")

    # load the encoded df
    with open("../data/processed/encodings.json", "r") as enc_file:
        df_encodings = json.load(enc_file)

    # Load Styles
    with open("../style/style.css", "r") as css_file:
        css = css_file.read()

    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
