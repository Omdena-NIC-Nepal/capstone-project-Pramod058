import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


def show():
    st.write("""
    This section includes the feature engineering of weather and climate data overview for Nepal. """)

    if "cleaned_weatherClimatedf" in st.session_state:
        cleaned_weatherClimatedf = st.session_state.cleaned_weatherClimatedf
    else:
        st.error(" Data not loaded. Please go to the overview and load again.")
        return


    # Example Feature: If Min and Max temperature exist
    if 'max_temp_2m' in cleaned_weatherClimatedf.columns and 'min_temp_2m' in cleaned_weatherClimatedf.columns:
        cleaned_weatherClimatedf['temp_range_2m'] = cleaned_weatherClimatedf['max_temp_2m'] - cleaned_weatherClimatedf['min_temp_2m']
        st.success("Created new feature: Temperature Range (max_temp_2m - min_temp_2m)")
        st.dataframe(cleaned_weatherClimatedf[['max_temp_2m', 'min_temp_2m', 'temp_range_2m']].head())
    else:
        st.warning("No 'max_temp_2m' and 'mix' columns found to create Temp Range")

    # Selectbox to select a column to plot
    st.subheader("Visualize a Feature")
    column_to_plot = st.selectbox("Select a column to plot", cleaned_weatherClimatedf.columns, index=3)

    # Plotting
    fig, ax = plt.subplots()
    if pd.api.types.is_numeric_dtype(cleaned_weatherClimatedf[column_to_plot]):
        cleaned_weatherClimatedf[column_to_plot].hist(ax=ax, bins=30)
        ax.set_title(f"Distribution of {column_to_plot}")
        st.pyplot(fig)
    else:
        st.warning("Selected column is not numeric for plotting.")

    st.divider()
