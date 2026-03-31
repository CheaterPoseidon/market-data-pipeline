import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from fetch_data import TICKERS

def plot_volatility():
    sector_volatility={}
    for sector,tickers in TICKERS.items():
        vol_values=[]
        for ticker in tickers:
            df= pd.read_csv(f'data/features/{ticker}_data.csv', index_col=0, parse_dates=True)
            vol_values.append(df['Volatility_20'].mean())
        sector_volatility[sector]=pd.Series(vol_values).mean()
    
    sns.set_theme()
    plt.figure(figsize=(10, 6))
    plt.bar(sector_volatility.keys(), sector_volatility.values())
    plt.title('Average 20-Day Volatility by Sector')
    plt.ylabel('Volatility')
    plt.tight_layout()
    plt.savefig('data/volatility_by_sector.png')
    plt.close()

def plot_cumulative_returns():
    sns.set_theme()
    plt.figure(figsize=(12, 6))
    for sector,tickers in TICKERS.items():
        returns_df=pd.DataFrame()
        for ticker in tickers:
            df= pd.read_csv(f'data/features/{ticker}_data.csv', index_col=0, parse_dates=True)
            returns_df[ticker]=df['Daily_Return']
        avg_returns = returns_df.mean(axis=1)
        cumulative = (1 + avg_returns).cumprod()
        plt.plot(cumulative.index, cumulative.values, label=sector)

    plt.title('Cumulative Returns by Sector')
    plt.ylabel('Growth of $1')
    plt.legend()
    plt.tight_layout()
    plt.savefig('data/cumulative_returns.png')
    plt.close()

if __name__=='__main__':
    plot_volatility()
    plot_cumulative_returns()