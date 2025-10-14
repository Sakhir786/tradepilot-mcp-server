"""
Layer 5: Trend Engine
SuperTrend, ADX/DMI, and moving averages
"""
import pandas as pd
import numpy as np
from typing import Dict

class Layer5Trend:
    """Trend analysis with multiple indicators"""
    
    def analyze(self, df: pd.DataFrame) -> Dict:
        """Run trend analysis"""
        df = df.copy()
        
        # Calculate moving averages
        ma20 = df["close"].rolling(window=20).mean()
        ma50 = df["close"].rolling(window=50).mean()
        ma200 = df["close"].rolling(window=200).mean()
        
        # Calculate ADX (simplified)
        up_move = df["high"].diff()
        down_move = -df["low"].diff()
        plus_dm = np.where((up_move > down_move) & (up_move > 0), up_move, 0)
        minus_dm = np.where((down_move > up_move) & (down_move > 0), down_move, 0)
        
        tr = df["true_range"]
        atr = tr.rolling(window=14).mean()
        plus_di = 100 * pd.Series(plus_dm).rolling(window=14).mean() / atr
        minus_di = 100 * pd.Series(minus_dm).rolling(window=14).mean() / atr
        dx = 100 * abs(plus_di - minus_di) / (plus_di + minus_di)
        adx = dx.rolling(window=14).mean()
        
        # Trend classification
        trend_direction = "BULLISH" if plus_di.iloc[-1] > minus_di.iloc[-1] else "BEARISH"
        trend_strength = "STRONG" if adx.iloc[-1] > 40 else "MODERATE" if adx.iloc[-1] > 25 else "WEAK"
        
        # Trend score
        ma_trend = 1 if (df["close"].iloc[-1] > ma20.iloc[-1] > ma50.iloc[-1] > ma200.iloc[-1]) else -1 if (df["close"].iloc[-1] < ma20.iloc[-1] < ma50.iloc[-1] < ma200.iloc[-1]) else 0
        dmi_trend = 1 if plus_di.iloc[-1] > minus_di.iloc[-1] else -1
        trend_score = (ma_trend + dmi_trend) / 2 * 100
        
        return {
            "trend_score": round(trend_score, 2),
            "trend_direction": trend_direction,
            "trend_strength": trend_strength,
            "adx": round(adx.iloc[-1], 2),
            "plus_di": round(plus_di.iloc[-1], 2),
            "minus_di": round(minus_di.iloc[-1], 2),
            "ma20": round(ma20.iloc[-1], 2),
            "ma50": round(ma50.iloc[-1], 2),
            "ma200": round(ma200.iloc[-1], 2),
            "signal": "STRONG_BUY" if trend_score > 50 and adx.iloc[-1] > 25 else "STRONG_SELL" if trend_score < -50 and adx.iloc[-1] > 25 else "NEUTRAL"
        }
