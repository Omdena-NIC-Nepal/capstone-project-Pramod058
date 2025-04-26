import pandas as pd # type: ignore


def load_data(file: str) -> pd.DataFrame:
    """
    Load data from a CSV file into a pandas DataFrame.
    Returns:
        pd.DataFrame: DataFrame containing the loaded data.
    """
    try:
        df = pd.read_csv(file)
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return e 
    

def remove_unwanted_columns(df: pd.DataFrame, columns_to_remove: list) -> pd.DataFrame:
    """
    Remove unwanted columns from the DataFrame.
    Args:
        df (pd.DataFrame): The DataFrame to clean.
        columns_to_remove (list): List of column names to remove.
    Returns:
        pd.DataFrame: DataFrame with unwanted columns removed.
    """

    return df.drop(columns=columns_to_remove, errors='ignore')



def clean_data(df):
    """
    Clean the DataFrame by dropping rows with missing values.
    Returns:
        pd.DataFrame: Cleaned DataFrame.
    """
    return df.dropna()