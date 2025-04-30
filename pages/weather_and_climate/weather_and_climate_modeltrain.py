import streamlit as st
from scripts.model_train import  train_model
from scripts.visualization import plot_actual_vs_predicted, plot_residuals


def show():
    st.write("""

        Model-train - weather and climate data 

    """)

    
    if "cleaned_weatherClimatedf" in st.session_state:
        cleaned_weatherClimatedf = st.session_state.cleaned_weatherClimatedf
    else:
        st.error("Data not loaded. Please go to the overview and load again.")
        return


        
    # Initialize session state
    if 'trained_model' not in st.session_state:
        st.session_state.trained_model = None

    st.subheader("⚙️ Model Training")

    # Model selection
    model_choice = st.selectbox("Select Model", ["Random Forest", "Gradient Boosting", "Linear Regression", "Ridge Regression"])

    # Train/Test split
    split = st.slider("Select Train/Test Split % for Training", min_value=50, max_value=95, value=80, step=5) / 100

    # Feature and target columns
    feature_cols = ['year', 'month', 'province']
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

    if st.button("Train Model"):

        with st.spinner('🚀 Training model. Please wait...'):
            model, metrics = train_model(cleaned_weatherClimatedf, model_choice, split, feature_cols, target_cols)

       
        st.progress(100, text="✅ Training Complete!")


        st.success(f"✅ Model Trained Successfully!")
        st.balloons()
        st.subheader("📊 Model Evaluation Metrics")

        col1, col2 = st.columns(2)
        with col1:
            st.write(f"**R² Score:** {metrics['R2 Score']:.4f}")
            st.write(f"**MSE:** {metrics['MSE']:.4f}")
        with col2:
            st.write(f"**RMSE:** {metrics['RMSE']:.4f}")
            st.write(f"**MAE:** {metrics['MAE']:.4f}")


        st.session_state.trained_model = model

        y_true = metrics['y_true']
        y_pred = metrics['y_pred']

        # Actual vs Predicted
        st.subheader("Actual vs Predicted Values")
        fig1 = plot_actual_vs_predicted(y_true, y_pred)
        st.pyplot(fig1)

        # Residual Analysis
        st.subheader("Residual Analysis")
        fig2 = plot_residuals(y_true, y_pred)
        st.pyplot(fig2)

        st.divider()