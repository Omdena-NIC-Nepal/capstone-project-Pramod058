import streamlit as st

def show():
    st.header("Overview")

    # Check if the 'selected_type' is already in session state
    if "selected_type" not in st.session_state:
        st.session_state["selected_type"] = "Weather and Climate"  # Default value

    # dropdown selectbox with the current session state value
    option = st.selectbox(
        "Select a data category to explore:",
        ["Weather and Climate", "Environmental-Glacier"],
        index=["Weather and Climate", "Environmental-Glacier",].index(st.session_state["selected_type"])
    )

    # Update session state with the selected option
    if st.session_state["selected_type"] != option:
        st.session_state["selected_type"] = option

    # Dynamic content based on selected option
    if option == "Weather and Climate":
        from pages.weather_and_climate import weather_and_climate_overview
        weather_and_climate_overview.show()

    elif option == "Environmental-Glacier":
        from pages.environmental_glacier import environmental_overview
        environmental_overview.show()

