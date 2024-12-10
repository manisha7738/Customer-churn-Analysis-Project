from src.data_loader import load_data, preprocess_data, split_features_target
from src.visualization import (
    plot_churn_distribution, 
    plot_feature_importance, 
    plot_correlation_matrix
)
from src.model import ChurnPredictor
from src.utils import create_output_directory, save_metrics

def main():
    # Create output directory
    create_output_directory()
    
    # Load and preprocess data
    # Note: Replace 'customer_data.csv' with your actual data file
    df = load_data('customer_data.csv')
    df_processed = preprocess_data(df)
    
    # Create visualizations
    plot_churn_distribution(df)
    plot_correlation_matrix(df_processed)
    
    # Prepare data for modeling
    X, y = split_features_target(df_processed)
    
    # Train and evaluate model
    predictor = ChurnPredictor()
    predictor.train(X, y)
    
    # Get and plot feature importance
    feature_importance = predictor.get_feature_importance(X.columns.tolist())
    plot_feature_importance(feature_importance)
    
    # Save evaluation metrics
    metrics = predictor.evaluate(X, y)
    save_metrics(metrics, 'outputs/metrics.json')

if __name__ == "__main__":
    main()