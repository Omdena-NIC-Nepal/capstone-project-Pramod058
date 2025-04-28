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



def glacier_input(latitude, longitude, mean_elevation, mean_length, mean_depth, height_range, average_slope, compactness):
    data = {
        'Latitude': [latitude],
        'Longitude': [longitude],
        'Mean Elevation': [mean_elevation],
        'Mean Length': [mean_length],
        'Mean Depth': [mean_depth],
        'Height Range': [height_range],
        'Average Slope (deg)': [average_slope],
        'Compactness': [compactness]
    }
    return pd.DataFrame(data)
