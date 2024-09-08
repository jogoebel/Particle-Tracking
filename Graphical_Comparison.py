import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
def histogram_plotting(TARDIS_df, PYTHON_df, log_scale=False):
    df1 = TARDIS_df
    df2 = PYTHON_df
    max_dt = len(df1.columns)
    n_cols = int(np.ceil(np.sqrt(max_dt)))
    n_rows = int(np.ceil(max_dt / n_cols))
    
    fig, axs = plt.subplots(n_rows, n_cols, figsize=(5 * n_cols, 4 * n_rows))
    axs = axs.flatten()
    
    for i, col_name in enumerate(df1.columns):
        min_val = min(df1[col_name].min(), df2[col_name].min())
        max_val = max(df1[col_name].max(), df2[col_name].max())
        bins = np.linspace(min_val, max_val, 20)
        
        axs[i].hist(df1[col_name], bins=bins, alpha=0.5, label='TARDIS', edgecolor='black', density=True)
        axs[i].hist(df2[col_name], bins=bins, alpha=0.5, label='PYTHON', edgecolor='black', density=True)
        
        axs[i].set_xlabel('Displacement (nm)')
        axs[i].set_ylabel('Probability Density')
        axs[i].set_title(f'Jump Distances for {col_name}')
        axs[i].legend(loc='upper right')
        
        if log_scale:
            axs[i].set_yscale('log')
    
    plt.tight_layout()
    return plt.show()
