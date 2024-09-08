import pandas as pd
import numpy as np

def legant_compatible_TARDIS(input_file,output_file,dim):
    """Input file path, output file path, dimensions"""
    particle_data = pd.read_csv(input_file)
    if dim == 2:
        particle_data['z [nm]'] = 0
    elif dim != 3:
        raise ValueError("dim argument must be either 2 or 3.")
    thunderstorm_data = particle_data[['traj_idx','t','x [nm]', 'y [nm]', 'z [nm]']].copy()
    thunderstorm_data.columns = ['id','frame','x [nm]', 'y [nm]', 'z [nm]'] 
    # Save the filtered data to a CSV file
    thunderstorm_data.fillna(np.nan, inplace=True)
    print(f'Done. The data was saved to {output_file}')
    # Save the processed data to a CSV file, specifying na_rep if you want 'NaN' in the CSV
    return thunderstorm_data.to_csv(output_file, index=False, na_rep='NaN')
