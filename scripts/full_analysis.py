import pandas as pd
import numpy as np
from pathlib import Path
from utils import load_data, calculate_ofi
from visualization import plot_ofi_heatmap
import logging
from datetime import datetime

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def run_full_analysis():
    try:
        # Set paths
        DATA_DIR = Path(__file__).parent.parent / 'data'
        RESULTS_DIR = Path(__file__).parent.parent / 'results'
        RESULTS_DIR.mkdir(exist_ok=True)
        
        # Process all files
        all_stocks_ofi = {}
        files = list(DATA_DIR.glob('xnas-itch-*.csv'))
        
        for file in files:
            logger.info(f"Processing {file.name}")
            df = load_data(file)
            ofi_results = calculate_ofi(df)
            symbol = ofi_results['symbol'].iloc[0]
            all_stocks_ofi[symbol] = ofi_results
            
            # Save individual stock results
            output_file = RESULTS_DIR / f'ofi_results_{symbol}.csv'
            ofi_results.to_csv(output_file, index=False)
            logger.info(f"Saved results for {symbol}")
            
        # Calculate cross-impacts
        logger.info("Calculating cross-impacts...")
        symbols = list(all_stocks_ofi.keys())
        cross_impact_matrix = np.zeros((len(symbols), len(symbols)))
        
        for i, sym1 in enumerate(symbols):
            for j, sym2 in enumerate(symbols):
                corr = all_stocks_ofi[sym1]['ofi_level_0'].corr(all_stocks_ofi[sym2]['ofi_level_0'])
                cross_impact_matrix[i, j] = corr
        
        # Create and save heatmap
        plot_ofi_heatmap(cross_impact_matrix, symbols, 
                        save_path=RESULTS_DIR / 'cross_impact_heatmap.png')
        
        # Save cross-impact matrix
        pd.DataFrame(cross_impact_matrix, 
                    index=symbols, 
                    columns=symbols).to_csv(RESULTS_DIR / 'cross_impact_matrix.csv')
        
        logger.info("Analysis completed successfully")
        return True
        
    except Exception as e:
        logger.error(f"Error in full analysis: {str(e)}")
        return False

if __name__ == "__main__":
    run_full_analysis()
