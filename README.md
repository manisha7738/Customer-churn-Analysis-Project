# Customer Churn Analysis Project

This project analyzes customer churn data to identify patterns and predict customer churn using machine learning techniques.

## Project Structure

```
├── src/
│   ├── data_loader.py    # Data loading and preprocessing functions
│   ├── visualization.py   # Data visualization functions
│   ├── model.py          # Machine learning model implementation
│   └── utils.py          # Utility functions
├── outputs/              # Directory for saving outputs
├── main.py              # Main script to run the analysis
├── requirements.txt     # Project dependencies
└── README.md           # Project documentation
```

## Features

- Data preprocessing and cleaning
- Exploratory data analysis with visualizations
- Customer churn prediction using Random Forest
- Feature importance analysis
- Model performance evaluation

## Setup and Installation

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Place your customer data CSV file in the project directory
2. Update the data file path in `main.py`
3. Run the analysis:
   ```bash
   python main.py
   ```

## Outputs

The analysis generates several outputs in the `outputs/` directory:
- Churn distribution visualization
- Correlation matrix
- Feature importance plot
- Model performance metrics

## Data Requirements

The input CSV file should contain the following columns:
- Customer demographic information
- Service usage metrics
- Customer behavior data
- Churn status (target variable)

## License

This project is licensed under the MIT License - see the LICENSE file for details.