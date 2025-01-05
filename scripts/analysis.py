import pandas as pd
import numpy as np
from pathlib import Path
from sklearn.decomposition import PCA
from .utils import load_data, calculate_ofi

def process_stock_data(file_path, sample_size=None):
    '''Process single stock data and calculate OFI'''
    df = load_data(file_path, sample_size)
    return calculate_ofi(df)

def calculate_cross_impact(ofi_data, price_changes):
    '''Calculate cross-impact between stocks'''
    return np.corrcoef(ofi_data.T)

def main():
    DATA_DIR = Path(__file__).parent.parent / 'data'
    files = list(DATA_DIR.glob('xnas-itch-*.csv'))
    
    # Process each stock
    all_ofi = {}
    for file in files:
        stock_ofi = process_stock_data(file)
        symbol = stock_ofi['symbol'].iloc[0]
        all_ofi[symbol] = stock_ofi

if __name__ == "__main__":
    main()
