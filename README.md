# Market Data Analytics Pipeline

A modular Python pipeline that ingests historical equity data, cleans it, engineers financial features, and produces sector comparison visualizations.

## Overview

This project pulls 5 years of daily price data for 25 stocks across 5 sectors using the Yahoo Finance API, processes it through a multi-stage pipeline, and outputs charts comparing sector-level volatility and cumulative returns.

## Pipeline Stages

| File | Description |
|------|-------------|
| `fetch_data.py` | Downloads historical OHLCV data for 25 tickers via yfinance |
| `clean_data.py` | Handles missing values, sets date index, sorts chronologically |
| `features.py` | Engineers daily returns, 20-day moving average, and 20-day volatility |
| `visualize.py` | Generates bar and line charts comparing sectors |
| `main.py` | Runs the full pipeline end to end |

## Sectors & Tickers

- **Tech**: AAPL, MSFT, GOOGL, AMZN, META
- **Energy**: XOM, CVX, COP, EOG, PSX
- **Finance**: JPM, BAC, WFC, C, GS
- **Healthcare**: JNJ, PFE, MRK, ABBV, TMO
- **Consumer Goods**: PG, KO, PEP, PM, MO

## How to Run

1. Install dependencies: pip install yfinance pandas matplotlib seaborn
2. Run the pipeline: python3 main.py

Output charts will be saved to `data/`.

## Tech Stack

Python, pandas, yfinance, matplotlib, seaborn
