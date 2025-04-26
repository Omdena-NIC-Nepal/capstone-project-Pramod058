import streamlit as st
from scripts.data_utils import load_data, remove_unwanted_columns, clean_data


def show():


    # Data preview
    st.subheader("Data Preview")

    weatherClimatedf = load_data("data/climate_data_nepal_district_wise_monthly_province_grouped.csv")

    weatherClimatedf = remove_unwanted_columns(weatherClimatedf, ["date", "province.1"])

    cleaned_weatherClimatedf = clean_data(weatherClimatedf)

    st.dataframe(cleaned_weatherClimatedf, height=200)

    st.divider()
    

    st.markdown("""
    The dataset you will be working with contains various climate-related features recorded across different districts and provinces of Nepal. The following columns represent key meteorological data, which will help you explore the impact of climate change in this region:

    1. **Date, Year, Month** 🗓️:  
       - These columns represent the temporal aspect of the data, allowing you to analyze trends over time. 
       - **Date** captures the specific day of measurement, while **Year** and **Month** provide more granular insights into long-term changes.

    2. **District, Province** 🏞️:  
       - This geographic data specifies the district and province in Nepal where the measurements were taken.
       - This information is useful for spatial analysis, helping you see how different areas are impacted by climate factors.

    3. **Latitude, Longitude** 🌍:  
       - These columns give the precise geographic location of the measurement points, enabling location-based analysis and visualizations.

    4. **Precipitation Total** 🌧️:  
       - The total amount of rainfall (in millimeters) recorded during a specific time period. This is a key indicator of weather patterns and changes in rainfall due to climate change.

    5. **Surface Pressure** 🌬️:  
       - The atmospheric pressure measured at the Earth's surface, which can be used to study weather systems and their impacts.

    6. **Specific Humidity at 2m** 💧:  
       - The amount of water vapor in the air at a height of 2 meters. It is an important measure for understanding moisture levels and their relationship to weather events.

    7. **Relative Humidity at 2m** 🌫️:  
       - The percentage of moisture in the air relative to the maximum possible at 2 meters above the ground. High humidity can have significant effects on health and the environment.

    8. **Air Temperature at 2m** 🌡️:  
       - The temperature of the air measured at 2 meters above the ground. This is one of the most crucial factors in determining climate patterns.

    9. **Wet Bulb Temperature at 2m** 🌡️💧:  
       - The temperature recorded when the air is cooled by the evaporation of water. It is a key indicator of heat stress and comfort levels.

    10. **Max and Min Temperature at 2m** 🔥❄️:  
        - These columns provide the highest and lowest temperatures recorded at 2 meters, useful for studying temperature extremes.

    11. **Temperature Range at 2m** 📉📈:  
        - The difference between the maximum and minimum temperatures recorded at 2 meters. This helps in understanding daily temperature variations.

    12. **Surface Skin Temperature** 🌞:  
        - This represents the temperature of the Earth’s surface, an important indicator for assessing changes in the land surface temperature due to climate change.

    13. **Wind Speed at 10m and 50m** 🌬️:  
        - Wind speeds are measured at two different heights (10 meters and 50 meters). These data points are essential for understanding wind patterns and their role in weather systems.

    14. **Max and Min Wind Speed at 10m and 50m** 🌪️:  
        - The maximum and minimum wind speeds recorded at both 10 meters and 50 meters. These figures help assess wind variability and extreme wind events.

    15. **Wind Speed Range at 10m and 50m** 🌪️:  
        - The difference between the maximum and minimum wind speeds at each height, giving insight into wind fluctuations over time.

    This dataset provides a comprehensive set of meteorological features, which will allow you to conduct thorough exploratory data analysis (EDA) and model climate change predictions for Nepal. Use the dropdown to select the dataset of your choice, and start exploring how these variables interconnect to reveal insights into Nepal's changing climate! 🌱
    """)

    st.divider()