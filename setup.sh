#!/bin/bash

echo "🚀 TradePilot MCP Server Setup"
echo "================================"

# Check Python version
python_version=$(python3 --version 2>&1 | awk '{print $2}')
echo "✓ Python version: $python_version"

# Create virtual environment
echo "📦 Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "🔌 Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "⬆️  Upgrading pip..."
pip install --upgrade pip

# Install dependencies
echo "📚 Installing dependencies..."
pip install -r requirements.txt

# Create .env file if it doesn't exist
if [ ! -f .env ]; then
    echo "📝 Creating .env file..."
    echo "POLYGON_API_KEY=your_polygon_api_key_here" > .env
    echo "⚠️  IMPORTANT: Edit .env file and add your Polygon.io API key"
else
    echo "✓ .env file already exists"
fi

# Create necessary directories
echo "📁 Creating directories..."
mkdir -p tradepilot_engine/layers
mkdir -p logs
mkdir -p cache

echo ""
echo "✅ Setup Complete!"
echo ""
echo "📋 Next Steps:"
echo "1. Edit .env file and add your POLYGON_API_KEY"
echo "2. Run: source venv/bin/activate"
echo "3. Run: python test_connection.py (to verify Polygon connection)"
echo "4. Run: uvicorn main:app --reload --port 10000"
echo "5. Open: http://localhost:10000/docs"
echo ""
echo "🔗 MCP Connection: http://localhost:10000"
echo ""
