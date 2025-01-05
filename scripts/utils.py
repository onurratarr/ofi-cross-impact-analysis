import pandas as pd
import numpy as np
from pathlib import Path

def load_data(file_path, sample_size=None):
    '''Load and preprocess order book data'''
    df = pd.read_csv(file_path, nrows=sample_size)
    df['ts_event'] = pd.to_datetime(df['ts_event'])
    return df.sort_values('ts_event')

def calculate_ofi(df, level=5):
    '''Calculate OFI metrics for multiple levels'''
    ofi_levels = []
    for i in range(level):
        bid_size = df[f'bid_sz_{i:02d}']
        ask_size = df[f'ask_sz_{i:02d}']
        ofi = bid_size - ask_size
        ofi_levels.append(ofi)
    
    return pd.DataFrame({
        'ts_event': df['ts_event'],
        'symbol': df['symbol'],
        **{f'ofi_level_{i}': ofi_levels[i] for i in range(level)}
    })
