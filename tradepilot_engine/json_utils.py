"""
JSON Utilities - Convert NumPy types to native Python types
"""
import numpy as np
import pandas as pd
from typing import Any, Dict, List

def clean_for_json(obj: Any) -> Any:
    """
    Recursively convert NumPy types to native Python types
    and handle NaN/Inf values
    """
    if isinstance(obj, dict):
        return {key: clean_for_json(value) for key, value in obj.items()}
    
    elif isinstance(obj, list):
        return [clean_for_json(item) for item in obj]
    
    elif isinstance(obj, (np.integer, np.int64, np.int32)):
        return int(obj)
    
    elif isinstance(obj, (np.floating, np.float64, np.float32)):
        if np.isnan(obj) or np.isinf(obj):
            return None
        return float(obj)
    
    elif isinstance(obj, np.bool_):
        return bool(obj)
    
    elif isinstance(obj, np.ndarray):
        return clean_for_json(obj.tolist())
    
    elif pd.isna(obj):
        return None
    
    return obj
