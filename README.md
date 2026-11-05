# PulseTrade Radar - US & Canada Indices & Futures Scalp Tracker

Real-time volatility and momentum radar built for tracking swift movements, scalp setups, and revival surges across major US and Canadian index futures and ETFs (excluding commodities).

## Key Features
- **Coverage**: S&P 500 (ES/SPY), Nasdaq 100 (NQ/QQQ), Dow 30 (YM/DIA), Russell 2000 (RTY/IWM), TSX 60 (SXF/XIU), and Volatility (VIX).
- **Scalp Setups**: Real-time momentum breakouts, revival bounces, and pivot/support/resistance levels.
- **Embedded TradingView Charts**: Live, zero-latency streaming candlesticks.
- **Automated Sync**: Synchronizes every 5 minutes round the clock via Antigravity Scheduled Automation.

## How to Publish to GitHub Pages

1. In your terminal, initialize the repository:
   ```bash
   cd /Users/benjamin/.gemini/antigravity/scratch/market-pulse-tracker
   git init
   git add .
   git commit -m "Initial commit: PulseTrade Radar"
   ```

2. Create a new repository on your GitHub account (named `market-pulse-tracker`), then run:
   ```bash
   git branch -M main
   git remote add origin https://github.com/<YOUR_GITHUB_USERNAME>/market-pulse-tracker.git
   git push -u origin main
   ```

3. Enable GitHub Pages:
   - Go to your repository **Settings** -> **Pages**.
   - Under **Build and deployment**, select `Deploy from a branch`.
   - Choose `main` branch and `/ (root)` folder.
   - Click **Save**. Your site will be live at `https://<YOUR_GITHUB_USERNAME>.github.io/market-pulse-tracker/`.
