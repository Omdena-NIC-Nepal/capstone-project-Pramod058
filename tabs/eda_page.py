import streamlit as st

def show():
    st.header("Exploratory Data Analysis")

    selected_type = st.session_state.get("selected_type", "weather and Climate")

    st.info(f"🔍 Exploratory analysis for: **{selected_type}** data")

    if selected_type == "Weather and Climate":
        from tabs.exanalysis_sections import weather_and_climate_eda
        weather_and_climate_eda.show()

    elif selected_type == "Environmental-Glacier":
        from tabs.exanalysis_sections import environmental_eda
        environmental_eda.show()

    elif selected_type == "Socio-Economic":
        from tabs.exanalysis_sections import socioeconomic_eda
        socioeconomic_eda.show()
