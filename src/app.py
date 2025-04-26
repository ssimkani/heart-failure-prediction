import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Streamlit UI
def main():

    # Set page config
    st.set_page_config(
        page_title="Heart Disease Risk Calculator",
        page_icon="❤️",
        layout="centered",
        initial_sidebar_state="collapsed",
    )
