import streamlit as st # type: ignore
from tabs import aboutpage, feat_eng_page, overviewPage, expanalysisPage, modeltrainPage, predictionPage, NLP

# Page config - wide layout, no sidebar
st.set_page_config(page_title="Nepal", layout="wide")

# Title outside sidebar
st.header("🌍 Climate Change Impact Dashboard - Nepal - Omdena batch II Capstone project")

# Sidebar tabs (using st.selectbox without background colors)
selected = st.sidebar.radio(
    "",  # Label for the radio buttons
    ["About the project", "Overview", "Exploratory Analysis", "Feature Engineering", "Model train and Evaluation", "Prediction", "NLP"],  # Tab options
    index=1,  # Setting the default tab to "Overview"
)

# Show the content based on the selected tab
if selected == "About the project":
    aboutpage.show()

elif selected == "Overview":
    overviewPage.show()

elif selected == "Exploratory Analysis":
    expanalysisPage.show()

elif selected == "Feature Engineering":
    feat_eng_page.show()

elif selected == "Model train and Evaluation":
    modeltrainPage.show()

elif selected == "Prediction":
    predictionPage.show()

elif selected == "NLP":
    NLP.show()