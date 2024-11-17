import pandas as pd

def load_dataset(file_path):
    """
    Load a dataset from a CSV file.
    Args:
        file_path (str): Path to the CSV file.
    Returns:
        pd.DataFrame: Loaded dataset as a DataFrame.
    """
    try:
        data = pd.read_csv(file_path)
        print(f"Loaded dataset from {file_path}")
        return data
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return None

def preprocess_data(data):
    """
    Preprocess the data for further analysis or modeling.
    Args:
        data (pd.DataFrame): The input dataset.
    Returns:
        pd.DataFrame: Preprocessed dataset.
    """
    # Example: Clean and fill missing values
    data = data.fillna("Unknown")
    data['Score'] = data['Score'].apply(pd.to_numeric, errors='coerce').fillna(0)
    return data

