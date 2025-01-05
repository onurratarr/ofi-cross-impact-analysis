# Order Flow Imbalance (OFI) Cross-Impact Analysis

This project evaluates the cross-impact of Order Flow Imbalance (OFI) on short-term price changes across highly liquid Nasdaq stocks. It involves computing OFI metrics, analyzing cross-impact relationships, and generating visualizations for insights.

## Project Structure
- **data/**: Contains placeholder datasets representing the format of original data.
- **notebooks/**: Includes Jupyter Notebook for exploratory analysis and methodology.
- **scripts/**: Python scripts for data processing, analysis, and visualization.
- **results/**: Stores output files, figures, and analysis results.

## Data Description
Working with high-frequency data for 4 Nasdaq stocks:
- BKR (Baker Hughes)
- NVDA (NVIDIA)
- MARA (Marathon Digital)
- TSLA (Tesla)

## How to Run the Code
1. **Set up the environment**:
   - Install Python 3.8 or higher.
   - Clone the repository: 
     ```
     git clone https://github.com/onurratarr/ofi-cross-impact-analysis.git
     cd ofi-cross-impact-analysis
     ```
   - Install the dependencies:
     ```
     pip install -r requirements.txt
     ```

2. **Execute the scripts**:
   - Preprocess data and calculate OFI metrics:
     ```
     python scripts/calculate_ofi.py
     ```
   - Perform PCA and cross-impact analysis:
     ```
     python scripts/full_analysis.py
     ```
   - Generate visualizations:
     ```
     python scripts/visualization.py
     ```

3. **Review the results**:
   - Outputs, including OFI metrics, PCA results, and visualizations, will be saved in the `results/` directory.

Summary of the Findings
OFI Metrics:

Successfully computed for four stocks: BKR, NVDA, MARA, and TSLA.
PCA reduced multi-level metrics into components, capturing ~85% variance in the first two components.
Cross-Impact Relationships:

NVDA showed the strongest contemporaneous impact on other stocks.
Significant relationships observed across all analyzed stocks.
Lagged Impact Analysis:

Moderate predictive power found for lagged OFI on price changes, with 1-minute and 5-minute horizons showing autocorrelations.
Visualizations:

Generated heatmaps, time-series plots, and boxplots to illustrate findings.
## References
- Cont, R., & Kukanov, A. (2017). Cross-Impact of Order Flow in Equity Markets.
- Databento Documentation: [https://databento.com/docs](https://databento.com/docs)





