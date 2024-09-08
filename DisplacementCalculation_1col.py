import pandas as pd
import numpy as np

def calculate_displacement(max_dt,dim,file_path):
    """max_dt --> max frame step, dim --> 2D or 3D displacement, file_path --> file location"""
    
    disp_lst = [] #displacement values
    dt_lst = [] #time interval
    
    particle_data = pd.read_csv(file_path)
     
    for trajectory in np.unique(particle_data['traj_idx']): # Iterate through each unique trajectory
        particle_traj = particle_data[particle_data['traj_idx'] == trajectory] #boolean selector

        xarr = np.array(particle_traj['x [nm]']) #x,y,z for p trajectory in each frame
        yarr = np.array(particle_traj['y [nm]'])
        zarr = np.array(particle_traj['z [nm]'])
    
        for dt in range(1, max_dt + 1): #1-5 inclusive
            xlocs0 = xarr[:-dt]
            xlocs1 = xarr[dt:]  #dt frames ahead
            ylocs0 = yarr[:-dt]
            ylocs1 = yarr[dt:]  #dt frames ahead
            zlocs0 = zarr[:-dt] 
            zlocs1 = zarr[dt:]  #dt frames ahead
            
            if dim == 2:
                displacement = np.sqrt((xlocs1-xlocs0)**2 + (ylocs1-ylocs0)**2)
            elif dim == 3:
                displacement = np.sqrt((xlocs1-xlocs0)**2 + (ylocs1-ylocs0)**2 + (zlocs1-zlocs0)**2)
            else:
                return "Please enter a valid Dimension"
            
            disp_lst.extend (displacement)
            dt_lst. extend ([dt] * len(displacement)) ##Displacement is in nm
    
    return pd.DataFrame({'dt': dt_lst, 'displacement': disp_lst})
