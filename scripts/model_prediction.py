import pandas as pd

def prepare_input(year, month, province):
    """Prepares input DataFrame for prediction."""
    input_data = pd.DataFrame({
        'year': [year],
        'month': [month],
        'province': [province]
    })
    return input_data

def predict(model, input_data):
    """Generates prediction using the trained model."""
    predictions = model.predict(input_data)[0]
    return predictions
