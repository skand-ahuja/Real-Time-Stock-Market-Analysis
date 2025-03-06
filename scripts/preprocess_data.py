"""
Function to clean and preprocess stock market data.

Steps:
    1. Load raw data from CSV.
    2. Remove incorrect headers (first 3 rows).
    3. Rename columns correctly.
    4. Convert 'Date' to datetime format.
    5. Convert numerical columns to float.
    6. Handle missing values (drop if necessary).
    7. Save the cleaned data.
"""

# Importing necessary Libraries:
import pandas as pd
import os

# File name of raw & preprocessed data:
# stock = input("Enter stock name: ")
stock = "^NSEI"
raw_data_filename = f'raw_{stock.replace("^", "").replace(".", "_")}_data.csv'
processed_data_filename = f'processed_{stock.replace("^", "").replace(".", "_")}_data.csv'

# Define file paths:
raw_data_path = os.path.join("data", raw_data_filename)
processed_data_path = os.path.join("data", processed_data_filename)


def preprocess_stock_data(input_file, output_file):
    try:
        # Creating pandas dataframe for analysis
        stock_data = pd.read_csv(input_file)
        print(f'Loaded data from {raw_data_path} for preprocessing.')

        # Top 5 rows of csv file:
        print("\nTop 5 rows of raw file: \n", stock_data.head())

        # Drop the first 2 rows (headers)
        stock_data = stock_data.drop([0, 1])

        # Reset the index without adding a new index column
        # stock_data.reset_index(drop=True, inplace=True)
        
        # Add new header row
        stock_data.columns = ["Date", "Closing_Price", "High", "Low", "Open", "Volume"]

        # Convert columns datatype to the correct datatype
        stock_data['Date'] = pd.to_datetime(stock_data['Date'])
        stock_data['Closing_Price'] = stock_data['Closing_Price'].astype(float)
        stock_data['High'] = stock_data['High'].astype(float)
        stock_data['Low'] = stock_data['Low'].astype(float)
        stock_data['Open'] = stock_data['Open'].astype(float)
        stock_data['Volume'] = stock_data['Volume'].astype(float)

        # Drop missing values:
        stock_data.dropna(inplace=True)

        # Save processed data to directory:
        stock_data.to_csv(output_file, index=False)
        print(f'Processed data saved at {output_file}.')

    except FileNotFoundError:
        print(f'ERROR: File {input_file} not found. Please run `fetch_data.py` first.')

    except Exception as e:
        print(f"Unexpected Error Occured: {e}")

# Run the script only if executed directly
if __name__ == "__main__":
    preprocess_stock_data(raw_data_path, processed_data_path)