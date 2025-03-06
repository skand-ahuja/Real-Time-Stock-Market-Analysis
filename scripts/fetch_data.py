# Importing Necessary libraries
import pandas as pd
import yfinance as yf

# Fetch the listed stock
# Testing
stock = "^NSEI"
from_date = '2023-01-01'
to_date = '2024-01-01'
interval = '1d'

# Uncomment for Dynamic User Input:
"""
stock = input("Enter Stock Name: ")
from_date = input("From Data: ")
to_date = input("To Date: ")
interval = input("Interval (1d/ 5d/ 1m/ 6m/ 1y/ 5y): ")
"""

# Define File path (Dynamically Naming the File Based on Stock Symbol):
data_path = f"data/raw_{stock.replace('^',"").replace(".", "_")}_data.csv" # Location to store

# Fetch the historical stock data
try:
    print(f"📡 Fetching stock data for {stock} from {from_date} to {to_date}")

    # fetch data:
    stock_data = yf.download(stock, start=from_date, end=to_date, interval=interval)

    print(f'Data for {stock} successfully saved to {data_path}!')

    # Check if data is empty:
    if stock_data.empty:
        raise ValueError(f"❌ No data found for stock: {stock}. Check the symbol or API availability.")
    
    # Save file to csv
    stock_data.to_csv(data_path)

except ValueError as ve:
    print(f'Error: {ve}')

except Exception as e:
    print(f'An unexpected error occured, error code: {e}')