import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def show():
    st.write("""
    This section includes the feature engineering of environmental glacier data""")

    if "glacierdf" in st.session_state:
        glacierdf = st.session_state.cleaned_weatherClimatedf
    else:
        st.error(" Data not loaded. Please go to the overview and load again.")
        return

    glacierdf = st.session_state.glacierdf
    
    # Ensure the necessary columns are numeric (handling potential issues with strings or non-numeric values)
    for col in ['Maximum Elevation', 'Minimum Elevation', 'Glacier Area', 'Mean Length', 'Mean Elevation', 
                'Latitude', 'Longitude', 'Accumulation Orientation', 'Ablation Orientation']:
        glacierdf[col] = pd.to_numeric(glacierdf[col], errors='coerce')

    # Feature Engineering Steps:

    # 1. Calculate the Elevation Range (Maximum Elevation - Minimum Elevation)
    glacierdf['Elevation Range'] = glacierdf['Maximum Elevation'] - glacierdf['Minimum Elevation']

    # 2. Calculate the Area-to-Length Ratio (Glacier Area / Mean Length)
    glacierdf['Area-to-Length Ratio'] = glacierdf['Glacier Area'] / glacierdf['Mean Length']

    # 3. Create a new feature: Glacier Height Index (Mean Elevation / Mean Length)
    glacierdf['Height Index'] = glacierdf['Mean Elevation'] / glacierdf['Mean Length']


    # 5. Normalize Latitude and Longitude (to a 0-1 scale)
    glacierdf['Normalized Latitude'] = (glacierdf['Latitude'] - glacierdf['Latitude'].min()) / (glacierdf['Latitude'].max() - glacierdf['Latitude'].min())
    glacierdf['Normalized Longitude'] = (glacierdf['Longitude'] - glacierdf['Longitude'].min()) / (glacierdf['Longitude'].max() - glacierdf['Longitude'].min())

    # 6. Create a feature based on Glacier Source encoding (using categorical encoding)
    glacierdf['Glacier Source Encoding'] = glacierdf['Glacier Source'].astype('category').cat.codes

    # 7. Create a new feature to indicate high altitude glaciers (Mean Elevation > 3000 meters)
    glacierdf['High Altitude Glacier'] = glacierdf['Mean Elevation'].apply(lambda x: 1 if x > 3000 else 0)

    # 8. Calculate the Slope Range (Difference between Accumulation and Ablation Orientation)
    glacierdf['Slope Range'] = glacierdf['Accumulation Orientation'] - glacierdf['Ablation Orientation']



    # Plotting Elevation Range vs. Area-to-Length Ratio
    st.subheader('Elevation Range vs Area-to-Length Ratio')
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.scatterplot(data=glacierdf, x='Elevation Range', y='Area-to-Length Ratio', ax=ax)
    ax.set_title('Elevation Range vs Area-to-Length Ratio')
    ax.set_xlabel('Elevation Range (meters)')
    ax.set_ylabel('Area-to-Length Ratio')
    st.pyplot(fig)

    # Plotting Glacier Height Index distribution
    st.subheader('Glacier Height Index Distribution')
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.histplot(glacierdf['Height Index'], bins=20, kde=True, ax=ax)
    ax.set_title('Glacier Height Index Distribution')
    ax.set_xlabel('Glacier Height Index')
    ax.set_ylabel('Frequency')
    st.pyplot(fig)

    # Plotting Glacier Area vs Glacier Length with a regression line
    st.subheader('Glacier Area vs Glacier Length')
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.regplot(data=glacierdf, x='Glacier Area', y='Mean Length', scatter_kws={'s': 10}, line_kws={'color': 'red'}, ax=ax)
    ax.set_title('Glacier Area vs Glacier Length')
    ax.set_xlabel('Glacier Area (square meters)')
    ax.set_ylabel('Glacier Length (meters)')
    st.pyplot(fig)

    # Plotting the relationship between Latitude and Longitude (Geospatial)
    st.subheader('Geospatial Distribution: Latitude vs Longitude')
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.scatterplot(data=glacierdf, x='Normalized Latitude', y='Normalized Longitude', ax=ax)
    ax.set_title('Geospatial Distribution: Latitude vs Longitude')
    ax.set_xlabel('Normalized Latitude')
    ax.set_ylabel('Normalized Longitude')
    st.pyplot(fig)


    st.divider()