import streamlit as st
from tabs.exanalysis_sections import environmentalEda, socioeconomicEda, weather_and_climateEda

def show():
    st.header("Exploratory Data Analysis")

    selected_type = st.session_state.get("selected_type", "weather and Climate")

    st.info(f"🔍 Exploratory analysis for: **{selected_type}** data")

    if selected_type == "Weather and Climate":
        weather_and_climateEda.show()
    elif selected_type == "Environmental":
        environmentalEda.show()
    elif selected_type == "Socio-Economic":
        socioeconomicEda.show()
