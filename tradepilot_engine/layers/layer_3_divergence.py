"""
Layer 3: Divergence Engine
Delta divergence detection and CDV analysis
"""
import pandas as pd
import numpy as np
from typing import Dict

class Layer3Divergence:
    """Divergence analysis using delta and CDV"""
    
    def analyze(self, df: pd.DataFrame) -> Dict:
        """Run divergence analysis"""
        df = df.copy()
        
        # Calculate delta (simplified)
        delta = np.where(df["close"] >= df["open"], df["volume"], -df["volume"])
        cdv = pd.Series(delta).cumsum()
        
        # CDV analysis
        cdv_slope = np.polyfit(np.arange(len(cdv.iloc[-20:])), cdv.iloc[-20:], 1)[0] if len(cdv) >= 20 else 0
        cdv_bias = "BULLISH" if cdv_slope > 0 else "BEARISH"
        
        return {
            "cdv": float(cdv.iloc[-1]),
            "cdv_slope": round(cdv_slope, 2),
            "cdv_bias": cdv_bias,
            "signal": "BUY" if cdv_bias == "BULLISH" else "SELL"
        }
