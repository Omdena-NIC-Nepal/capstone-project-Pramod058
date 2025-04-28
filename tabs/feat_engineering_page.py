import streamlit as st



def show():
    st.header("Feature Engineering")
    selected_type = st.session_state.get("selected_type", "Weather and Climate")
    
    st.info(f"🔍 Feature Engineering for: **{selected_type}** data")
    
    if selected_type == "Weather and Climate":
        from tabs.feat_eng_sections import weather_and_climate_feat_eng
        weather_and_climate_feat_eng.show()

    elif selected_type == "Environmental-Glacier":
        from tabs.feat_eng_sections import environmental_feat_eng
        environmental_feat_eng.show()

    elif selected_type == "Socio-Economic":
        from tabs.feat_eng_sections import socioeconomic_feat_eng
        socioeconomic_feat_eng.show()
