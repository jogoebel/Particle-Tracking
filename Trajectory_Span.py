import pandas as pd
import numpy as np

def calculate_trajectory_span(file_path):

    largest_span = 0  # Largest difference in frames for any trajectory
    
    particle_data = pd.read_csv(file_path)
     
    for trajectory in np.unique(particle_data['traj_idx']):  # Iterate through each unique trajectory
        particle_traj = particle_data[particle_data['traj_idx'] == trajectory]  # boolean selector

        frame_numbers = np.array(particle_traj['t'])
        traj_span = frame_numbers.max() - frame_numbers.min()
        largest_span = max(largest_span, traj_span)  # Update largest span if current one is larger
        
    return largest_span
    
