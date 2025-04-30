import streamlit as st

def show():
    st.header("Exploratory Data Analysis")

    selected_type = st.session_state.get("selected_type", "weather and Climate")

    st.info(f"🔍 Exploratory analysis for: **{selected_type}** data")

    if selected_type == "Weather and Climate":
        from pages.weather_and_climate import weather_and_climate_eda
        weather_and_climate_eda.show()

    elif selected_type == "Environmental-Glacier":
        from pages.environmental_glacier import environmental_eda
        environmental_eda.show()

    elif selected_type == "Socio-Economic":
        from pages.socioeconomic import socioeconomic_eda
        socioeconomic_eda.show()
