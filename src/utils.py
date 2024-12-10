import os
import json
from typing import Dict, Any

def create_output_directory() -> None:
    """
    Create output directory if it doesn't exist
    """
    if not os.path.exists('outputs'):
        os.makedirs('outputs')

def save_metrics(metrics: Dict[str, Any], filepath: str) -> None:
    """
    Save metrics to a JSON file
    """
    with open(filepath, 'w') as f:
        json.dump(metrics, f, indent=4)