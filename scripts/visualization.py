import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def plot_ofi_heatmap(cross_impact_matrix, symbols, save_path=None):
    '''Create heatmap of cross-impact relationships'''
    plt.figure(figsize=(10, 8))
    sns.heatmap(cross_impact_matrix, 
                xticklabels=symbols,
                yticklabels=symbols,
                cmap='coolwarm',
                center=0)
    plt.title('Cross-Impact of OFI Between Stocks')
    if save_path:
        plt.savefig(save_path)
    plt.close()
