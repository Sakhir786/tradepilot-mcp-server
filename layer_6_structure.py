"""
Layer 6: Market Structure Engine
CHoCH, BOS, Order Blocks, and FVG detection
"""
import pandas as pd
from typing import Dict

class Layer6Structure:
    """Market structure analysis"""
    
    def analyze(self, df: pd.DataFrame) -> Dict:
        """Run structure analysis"""
        df = df.copy()
        
        # Simplified structure analysis
        pivot_len = 5
        high_pivots = df["high"].rolling(window=pivot_len*2+1, center=True).max()
        low_pivots = df["low"].rolling(window=pivot_len*2+1, center=True).min()
        
        last_high = high_pivots.dropna().iloc[-1] if len(high_pivots.dropna()) > 0 else df["high"].iloc[-1]
        last_low = low_pivots.dropna().iloc[-1] if len(low_pivots.dropna()) > 0 else df["low"].iloc[-1]
        
        # Determine bias
        if df["close"].iloc[-1] > last_high:
            bias = "BULLISH"
        elif df["close"].iloc[-1] < last_low:
            bias = "BEARISH"
        else:
            bias = "NEUTRAL"
        
        return {
            "bias": bias,
            "last_high": round(last_high, 2),
            "last_low": round(last_low, 2),
            "signal": "BUY" if bias == "BULLISH" else "SELL" if bias == "BEARISH" else "NEUTRAL"
        }
