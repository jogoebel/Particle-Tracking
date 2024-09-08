import numpy as np
import matplotlib.pyplot as plt

def compare_ecdf(TARDIS_df, PYTHON_df, max_dt, log_scale=False):
    """tardis_df, python_df, max_dt, log"""
    
    plt.figure(figsize=(10, 8))
    
    for i in range(max_dt):
        col_name = f'dT = {i + 1}'

        subset_TARDIS = np.sort(TARDIS_df[col_name])
        subset_PYTHON = np.sort(PYTHON_df[col_name])
        
        # Calculate ECDF values for TARDIS subset
        y_vals_TARDIS = np.arange(1, len(subset_TARDIS) + 1) / len(subset_TARDIS)
        plt.plot(subset_TARDIS, y_vals_TARDIS, marker='.', linestyle='none', label=f'TARDIS dt={i + 1}')
        
        # Calculate ECDF values for PYTHON subset
        y_vals_PYTHON = np.arange(1, len(subset_PYTHON) + 1) / len(subset_PYTHON)
        plt.plot(subset_PYTHON, y_vals_PYTHON, marker='.', linestyle='none', label=f'PYTHON dt={i + 1}')
        
        plt.xlabel('Displacement (nm)')
        plt.ylabel('ECDF')
        plt.title('Combined ECDFs for Different Frame Intervals')
        plt.legend(title='Dataset and Frame Interval (dt)', bbox_to_anchor=(1.05, 1), loc='upper left')
        
        if log_scale:
            plt.xscale('log')  # Optionally set x-axis to logarithmic scale
        
        plt.tight_layout()
    
    return plt.show()

