import numpy as np
import pandas as pd
def maximum_uncertainty(file_path,dim):
    particle_data = pd.read_csv(file_path)
    if dim == 2:
        max_unc = particle_data['xy_pstd'].max()
    elif dim == 3:
        uncertainties = [particle_data['xy_pstd'].max(),particle_data['z_pstd'].max()]
        max_unc = max(uncertainties)
    else:
        print('please enter a valid dimension')
    return max_unc
