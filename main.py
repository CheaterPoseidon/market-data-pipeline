from fetch_data import fetch_stock_data
from clean_data import clean_data
from features import compute_features
from visualize import plot_volatility, plot_cumulative_returns

if __name__ == '__main__':
    print("Fetching Stock Data...")
    fetch_stock_data()

    print("Cleaning Data...")
    clean_data()

    print("Calculating Metrics...")
    compute_features()

    print("Generating Visualizations...")
    plot_volatility()
    plot_cumulative_returns()

    print("Done!")