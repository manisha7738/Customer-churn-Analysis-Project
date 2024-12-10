import matplotlib.pyplot as plt
import seaborn as sns
from typing import Dict, Any
import pandas as pd

def plot_churn_distribution(df: pd.DataFrame) -> None:
    """
    Plot the distribution of churned vs non-churned customers
    """
    plt.figure(figsize=(8, 6))
    sns.countplot(data=df, x='Churn')
    plt.title('Distribution of Customer Churn')
    plt.savefig('outputs/churn_distribution.png')
    plt.close()

def plot_feature_importance(feature_importance: Dict[str, Any]) -> None:
    """
    Plot feature importance
    """
    plt.figure(figsize=(10, 6))
    sns.barplot(x=list(feature_importance.values()), 
                y=list(feature_importance.keys()))
    plt.title('Feature Importance in Churn Prediction')
    plt.xlabel('Importance Score')
    plt.savefig('outputs/feature_importance.png')
    plt.close()

def plot_correlation_matrix(df: pd.DataFrame) -> None:
    """
    Plot correlation matrix of numerical features
    """
    plt.figure(figsize=(12, 8))
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm', center=0)
    plt.title('Correlation Matrix of Features')
    plt.savefig('outputs/correlation_matrix.png')
    plt.close()