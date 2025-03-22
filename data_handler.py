import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
import time

def get_stock_data(tickers, start_date, end_date, max_retries=3):
    """Download stock data for the given tickers and date range with retry logic."""
    for attempt in range(max_retries):
        try:
            # Download data
            data = yf.download(tickers, start=start_date, end=end_date, auto_adjust=True)
            
            # Check if data is not empty
            if not data.empty:
                # If 'Adj Close' column exists, use it
                if 'Adj Close' in data.columns:
                    price_data = data['Adj Close']
                # If not, use 'Close' column
                elif 'Close' in data.columns:
                    price_data = data['Close']
                # Handle case when the data has a MultiIndex with 'Close' as a level
                elif isinstance(data.columns, pd.MultiIndex) and 'Close' in data.columns.levels[0]:
                    price_data = data['Close']
                # Finally, try to get Adj Close as a level in MultiIndex
                elif isinstance(data.columns, pd.MultiIndex) and 'Adj Close' in data.columns.levels[0]:
                    price_data = data['Adj Close']
                else:
                    # If neither Close nor Adj Close is available, use the first column
                    price_data = data.iloc[:, 0]
                    print(f"Warning: Using {data.columns[0]} as price data. Available columns: {data.columns}")
                
                # If we have a Series (single ticker), convert to DataFrame
                if isinstance(price_data, pd.Series):
                    price_data = pd.DataFrame({tickers[0]: price_data})
                
                return price_data
            else:
                print(f"Attempt {attempt+1}: No data retrieved. Retrying...")
                time.sleep(2)  # Wait before retrying
        except Exception as e:
            print(f"Attempt {attempt+1}: Error downloading data: {e}")
            print(f"Available columns: {data.columns if 'data' in locals() and not data.empty else 'None'}")
            time.sleep(2)  # Wait before retrying
    
    # If we've reached here, all attempts failed
    raise ValueError("Failed to download stock data after multiple attempts. Please check your internet connection and ticker symbols.")

def calculate_returns(prices):
    """Calculate daily returns from price data."""
    # Explicitly specify fill_method=None to avoid the warning
    return prices.pct_change(fill_method=None).dropna()

def get_default_dates():
    """Get default date range (last 3 years)."""
    end_date = datetime.now()
    start_date = end_date - timedelta(days=365*3)
    return start_date, end_date