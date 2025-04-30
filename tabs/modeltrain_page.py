import streamlit as st

def show():
    st.header("Model training and Evaluation")
    selected_type = st.session_state.get("selected_type", "weather and Climate")
    
    st.info(f"🔍 Model training and Evaluation for: **{selected_type}** data")
    
    if selected_type == "Weather and Climate":
        from pages.weather_and_climate import weather_and_climate_modeltrain
        weather_and_climate_modeltrain.show()

    elif selected_type == "Environmental-Glacier":
        from pages.environmental_glacier import environmental_modeltrain
        environmental_modeltrain.show()
        
    elif selected_type == "Socio-Economic":
        from pages.socioeconomic import socioeconomic_modeltrain
        socioeconomic_modeltrain.show()
