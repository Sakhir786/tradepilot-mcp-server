"""
Layer 10: Candle Intelligence Engine
Advanced candlestick pattern detection
"""
import pandas as pd
import numpy as np
from typing import Dict

class Layer10CandleIntelligence:
    """Candle pattern intelligence"""
    
    def analyze(self, df: pd.DataFrame) -> Dict:
        """Run candle pattern analysis"""
        df = df.copy()
        
        # Get last few candles
        if len(df) < 3:
            return {"error": "Not enough data", "signal": "NEUTRAL"}
        
        # Current candle
        is_bullish = df["close"].iloc[-1] > df["open"].iloc[-1]
        body_size = abs(df["close"].iloc[-1] - df["open"].iloc[-1])
        candle_range = df["high"].iloc[-1] - df["low"].iloc[-1]
        body_percent = body_size / candle_range if candle_range > 0 else 0
        
        # Previous candle
        prev_bullish = df["close"].iloc[-2] > df["open"].iloc[-2]
        prev_body = abs(df["close"].iloc[-2] - df["open"].iloc[-2])
        
        # Pattern detection
        bullish_engulfing = is_bullish and not prev_bullish and body_size > prev_body * 1.1
        bearish_engulfing = not is_bullish and prev_bullish and body_size > prev_body * 1.1
        
        doji = body_percent < 0.1
        hammer = is_bullish and df["lower_wick"].iloc[-1] > body_size * 2
        shooting_star = not is_bullish and df["upper_wick"].iloc[-1] > body_size * 2
        
        # Pattern score
        pattern_score = 0
        if bullish_engulfing or hammer:
            pattern_score = 60
        elif bearish_engulfing or shooting_star:
            pattern_score = -60
        elif doji:
            pattern_score = 0
        
        # Pattern strength
        pattern_strength = "STRONG" if abs(pattern_score) > 50 else "MODERATE" if abs(pattern_score) > 30 else "WEAK"
        
        # Signal
        if pattern_score > 40:
            signal = "BUY"
        elif pattern_score < -40:
            signal = "SELL"
        else:
            signal = "NEUTRAL"
        
        return {
            "pattern_score": round(pattern_score, 2),
            "pattern_strength": pattern_strength,
            "body_percent": round(body_percent * 100, 2),
            "is_bullish": is_bullish,
            "is_doji": doji,
            "is_hammer": hammer,
            "is_shooting_star": shooting_star,
            "bullish_engulfing": bullish_engulfing,
            "bearish_engulfing": bearish_engulfing,
            "signal": signal
        }
