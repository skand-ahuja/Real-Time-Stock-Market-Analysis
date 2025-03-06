# Importing Necessary libraries
import pandas as pd
import yfinance as yf

# Fetch the listed stock
stock = "^NSEI"
"""Fetch any stock of our choice"""

# Fetch the historical stock data
stock_data = yf.download(stock, start='2023-01-01', end='2024-01-01')

# Save file to csv
data_path = "data/raw_stock_data.csv" # Location
stock_data.to_csv(data_path)


print(f'Data for {stock} successfully saved to {data_path}!')
