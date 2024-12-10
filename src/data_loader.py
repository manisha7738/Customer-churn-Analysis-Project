import pandas as pd
from typing import Tuple

def load_data(filepath: str) -> pd.DataFrame:
    """
    Load customer churn data from CSV file
    """
    return pd.read_csv(filepath)

def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Preprocess the data by handling missing values and encoding categorical variables
    """
    # Create a copy of the dataframe
    df_processed = df.copy()
    
    # Handle missing values
    df_processed = df_processed.fillna(df_processed.mean(numeric_only=True))
    
    # Convert categorical variables to numerical
    categorical_columns = df_processed.select_dtypes(include=['object']).columns
    for column in categorical_columns:
        df_processed[column] = pd.factorize(df_processed[column])[0]
    
    return df_processed

def split_features_target(df: pd.DataFrame) -> Tuple[pd.DataFrame, pd.Series]:
    """
    Split the data into features and target
    """
    X = df.drop('Churn', axis=1)
    y = df['Churn']
    return X, y