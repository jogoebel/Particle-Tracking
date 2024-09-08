import numpy as np
import matplotlib.pyplot as plt
import json
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, ConstantKernel as C

def probability_densities(TARDIS_df, PYTHON_df, max_dt, log_scale, save_results):
    """TARDIS_df, PYTHON_df, max_dt, log_scale=False, save_results=False"""
    
    results = {}
    density_ratios = {}
    
    for i in range(1, max_dt + 1):
        col_name = f'dT = {i}'
       
        min_val = min(TARDIS_df[col_name].min(), PYTHON_df[col_name].min())
        max_val = max(TARDIS_df[col_name].max(), PYTHON_df[col_name].max())
        bins = np.arange(min_val, max_val + 15, 15)
        
        tardis_hist, bin_edges = np.histogram(TARDIS_df[col_name], bins=bins, density=True)
        python_hist, _ = np.histogram(PYTHON_df[col_name], bins=bins, density=True)
        
        
        ratio = np.nan_to_num(python_hist / tardis_hist, nan=0.0, posinf=0.0, neginf=0.0)
        bin_midpoints = (bin_edges[:-1] + bin_edges[1:]) / 2
        
        ##Gausian Filter Test
        kernel = C(1.0, (1e-4, 1e1)) * RBF(1.0, (1e-4, 1e1))
        gp = GaussianProcessRegressor(kernel=kernel, n_restarts_optimizer=10)
        gp.fit(bin_midpoints[:, np.newaxis], ratio)
        xfit = np.linspace(0, 10, 1000)
        yfit, MSE = gp.predict(xfit[:, np.newaxis], return_std=True)
        dyfit = 2 * MSE  # 2*sigma ~ 95% confidence region
        
        plt.figure(figsize=(8, 5))
        plt.plot(bin_midpoints, ratio, label=f'PYTHON/TARDIS Ratio for {col_name}')
        plt.fill_between(xfit, yfit - dyfit, yfit + dyfit, color='gray', alpha=0.2)
        plt.plot(xfit, yfit, '-', color='gray')
        plt.xlabel('Displacement (nm)')
        plt.ylabel('Density Ratio (PYTHON / TARDIS)')
        plt.title(f'Density Ratio for {col_name}')
        plt.legend()
        
        if log_scale == True:
            plt.yscale('log')
        
        plt.show()

        # Saving the data
        results[col_name] = {'bins': bin_edges, 'tardis_hist': tardis_hist, 'python_hist': python_hist}
        density_ratios[col_name] = {'bin_midpoints': bin_midpoints, 'density_ratio': ratio}
    
    if save_results == True:
        with open('density_ratio_analysis_results.json', 'w') as f:
            json.dump({'results': results, 'density_ratios': density_ratios}, f, indent=4)
    
    return results, density_ratios
