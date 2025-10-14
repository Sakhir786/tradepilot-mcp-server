"""
Layer 4: Volume Strength Engine
RVOL and volume spike detection
"""
import pandas as pd
from typing import Dict

class Layer4VolumeStrength:
    """Volume strength analysis with RVOL"""
    
    def analyze(self, df: pd.DataFrame) -> Dict:
        """Run volume strength analysis"""
        df = df.copy()
        
        # Calculate RVOL
        avg_volume = df["volume"].rolling(window=20).mean()
        rvol = df["volume"].iloc[-1] / avg_volume.iloc[-1] if avg_volume.iloc[-1] > 0 else 1
        
        # Classify RVOL state
        if rvol >= 3.0:
            state = "EXTREME"
        elif rvol >= 2.0:
            state = "HIGH"
        elif rvol >= 1.5:
            state = "ELEVATED"
        elif rvol >= 1.0:
            state = "NORMAL"
        else:
            state = "LOW"
        
        return {
            "rvol": round(rvol, 2),
            "rvol_state": state,
            "avg_volume": float(avg_volume.iloc[-1]),
            "current_volume": float(df["volume"].iloc[-1]),
            "signal": "STRONG_BUY" if rvol > 2.0 and df["close"].iloc[-1] > df["open"].iloc[-1] else "NEUTRAL"
        }
