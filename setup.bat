@echo off
echo 🚀 TradePilot MCP Server Setup
echo ================================
echo.

REM Check Python version
python --version
echo.

REM Create virtual environment
echo 📦 Creating virtual environment...
python -m venv venv
echo.

REM Activate virtual environment
echo 🔌 Activating virtual environment...
call venv\Scripts\activate.bat
echo.

REM Upgrade pip
echo ⬆️  Upgrading pip...
python -m pip install --upgrade pip
echo.

REM Install dependencies
echo 📚 Installing dependencies...
pip install -r requirements.txt
echo.

REM Create .env file if it doesn't exist
if not exist .env (
    echo 📝 Creating .env file...
    echo POLYGON_API_KEY=your_polygon_api_key_here > .env
    echo ⚠️  IMPORTANT: Edit .env file and add your Polygon.io API key
) else (
    echo ✓ .env file already exists
)
echo.

REM Create necessary directories
echo 📁 Creating directories...
if not exist tradepilot_engine\layers mkdir tradepilot_engine\layers
if not exist logs mkdir logs
if not exist cache mkdir cache
echo.

echo ✅ Setup Complete!
echo.
echo 📋 Next Steps:
echo 1. Edit .env file and add your POLYGON_API_KEY
echo 2. Run: venv\Scripts\activate
echo 3. Run: python test_connection.py (to verify Polygon connection)
echo 4. Run: uvicorn main:app --reload --port 10000
echo 5. Open: http://localhost:10000/docs
echo.
echo 🔗 MCP Connection: http://localhost:10000
echo.
pause
