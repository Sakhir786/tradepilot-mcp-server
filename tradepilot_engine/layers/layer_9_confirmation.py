"""
Layer 9: Confirmation Engine
Multi-timeframe confirmation system
"""
import pandas as pd
from typing import Dict

class Layer9Confirmation:
    """Confirmation analysis across layers"""
    
    def analyze(self, df: pd.DataFrame, layer_results: Dict) -> Dict:
        """Run confirmation analysis based on other layers"""
        
        # Collect signals from other layers
        signals = []
        
        if "layer_1_momentum" in layer_results:
            mom_signal = layer_results["layer_1_momentum"].get("signal", "NEUTRAL")
            if "BUY" in mom_signal:
                signals.append(1)
            elif "SELL" in mom_signal:
                signals.append(-1)
            else:
                signals.append(0)
        
        if "layer_2_volume" in layer_results:
            vol_signal = layer_results["layer_2_volume"].get("signal", "NEUTRAL")
            if "BUY" in vol_signal:
                signals.append(1)
            elif "SELL" in vol_signal:
                signals.append(-1)
            else:
                signals.append(0)
        
        if "layer_5_trend" in layer_results:
            trend_signal = layer_results["layer_5_trend"].get("signal", "NEUTRAL")
            if "BUY" in trend_signal:
                signals.append(1)
            elif "SELL" in trend_signal:
                signals.append(-1)
            else:
                signals.append(0)
        
        # Calculate confirmation
        if len(signals) > 0:
            avg_signal = sum(signals) / len(signals)
            confirmation_signal = int(avg_signal * 2)  # Scale to -2 to +2
            confidence = abs(avg_signal) * 100
        else:
            confirmation_signal = 0
            confidence = 0
        
        # Generate signal
        if confirmation_signal >= 2:
            signal = "STRONG_BUY"
        elif confirmation_signal == 1:
            signal = "BUY"
        elif confirmation_signal <= -2:
            signal = "STRONG_SELL"
        elif confirmation_signal == -1:
            signal = "SELL"
        else:
            signal = "NEUTRAL"
        
        return {
            "confirmation_signal": confirmation_signal,
            "confidence": round(confidence, 2),
            "signals_aligned": len([s for s in signals if abs(s) > 0]),
            "signal": signal
        }
