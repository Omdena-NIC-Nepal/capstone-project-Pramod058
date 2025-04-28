import streamlit as st
import pandas as pd
from scripts.model_prediction import prepare_input, predict


def show():
    st.write("""
    This page allows you to make predictions using the trained model. """)

    if 'trained_model' not in st.session_state or st.session_state.trained_model is None:
        st.warning("⚠️ Please train the model first on the Model Train page.")
        return

    model = st.session_state.trained_model

    # Mappings for Month and Province
    month_mapping = {
        1: "January", 2: "February", 3: "March", 4: "April",
        5: "May", 6: "June", 7: "July", 8: "August",
        9: "September", 10: "October", 11: "November", 12: "December"
    }
    reverse_month_mapping = {v: k for k, v in month_mapping.items()}

    province_mapping = {
        1: "1 - Koshi Province",
        2: "2 - Madesh Province",
        3: "3 - Bagmati Province",
        4: "4 - Gandaki Province",
        5: "5 - Lumbini Province",
        6: "6 - Karnali Province",
        7: "7 - Sudurpashchim Province",
    }
    reverse_province_mapping = {v: k for k, v in province_mapping.items()}

    selected_year = st.number_input("Enter Year", min_value=2023, max_value=2100, step=1)
    selected_month_name = st.selectbox("Select Month", list(month_mapping.values()))
    selected_province_name = st.selectbox("Select Province", list(province_mapping.values()))

    selected_month = reverse_month_mapping[selected_month_name]
    selected_province = reverse_province_mapping[selected_province_name]

    if st.button("Predict"):
        input_data = prepare_input(selected_year, selected_month, selected_province)
        prediction = predict(model, input_data)

        target_cols = [
            'precipitation_total',
            'relative_humidity_2m',
            'air_temp_2m',
            'max_temp_2m',
            'min_temp_2m',
            'wind_speed_10m',
            'max_wind_speed_10m',
            'min_wind_speed_10m'
        ]

        result = pd.DataFrame({
            'Parameter': target_cols,
            'Predicted Value': prediction
        })

        st.success(f"📈 Predictions for {selected_month_name} {selected_year} in {selected_province_name}:")
        st.dataframe(result)


    st.divider()