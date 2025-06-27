import streamlit as st 

# Page config - wide layout, no sidebar
st.set_page_config(page_title="Nepal", layout="wide")

# Title outside sidebar
st.header("🌍 Climate Change Impact Dashboard - Nepal - Omdena batch II Capstone project")

# Sidebar tabs (using st.selectbox without background colors)
selected = st.sidebar.radio(
    "",  # Label for the radio buttons
    ["About the project", "Overview", "Exploratory Analysis", "Feature Engineering", "Model train and Evaluation", "Prediction", "NLP"],  # Tab options
    index=1# Setting the default tab to "Overview"
)


# Show the content based on the selected tab
if selected == "About the project":
    from tabs import about_page
    about_page.show()

elif selected == "Overview":
    from tabs import overview_page
    overview_page.show()

elif selected == "Exploratory Analysis":
    from tabs import eda_page
    eda_page.show()

elif selected == "Feature Engineering":
    from tabs import feat_engineering_page
    feat_engineering_page.show()

elif selected == "Model train and Evaluation":
    from tabs import modeltrain_page
    modeltrain_page.show()

elif selected == "Prediction":
    from tabs import prediction_page
    prediction_page.show()

elif selected == "NLP":
    from tabs import nlp_page
    nlp_page.show()


# Footer 

if selected not in ["About the project"]:  
    st.markdown("---")
    st.markdown(
        """
        <div style="text-align: center;">
            <p>Version 1.0 | Developed by <b>Pramod</b></p>
            <p>
                <a href="https://www.linkedin.com/in/your-linkedin-profile" target="_blank" style="text-decoration: none;">LinkedIn</a> |
                <a href="https://github.com/your-github-profile" target="_blank" style="text-decoration: none;">GitHub</a>
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )