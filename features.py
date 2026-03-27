import os
import pandas as pd

def compute_features():
    os.makedirs('data/features', exist_ok=True)
    for filename in os.listdir('data/cleaned/'):
        if filename.endswith('.csv'):
            df=pd.read_csv(f'data/cleaned/{filename}',index_col=0, parse_dates=True)
            df.columns = ['Close', 'High', 'Low', 'Open', 'Volume']
            df['Daily_Return']=df['Close'].pct_change()
            df['20_Day_MA']=df['Close'].rolling(20).mean()
            df['Volatility_20']=df['Daily_Return'].rolling(20).std()
            df.dropna(inplace=True)
            df.to_csv(f'data/features/{filename}')

if __name__ == '__main__':
    compute_features()