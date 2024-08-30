# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 09:28:31 2024

@author: A127895
"""

import numpy as np
import os

# Specify the directory path
root_dir = r'C:\Users\A127895\Desktop\8. Python\2024.07.29 - TSM data collector\raw data\LEG1\125C24H_24020133LEG1'

# Specify the letter to search for in folder names
target_letter = 'A'

# Get a list of all folders in the root directory that contain the target letter
folders = [f for f in os.listdir(root_dir) if os.path.isdir(os.path.join(root_dir, f)) and target_letter in f]

# Loop through each folder
for folder in folders:
    folder_path = os.path.join(root_dir, folder)
    print(f"Processing folder: {folder}")
    
    # Get a list of all .dat files in the folder
    dat_files = [f for f in os.listdir(folder_path) if f.endswith('.dat')]
    
    # Loop through each .dat file
    for file in dat_files:
        file_path = os.path.join(folder_path, file)
        print(f"Processing file: {file}")
        
        # Load the data from the .dat file
        warpagedata = np.loadtxt(file_path)
        data  = warpagedata.tolist()
        
        # finding the maximum and 
        # minimum element in the array
        max_element = np.max(data)
        min_element = np.min(data)
        median_element = np.median(data)
        std_dev_element = np.std(data)
        avg_element = np.average(data)

        # printing the result
        print('maximum element in the array is: ', 
              max_element)
        print('minimum element in the array is: ',
              min_element)
        print('median element in the array is: ',
              median_element)
        print('Standard deviation element in the array is: ',
              std_dev_element)

        print(avg_element)
