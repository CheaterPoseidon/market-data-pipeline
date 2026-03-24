import yfinance as yf
import os

TICKERS = {
    'Tech': ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'META'],
    'Energy': ['XOM', 'CVX', 'COP', 'EOG', 'PSX'],
    'Finance': ['JPM', 'BAC', 'WFC', 'C', 'GS'],
    'Healthcare': ['JNJ', 'PFE', 'MRK', 'ABBV', 'TMO'],
    'Consumer Goods': ['PG', 'KO', 'PEP', 'PM', 'MO']
}

def fetch_stock_data():
    os.makedirs('data', exist_ok=True)
    for sector,tickers in TICKERS.items():
        for ticker in tickers:
            df = yf.download(ticker, period='5y')
            df.to_csv(f'data/{ticker}_data.csv')

if __name__ == '__main__':
    fetch_stock_data()



