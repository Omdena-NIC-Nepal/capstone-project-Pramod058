# 🌍 Climate Change Impact Dashboard - Nepal  
**Omdena Batch II Capstone Project**  
*By Pramod Aryal*  

---

## 🚀 Getting Started

### Prerequisites  
- Python 
- pip package manager  



## Steps to View and Run the Code

### 1. Clone the Repository
```
git clone https://github.com/Omdena-NIC-Nepal/capstone-project-Pramod058.git

```

### 2. Install Dependencies
Ensure you have Python installed, then run:
```
pip install -r requirements.txt
```

### 3. Run the Dashboard
```
streamlit run app.py
```

## 📌 Project Overview
This dashboard analyzes climate change impacts in Nepal using:

####             -Machine Learning for climate predictions

####             -NLP for sentiment analysis

####             -Interactive visualizations of district-wise climate data

🌟 Features	Description
- 📊 Overview	Select and preview raw climate/glacier datasets
- 🔍 EDA	Explore data distributions and correlations
- 🛠️ Feature Engineering	Transform raw data into model-ready features
- 📉 Model Training	Train and evaluate regression/classification models
- 🔮 Prediction	Generate climate impact forecasts
- 🧠 NLP	Analyze sentiment of user-provided text



## Folder Structure


# 📁 Project Folder Structure

```plaintext
CAPSTONE-PROJECT/
├── .github/
├── data/
│   ├── climate_data_nepal_district_wise.csv
│   └── nepal_glacier_data.csv
├── pages/
│   ├── environmental_glacier/
│   │   ├── __pycache__/
│   │   ├── environmental_eda.py
│   │   ├── environmental_feat_eng.py
│   │   ├── environmental_modeltrain.py
│   │   ├── environmental_overview.py
│   │   └── environmental_prediction.py
│   └── weather_and_climate/
│       ├── __pycache__/
│       ├── weather_and_climate_eda.py
│       ├── weather_and_climate_feat_eng.py
│       ├── weather_and_climate_modeltrain.py
│       └── weather_and_climate_overview.py
├── scripts/
│   ├── __pycache__/
│   ├── data_utils.py
│   ├── model_prediction.py
│   ├── model_train.py
│   └── visualization.py
├── tabs/
│   ├── __pycache__/
│   ├── about_page.py
│   ├── eda_page.py
│   ├── feat_engineering_page.py
│   ├── modeltrain_page.py
│   ├── NLP.py
│   ├── overview_page.py
│   └── prediction_page.py
├── app.py
├── eda.ipynb
├── README.md
└── requirements.txt
```


## 🖥️ Usage Guide
Navigation
Use the right-side tabs to switch sections.

### Follow this workflow:

```
Overview → EDA → Feature Engineering → Model Training → Prediction → NLP

```


## Author
- [Pramod Aryal](https://www.linkedin.com/in/pramod58/)

---
For any questions or improvements, please reach out or open an issue in the repository.
