# Configuration for Polygon.io API
# In production, use environment variables instead of hardcoding

import os
from dotenv import load_dotenv

load_dotenv()

POLYGON_API_KEY = os.getenv("POLYGON_API_KEY", "")
BASE_URL = "https://api.polygon.io"
