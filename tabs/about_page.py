import streamlit as st

def show():
    st.title("About the Project")

    st.markdown("""
                
    Project tutorial [Drive Link](<https://drive.google.com/file/d/1WDvzwQrYD7CzcrKMeoPlY88ihD5a9Piw/view?usp=sharing>) 
                
    Welcome to the **Climate Change Impact Project in Nepal**! 🌍

    This project aims to analyze and predict the impact of climate change in Nepal using various machine learning techniques. You will be guided through different stages where you can explore, train, and predict outcomes based on climate data. Here is a step-by-step guide to navigating through the project:

    **1. Overview Page** 📊
    - The first page you will encounter is the "Overview" page.
    - In this section, you will be able to choose from a dropdown to select the dataset you would like to explore.
    - Once you've made your selection, the raw sample data of your choice will be displayed for you to examine.

    **2. Exploratory Data Analysis (EDA)** 🔍
    - The next page is dedicated to **Exploratory Data Analysis (EDA)**.
    - You’ll explore various data exploration techniques and visualizations.
    - At this stage, you'll actively participate by exploring the data and visualizing it with different methods. The insights you gain here will lay the foundation for the feature engineering process.

    **3. Feature Engineering** 🛠️
    - In the "Feature Engineering" section, we will focus on capturing and engineering important features from the raw data.
    - You will get the chance to transform the data into meaningful features that will help improve the model’s performance.

    **4. Model Training and Evaluation** 📉
    - On this page, you will find multiple machine learning models available for training.
    - You will select a model of your choice, train it using the prepared data, and evaluate its performance.
    - Once you train the model, you will receive evaluation metrics to assess its accuracy and effectiveness.

    **5. Prediction** 🔮
    - In this stage, you will see predictions based on the model you trained.
    - The system will predict the outcomes based on the climate data, and you’ll be able to visualize the results.
                
    **6. Natural Language Processing (NLP) and Sentiment Analysis** 🧠💬
    - The final page in this project is dedicated to **Natural Language Processing (NLP)**.
    - Here, you will be able to enter a text in the provided textbox and analyze the **sentiment** of the text.
    - The system will analyze the sentiment and categorize it into positive, negative, or neutral based on the content of your input.


    ## How to Navigate:
    - Use the **tabs** at the right side of the webapp to move between different sections of the project.
    - Start with the "Overview" page and move through each page step by step to get the most out of the experience.

        ---
    
    ### Regards,
    **Pramod Aryal**  
    Connect with me on [LinkedIn](<https://www.linkedin.com/in/pramod58/>) | [GitHub](<https://github.com/Pramod058>)  
    """)

