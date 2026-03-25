import os
import pandas as pd

def clean_data():
    os.makedirs('data/cleaned', exist_ok=True)
    for filename in os.listdir('data/'):
        if filename.endswith('.csv'):
            df=pd.read_csv(f'data/{filename}',header=2, index_col=0)
            df=df.dropna()
            df.sort_index(inplace=True)
            df.to_csv(f'data/cleaned/{filename}')


if __name__ == '__main__':
    clean_data()