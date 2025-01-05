import pandas as pd
import numpy as np
from pathlib import Path
from utils import load_data, calculate_ofi
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def test_pipeline():
    try:
        # Set paths
        DATA_DIR = Path(__file__).parent.parent / 'data'
        
        # Test with TSLA data first
        test_file = DATA_DIR / 'xnas-itch-tsla-20241219.mbp-10.csv'
        
        # Load first 1000 rows
        logger.info("Loading test data...")
        df = load_data(test_file, sample_size=1000)
        
        # Calculate OFI
        logger.info("Calculating OFI...")
        ofi_results = calculate_ofi(df)
        
        # Basic statistics
        logger.info("\nOFI Statistics:")
        print(ofi_results.describe())
        
        return True
        
    except Exception as e:
        logger.error(f"Error in test pipeline: {str(e)}")
        return False

if __name__ == "__main__":
    test_pipeline()