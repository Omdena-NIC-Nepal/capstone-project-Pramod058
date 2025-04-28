import streamlit as st 

def show():
    st.header("Overview")

    option = st.selectbox(
        "Select a data category to explore:",
        ["Weather and Climate", "Environmental-Glacier", "Socio-Economic"], index = 1
    )


    # Store in session state so analysis tab can use it
    st.session_state["selected_type"] = option


    if option == "Weather and Climate":
        from tabs.overviewPage_sections import weather_and_climate_overview
        weather_and_climate_overview.show()

    elif option == "Environmental-Glacier":
        from tabs.overviewPage_sections import environmental_overview
        environmental_overview.show()

    elif option == "Socio-Economic":
        from tabs.overviewPage_sections import socioeconomic_overview   
        socioeconomic_overview.show()

