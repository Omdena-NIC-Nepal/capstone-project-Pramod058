import streamlit as st


def show():
    st.header("Prediction Page")

    selected_type = st.session_state.get("selected_type", "weather and Climate")

    st.info(f"🔍 Prediction for: **{selected_type}** data")
    
   
    if selected_type == "Weather and Climate":
        from tabs.prediction_sections import weather_and_climate_prediction
        weather_and_climate_prediction.show()

    elif selected_type == "Environmental-Glacier":
        from tabs.prediction_sections import environmental_prediction
        environmental_prediction.show()

    elif selected_type == "Socio-Economic":
        from tabs.prediction_sections import socioeconomic_prediction
        socioeconomic_prediction.show()