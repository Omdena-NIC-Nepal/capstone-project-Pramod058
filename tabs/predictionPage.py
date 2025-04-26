import streamlit as st
from tabs.prediction_sections import weather_and_climatePrediction, environmentalPrediction, socioeconomicPrediction


def show():
    st.header("Prediction Page")

    selected_type = st.session_state.get("selected_type", "weather and Climate")

    st.info(f"🔍 Prediction for: **{selected_type}** data")
    
   
    if selected_type == "Weather and Climate":
        weather_and_climatePrediction.show()
    elif selected_type == "Environmental":
        environmentalPrediction.show()
    elif selected_type == "Socio-Economic":
        socioeconomicPrediction.show()