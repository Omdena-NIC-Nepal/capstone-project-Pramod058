import streamlit as st

try:
    from scripts.model_prediction import glacier_input, predict
except ImportError as e:
    st.error(f"Failed to import modules: {e}")
    st.stop()

def show():
    st.subheader("Glacier Area Prediction")
    st.write("""
    Welcome!  
    This tool helps you **predict the approximate area of a glacier** based on various glacier characteristics.  
    Please enter the required environmental parameters below —  
    The more accurate the input, the better the prediction will be. 🌟
    """)

    if 'trained_model' not in st.session_state or st.session_state.trained_model is None:
        st.warning(" Please train the model first on the Model Train page.")
        return
    
    if 'glacierdf' not in st.session_state:
        st.error(" Cleaned Glacier Data not available. Please load and clean data first.")
        return
    
    model = st.session_state.trained_model
    glacierdf = st.session_state.glacierdf

    st.subheader("Enter Glacier Characteristics:")


    random_sample = glacierdf.sample(1).squeeze()
    with st.form("glacier_input_form"):
        col1, col2 = st.columns(2)
        with col1:

            latitude = st.number_input("Latitude", format="%.6f", value=float(random_sample['Latitude']))
            longitude = st.number_input("Longitude", format="%.6f", value=float(random_sample['Longitude']))
            mean_elevation = st.number_input("Mean Elevation (meters)", value=float(random_sample['Mean Elevation']))
            mean_length = st.number_input("Mean Length (meters)", value=float(random_sample['Mean Length']))
        with col2:
            mean_depth = st.number_input("Mean Depth (meters)", value=float(random_sample['Mean Depth']))
            height_range = st.number_input("Height Range (meters)", value=float(random_sample['Height Range']))
            average_slope = st.number_input("Average Slope (degrees)", value=float(random_sample['Average Slope (deg)']))
            compactness = st.number_input("Compactness", format="%.6f", value=float(random_sample['Compactness']))

        submit_button = st.form_submit_button(label="🔮 Predict Glacier Area")



    if submit_button:
        input_data = glacier_input(
            latitude, longitude, mean_elevation,
            mean_length, mean_depth, height_range,
            average_slope, compactness
        )

        prediction = predict(model, input_data)
        predicted_value = float(prediction[0])

        st.success(f" **Predicted Glacier Area:** {predicted_value:.4f} sq. km")
        st.balloons()
    st.divider()
    st.info("""
    📌 **Note:**  
    The model was trained using glacier environmental features like elevation, slope, depth, and location.  
    Please provide realistic values for the most accurate prediction! 
    """)

