import pandas as pd
import numpy as np
from pathlib import Path

def calculate_ofi(df, level=5):
    '''
    Calculate Order Flow Imbalance for given order book data
    Parameters:
    - df: DataFrame with order book data
    - level: Number of price levels to consider (default=5)
    '''
    ofi_levels = []
    
    for i in range(level):
        # Calculate OFI for each level
        bid_size = df[f'bid_sz_{i:02d}']
        ask_size = df[f'ask_sz_{i:02d}']
        
        # Basic OFI calculation: bid size - ask size
        ofi = bid_size - ask_size
        ofi_levels.append(ofi)
    
    return pd.DataFrame({
        'ts_event': df['ts_event'],
        'symbol': df['symbol'],
        **{f'ofi_level_{i}': ofi_levels[i] for i in range(level)}
    })

# Example usage
if __name__ == "__main__":
    DATA_DIR = Path(__file__).parent.parent / 'data'
    # Process first 1000 rows as a test
    df = pd.read_csv(DATA_DIR / 'xnas-itch-tsla-20241219.mbp-10.csv', nrows=1000)
    ofi_result = calculate_ofi(df)
    print(ofi_result.head())
