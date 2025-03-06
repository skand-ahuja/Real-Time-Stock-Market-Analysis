"""
Preprocess raw stock market data by:
    1. Loading raw data from CSV.
    2. Removing incorrect headers (first 2 rows).
    3. Renaming columns correctly.
    4. Converting 'Date' to datetime format.
    5. Converting numerical columns to float.
    6. Handling missing values (dropping if necessary).
    7. Saving the cleaned data for further analysis.
"""

# Import necessary libraries
import pandas as pd
import os

# Define stock symbol (Modify for dynamic input if needed)
stock = "^NSEI"

# Generate file names dynamically based on stock symbol
raw_data_filename = f'raw_{stock.replace("^", "").replace(".", "_")}_data.csv'
processed_data_filename = f'processed_{stock.replace("^", "").replace(".", "_")}_data.csv'

# Define file paths
raw_data_path = os.path.join("data", raw_data_filename)
processed_data_path = os.path.join("data", processed_data_filename)


def preprocess_stock_data(input_file, output_file):
    """
    Cleans and preprocesses stock data.
    
    Parameters:
        input_file (str): Path to raw stock data CSV file.
        output_file (str): Path to save the cleaned stock data CSV file.
    """
    try:
        # Load raw stock data
        stock_data = pd.read_csv(input_file)
        print(f"📂 Loaded data from {raw_data_path} for preprocessing.")

        # Display the first 5 rows before preprocessing
        print("\n🔍 Top 5 rows of raw file: \n", stock_data.head())

        # Remove the first 2 rows (incorrect headers)
        stock_data = stock_data.drop([0, 1])

        # Assign correct column names
        stock_data.columns = ["Date", "Closing_Price", "High", "Low", "Open", "Volume"]

        # Convert 'Date' column to datetime format
        stock_data['Date'] = pd.to_datetime(stock_data['Date'])

        # Convert numeric columns to float type
        for col in ["Closing_Price", "High", "Low", "Open", "Volume"]:
            stock_data[col] = stock_data[col].astype(float)

        # Drop missing values if any
        stock_data.dropna(inplace=True)

        # Save cleaned data to CSV (without index column)
        stock_data.to_csv(output_file, index=False)
        print(f"✅ Processed data successfully saved at: {output_file}")

    except FileNotFoundError:
        print(f"❌ ERROR: File {input_file} not found. Please run `fetch_data.py` first.")

    except Exception as e:
        print(f"⚠️ Unexpected Error Occurred: {e}")


# Run script only when executed directly (not when imported)
if __name__ == "__main__":
    preprocess_stock_data(raw_data_path, processed_data_path)
