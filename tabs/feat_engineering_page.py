import streamlit as st



def show():
    st.header("Feature Engineering")
    selected_type = st.session_state.get("selected_type", "Weather and Climate")
    
    st.info(f"🔍 Feature Engineering for: **{selected_type}** data")
    
    if selected_type == "Weather and Climate":
        from pages.weather_and_climate import weather_and_climate_feat_eng
        weather_and_climate_feat_eng.show()

    elif selected_type == "Environmental-Glacier":
        from pages.environmental_glacier import environmental_feat_eng
        environmental_feat_eng.show()

    elif selected_type == "Socio-Economic":
        from pages.socioeconomic import socioeconomic_feat_eng
        socioeconomic_feat_eng.show()
