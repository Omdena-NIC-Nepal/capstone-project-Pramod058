import streamlit as st # type: ignore
from tabs.overviewPage_sections import environmentalOverview, socioeconomicOverview, weather_and_climateOverview

def show():
    st.header("Overview")

    option = st.selectbox(
        "Select a data category to explore:",
        ["Weather and Climate", "Environmental", "Socio-Economic"], index = 0
    )


    # Store in session state so analysis tab can use it
    st.session_state["selected_type"] = option


    if option == "Weather and Climate":
        weather_and_climateOverview.show()
    elif option == "Environmental":
        environmentalOverview.show()
    elif option == "Socio-Economic":
        socioeconomicOverview.show()

