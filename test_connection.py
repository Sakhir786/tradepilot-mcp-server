#!/usr/bin/env python3
"""
Test script to verify Polygon.io API connection
"""
import os
import sys
from dotenv import load_dotenv
import requests

def test_polygon_connection():
    """Test Polygon.io API connectivity"""
    load_dotenv()
    
    api_key = os.getenv("POLYGON_API_KEY")
    
    if not api_key or api_key == "your_polygon_api_key_here":
        print("❌ ERROR: POLYGON_API_KEY not set in .env file")
        print("Please edit .env and add your Polygon.io API key")
        return False
    
    print(f"🔑 API Key found: {api_key[:10]}...")
    print("🔄 Testing connection to Polygon.io...")
    
    # Test with a simple ticker lookup
    url = f"https://api.polygon.io/v3/reference/tickers?search=AAPL&active=true&limit=1&apiKey={api_key}"
    
    try:
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            if "results" in data and len(data["results"]) > 0:
                print("✅ Connection successful!")
                print(f"✓ Retrieved data for: {data['results'][0]['ticker']}")
                print(f"✓ Company: {data['results'][0].get('name', 'N/A')}")
                return True
            else:
                print("⚠️  Connection successful but no data returned")
                return False
        elif response.status_code == 403:
            print("❌ Authentication failed - Invalid API key")
            return False
        elif response.status_code == 429:
            print("⚠️  Rate limit exceeded - Your API key is valid but you've hit the rate limit")
            return False
        else:
            print(f"❌ Request failed with status code: {response.status_code}")
            print(f"Response: {response.text}")
            return False
            
    except requests.exceptions.Timeout:
        print("❌ Connection timeout - Check your internet connection")
        return False
    except requests.exceptions.ConnectionError:
        print("❌ Connection error - Check your internet connection")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {str(e)}")
        return False

if __name__ == "__main__":
    print("=" * 50)
    print("TradePilot MCP Server - Connection Test")
    print("=" * 50)
    print()
    
    success = test_polygon_connection()
    
    print()
    if success:
        print("🎉 All systems ready!")
        print("Run: uvicorn main:app --reload --port 10000")
        sys.exit(0)
    else:
        print("❌ Setup incomplete. Please fix the errors above.")
        sys.exit(1)
