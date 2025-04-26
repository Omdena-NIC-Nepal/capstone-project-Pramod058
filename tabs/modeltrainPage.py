import streamlit as st
from tabs.modeltrain_sections import weather_and_climateModeltrain,  environmentalModeltrain, socioeconomicModeltrain

def show():
    st.header("Model training and Evaluation")
    selected_type = st.session_state.get("selected_type", "weather and Climate")
    
    st.info(f"🔍 Model training and Evaluation for: **{selected_type}** data")
    
    if selected_type == "Weather and Climate":
        weather_and_climateModeltrain.show()
    elif selected_type == "Environmental":
        environmentalModeltrain.show()
    elif selected_type == "Socio-Economic":
        socioeconomicModeltrain.show()
