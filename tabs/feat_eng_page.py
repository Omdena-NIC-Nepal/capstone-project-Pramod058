import streamlit as st
from tabs.featEng_sections import   weather_and_climatefeateng,  environmentalfeateng, socioeconomicfeateng



def show():
    st.header("Feature Engineering")
    selected_type = st.session_state.get("selected_type", "Weather and Climate")
    
    st.info(f"🔍 Feature Engineering for: **{selected_type}** data")
    
    if selected_type == "Weather and Climate":
        weather_and_climatefeateng.show()
    elif selected_type == "Environmental":
        environmentalfeateng.show()
    elif selected_type == "Socio-Economic":
        socioeconomicfeateng.show()
