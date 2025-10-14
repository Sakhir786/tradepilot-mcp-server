"""
TradePilot Engine - Multi-Layer Technical Analysis System
"""

__version__ = "2.0.0"
__author__ = "TradePilot Team"

from .engine_core import TradePilotEngine
from .data_processor import DataProcessor

__all__ = ["TradePilotEngine", "DataProcessor"]
