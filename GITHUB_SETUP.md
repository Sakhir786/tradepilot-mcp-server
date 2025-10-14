# 🎯 GitHub Setup Guide

Complete guide to setting up TradePilot MCP Server from a fresh git clone.

---

## 📋 Prerequisites

Before you begin, make sure you have:
- ✅ Python 3.8 or higher installed
- ✅ Git installed
- ✅ A Polygon.io API key ([Sign up free](https://polygon.io/))
- ✅ Terminal/Command Prompt access

---

## 🚀 Setup Steps

### Step 1: Clone the Repository

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/tradepilot-mcp-server.git

# Navigate into the directory
cd tradepilot-mcp-server
```

### Step 2: Run the Setup Script

**On Linux/Mac:**
```bash
# Make the script executable
chmod +x setup.sh

# Run setup
./setup.sh
```

**On Windows:**
```bash
# Run setup
setup.bat
```

This will:
- Create a Python virtual environment
- Install all dependencies
- Create a `.env` file template
- Set up necessary directories

### Step 3: Configure Your API Key

Edit the `.env` file and add your Polygon.io API key:

```bash
# On Linux/Mac
nano .env

# On Windows
notepad .env
```

Replace the placeholder:
```
POLYGON_API_KEY=your_actual_api_key_here
```

Save and close the file.

### Step 4: Test the Connection

Activate your virtual environment and test:

**Linux/Mac:**
```bash
source venv/bin/activate
python test_connection.py
```

**Windows:**
```bash
venv\Scripts\activate
python test_connection.py
```

You should see:
```
✅ Connection successful!
✓ Retrieved data for: AAPL
✓ Company: Apple Inc.
🎉 All systems ready!
```

### Step 5: Start the Server

```bash
uvicorn main:app --reload --port 10000
```

You should see:
```
INFO:     Uvicorn running on http://127.0.0.1:10000
INFO:     Application startup complete.
```

### Step 6: Verify It's Working

Open your browser and go to:
```
http://localhost:10000/docs
```

You should see the interactive API documentation!

---

## 🔧 Alternative: Manual Setup

If the automated scripts don't work, here's the manual process:

### 1. Create Virtual Environment
```bash
python3 -m venv venv
```

### 2. Activate Virtual Environment
**Linux/Mac:**
```bash
source venv/bin/activate
```

**Windows:**
```bash
venv\Scripts\activate
```

### 3. Upgrade pip
```bash
python -m pip install --upgrade pip
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Create .env File
```bash
cp .env.example .env
```

Then edit `.env` and add your API key.

### 6. Create Directories
```bash
mkdir -p tradepilot_engine/layers
mkdir -p logs
mkdir -p cache
```

### 7. Test & Run
```bash
python test_connection.py
uvicorn main:app --reload --port 10000
```

---

## 🐛 Troubleshooting

### "python3: command not found"
Try `python` instead of `python3`:
```bash
python -m venv venv
```

### "pip: command not found"
Install pip:
```bash
# On Ubuntu/Debian
sudo apt-get install python3-pip

# On macOS
brew install python3
```

### "Permission denied" on setup.sh
Make it executable:
```bash
chmod +x setup.sh
```

### "Module not found" errors
Reinstall dependencies:
```bash
pip install --upgrade -r requirements.txt
```

### Port 10000 already in use
Use a different port:
```bash
uvicorn main:app --reload --port 8000
```

### API key not working
1. Make sure there are no spaces around the `=` in `.env`
2. Verify your key at [Polygon.io Dashboard](https://polygon.io/dashboard)
3. Check for typos in the key

---

## 📊 Testing the Engine

### Test with curl
```bash
# Get signal summary for AAPL
curl "http://localhost:10000/engine/signal-summary?symbol=AAPL"

# Get full analysis
curl "http://localhost:10000/engine/analyze?symbol=AAPL&tf=day&limit=365"

# Test a specific layer
curl "http://localhost:10000/engine/layer/layer_1_momentum?symbol=TSLA"
```

### Test with Python
```python
import requests

# Get signal summary
response = requests.get("http://localhost:10000/engine/signal-summary?symbol=AAPL")
data = response.json()

print(f"Symbol: {data['symbol']}")
print(f"Signal: {data['overall_signal']}")
print(f"Confidence: {data['overall_confidence']}%")
print(f"Recommendation: {data['recommendation']}")
```

### Test in Browser
Go to: `http://localhost:10000/docs`

1. Click on any endpoint
2. Click "Try it out"
3. Enter parameters
4. Click "Execute"
5. See the results!

---

## 🔄 Updating Your Clone

When the repository is updated:

```bash
# Pull latest changes
git pull origin main

# Activate virtual environment
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Update dependencies
pip install --upgrade -r requirements.txt

# Restart server
uvicorn main:app --reload --port 10000
```

---

## 🚢 Deploying Your Clone

### To Render.com (Free)

1. Push your clone to GitHub
2. Go to [render.com](https://render.com)
3. Click "New +" → "Web Service"
4. Connect your GitHub repository
5. Configure:
   - **Name**: tradepilot-mcp-server
   - **Environment**: Python
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port 10000`
6. Add Environment Variable:
   - **Key**: `POLYGON_API_KEY`
   - **Value**: Your actual API key
7. Click "Create Web Service"

Your server will be live at: `https://your-app.onrender.com`

### To Railway.app

```bash
# Install Railway CLI
npm install -g @railway/cli

# Login
railway login

# Initialize
railway init

# Deploy
railway up
```

---

## 📝 Next Steps

After setup is complete:

1. ✅ Read the [README.md](README.md) for detailed documentation
2. ✅ Explore the API at `/docs` endpoint
3. ✅ Integrate with your AI agent or trading bot
4. ✅ Customize layers for your trading strategy
5. ✅ Star the repository if you find it useful! ⭐

---

## 🆘 Still Having Issues?

1. Check the [Troubleshooting](#-troubleshooting) section above
2. Review the [README.md](README.md)
3. Open an issue on GitHub with:
   - Your operating system
   - Python version (`python --version`)
   - Error messages
   - Steps you've tried

---

## ✅ Setup Checklist

Use this to verify everything is working:

- [ ] Python 3.8+ installed
- [ ] Git repository cloned
- [ ] Virtual environment created
- [ ] Dependencies installed
- [ ] `.env` file configured with API key
- [ ] Connection test passed
- [ ] Server starts without errors
- [ ] Can access `/docs` endpoint
- [ ] Can run example API calls
- [ ] Engine returns valid analysis

**All checked?** You're ready to trade! 🚀

---

**Happy Trading!** 📈
