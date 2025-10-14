# 🚀 TradePilot MCP Server v2.0

**Advanced Multi-Layer Trading Intelligence Engine**

A production-grade MCP (Model Context Protocol) server that combines **Polygon.io real-time market data** with a **10-layer technical analysis engine** for autonomous trading intelligence. Designed for easy local setup and GitHub deployment.

---

## 📊 What is This?

TradePilot is a **FastAPI-based MCP server** that:
- Fetches real-time and historical market data from Polygon.io
- Runs analysis through **10 specialized technical indicator layers**
- Provides structured JSON outputs perfect for AI/GPT integration
- Delivers actionable trading signals with confidence scores

Think of it as your **AI trading copilot** that handles all the heavy technical analysis and data fetching, so you (or your AI agent) can focus on decision-making.

---

## 🎯 10-Layer Analysis Engine

| Layer | Focus | Key Indicators |
|-------|-------|---------------|
| **1** | **Momentum** | RSI, MACD, Stochastic, CMF, ADX, Ichimoku |
| **2** | **Volume** | OBV, A/D Line, CMF, Volume Divergence |
| **3** | **Divergence** | Delta Divergence, CDV Analysis |
| **4** | **Volume Strength** | RVOL, Volume Spikes, Buy/Sell Pressure |
| **5** | **Trend** | SuperTrend, ADX/DMI, Moving Averages, Channels |
| **6** | **Market Structure** | CHoCH, BOS, Order Blocks, FVG |
| **7** | **Liquidity** | Liquidity Sweeps, Hunt Detection |
| **8** | **Volatility Regime** | ATR Percentiles, Regime Classification |
| **9** | **Confirmation** | Multi-Timeframe Alignment |
| **10** | **Candle Intelligence** | Pattern Recognition, Candle Scoring |

Each layer produces a **signal** (BUY/SELL/NEUTRAL) with a **confidence score**, which are combined into an **overall recommendation**.

---

## 🚀 Quick Start (Local Setup)

### Prerequisites
- **Python 3.8+**
- **Polygon.io API Key** ([Get one free](https://polygon.io/))

### Option 1: Automated Setup (Recommended)

**On Linux/Mac:**
```bash
# Clone the repository
git clone <your-repo-url>
cd tradepilot-mcp-server

# Make setup script executable
chmod +x setup.sh

# Run setup
./setup.sh

# Activate environment
source venv/bin/activate

# Edit .env and add your API key
nano .env
# Change: POLYGON_API_KEY=your_polygon_api_key_here

# Test connection
python test_connection.py

# Start the server
uvicorn main:app --reload --port 10000
```

**On Windows:**
```bash
# Clone the repository
git clone <your-repo-url>
cd tradepilot-mcp-server

# Run setup
setup.bat

# Edit .env and add your API key
notepad .env
# Change: POLYGON_API_KEY=your_polygon_api_key_here

# Activate environment
venv\Scripts\activate

# Test connection
python test_connection.py

# Start the server
uvicorn main:app --reload --port 10000
```

### Option 2: Manual Setup

```bash
# Clone repository
git clone <your-repo-url>
cd tradepilot-mcp-server

# Create virtual environment
python3 -m venv venv

# Activate (Linux/Mac)
source venv/bin/activate
# Or on Windows:
# venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
echo "POLYGON_API_KEY=your_key_here" > .env

# Test connection
python test_connection.py

# Start server
uvicorn main:app --reload --port 10000
```

---

## 📡 API Endpoints

### 🏠 Core Endpoints
- `GET /` - Server status
- `GET /docs` - Interactive API documentation
- `GET /engine/health` - Engine health check

### 🔍 Market Data Endpoints
- `GET /symbol-lookup?query=apple` - Search for tickers
- `GET /candles?symbol=AAPL&tf=day&limit=730` - Get OHLCV data
- `GET /news?symbol=AAPL` - Latest news
- `GET /ticker-details?symbol=AAPL` - Company information
- `GET /last-trade?symbol=AAPL` - Latest trade data

### ⚙️ TradePilot Engine Endpoints

#### Complete Analysis
```bash
GET /engine/analyze?symbol=AAPL&tf=day&limit=730
```
Returns full analysis from all 10 layers with detailed metrics and signals.

#### Quick Signal Summary
```bash
GET /engine/signal-summary?symbol=AAPL
```
Returns condensed decision-making data:
```json
{
  "symbol": "AAPL",
  "latest_price": 150.25,
  "momentum_bias": "BULLISH",
  "momentum_score": 67.5,
  "trend_direction": "BULLISH",
  "trend_strength": 42.3,
  "volume_flow": 45.2,
  "volatility_regime": "NORMAL",
  "overall_signal": "BULLISH",
  "overall_confidence": 72.4,
  "recommendation": "BUY"
}
```

#### Single Layer Analysis
```bash
GET /engine/layer/layer_1_momentum?symbol=AAPL
```

#### List Available Layers
```bash
GET /engine/layers
```

---

## 🧠 Using with ChatGPT / Claude / AI Agents

### Step 1: Start the Server
```bash
uvicorn main:app --host 0.0.0.0 --port 10000
```

### Step 2: Configure MCP in Your AI Tool

**For ChatGPT (Custom GPT):**
1. Create a Custom GPT
2. Add Action: `http://localhost:10000/openapi.json`
3. Your GPT can now call TradePilot endpoints!

**For Claude (MCP Protocol):**
1. Add server to your MCP config
2. Point to: `http://localhost:10000`

**For LangChain / AutoGPT:**
```python
from langchain.tools import Tool

tradepilot_tool = Tool(
    name="TradePilot Analysis",
    func=lambda symbol: requests.get(
        f"http://localhost:10000/engine/signal-summary?symbol={symbol}"
    ).json(),
    description="Get comprehensive trading signal analysis"
)
```

### Step 3: Example Prompts

**To GPT:**
> "Use TradePilot to analyze AAPL and tell me if I should buy, sell, or hold based on the current technical picture."

> "Compare the momentum and volume signals for TSLA and NVDA using TradePilot, then recommend which looks better for a swing trade."

> "What's the volatility regime for SPY according to TradePilot Layer 8?"

---

## 📂 Project Structure

```
tradepilot-mcp-server/
├── main.py                          # FastAPI server
├── engine_router.py                 # Engine API routes
├── polygon_client.py                # Polygon.io data fetcher
├── test_connection.py               # Connection test script
├── setup.sh / setup.bat             # Auto-setup scripts
├── requirements.txt                 # Dependencies
├── .env                             # API keys (create this)
├── README.md                        # This file
│
├── tradepilot_engine/               # Core engine package
│   ├── __init__.py
│   ├── engine_core.py               # Main orchestrator
│   ├── data_processor.py            # Data conversion
│   │
│   └── layers/                      # 10 analysis layers
│       ├── __init__.py
│       ├── layer_1_momentum.py
│       ├── layer_2_volume.py
│       ├── layer_3_divergence.py
│       ├── layer_4_volume_strength.py
│       ├── layer_5_trend.py
│       ├── layer_6_structure.py
│       ├── layer_7_liquidity.py
│       ├── layer_8_volatility_regime.py
│       ├── layer_9_confirmation.py
│       └── layer_10_candle_intelligence.py
```

---

## 🔧 Configuration

### Environment Variables (.env)
```bash
POLYGON_API_KEY=your_key_here
PORT=10000
```

### Polygon.io Rate Limits
- **Free Tier**: 5 API calls/minute
- **Starter**: 100 calls/minute
- **Developer**: 1000 calls/minute

The server caches data intelligently to minimize API calls.

---

## 🧪 Testing

### Test Polygon Connection
```bash
python test_connection.py
```

### Test Engine Analysis
```bash
curl "http://localhost:10000/engine/signal-summary?symbol=AAPL"
```

### Interactive API Docs
Open: `http://localhost:10000/docs`

---

## 🐛 Troubleshooting

### "Unable to fetch candle data"
- Check your Polygon.io API key
- Verify the symbol is correct
- Check if market is open (for recent data)

### "Insufficient data" error
- Increase `limit` parameter (default 730 days)
- Check if the symbol has trading history

### Import errors
```bash
pip install --upgrade -r requirements.txt
```

### Server won't start
```bash
# Check if port is in use
lsof -i :10000

# Use different port
uvicorn main:app --port 8000
```

---

## 📈 Example Use Cases

### 1. Daily Stock Screener
```python
import requests

symbols = ["AAPL", "MSFT", "GOOGL", "TSLA"]
results = []

for symbol in symbols:
    response = requests.get(f"http://localhost:10000/engine/signal-summary?symbol={symbol}")
    data = response.json()
    
    if data["overall_confidence"] > 70 and data["overall_signal"] == "BULLISH":
        results.append(symbol)

print(f"Strong buy signals: {results}")
```

### 2. Automated Trading Alerts
```python
symbol = "SPY"
response = requests.get(f"http://localhost:10000/engine/analyze?symbol={symbol}")
analysis = response.json()

if analysis["overall_signal"]["recommendation"] == "STRONG BUY":
    send_alert(f"🚀 Strong buy signal on {symbol}!")
```

### 3. AI Trading Assistant
Integrate with your AI agent to provide real-time analysis and trading recommendations based on multi-layer technical analysis.

---

## 🚢 Deployment

### Deploy to Render.com (Free)
1. Push this repo to GitHub
2. Go to [render.com](https://render.com)
3. New → Web Service
4. Connect GitHub repo
5. Add environment variable: `POLYGON_API_KEY`
6. Deploy!

### Deploy to Railway.app
```bash
railway init
railway add
railway up
```

### Deploy to Heroku
```bash
heroku create tradepilot-mcp
heroku config:set POLYGON_API_KEY=your_key
git push heroku main
```

---

## 🤝 Contributing

Contributions welcome! To add new layers or improve existing ones:

1. Fork the repository
2. Create your feature branch
3. Add your layer in `tradepilot_engine/layers/`
4. Update `engine_core.py` to include your layer
5. Submit a pull request

---

## 📄 License

MIT License - Feel free to use this for personal or commercial projects

---

## 🙏 Credits

- **Polygon.io** for market data
- **FastAPI** for the web framework
- **TradingView** for indicator inspiration
- Built with ❤️ for traders and AI developers

---

## 📞 Support

- **Issues**: [GitHub Issues]
- **Discussions**: [GitHub Discussions]
- **Documentation**: `/docs` endpoint

---

**Ready to trade smarter?** 🚀

Start the server and let TradePilot handle the technical analysis while you focus on making profitable decisions!

```bash
uvicorn main:app --reload --port 10000
```

Then visit: `http://localhost:10000/docs`
