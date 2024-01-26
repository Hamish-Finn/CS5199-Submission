import numpy as np
from pathlib import Path
import os

# This file defines the parameters used for the SIRQ model. These parameters are taken from Rizi et al. :
# Code: https://github.com/k-rizi/Contact-Tracing-On-Clique-Networks/blob/10f26effd2881d7ecf518dd91a6734c21733f248/fig3a/fig3a.ipynb

# Model Parameters
p_infects = np.linspace(0.1, 0.7, 40) # 'p_range'
p_detect = [0, .25, .50] # 'alphas'
p_remove = 1 # Implicitly Defined

# Regular Clique Network Parameters
n_RC = 100000 # 'N'
k_mean_RC = 6 # 'average_degree'
c_sizes_RC = [2, 3, 4] # 'c_1_list'

# Experiment Parameters 
ens = 100
cores = 40


# Utility Functions.
data_directory = 'datasets/'

def create_data_output_directory(path=''):
    if not os.path.exists(data_directory+ path):
        Path(data_directory + path).mkdir(parents=True, exist_ok=True)

def get_out_path(path=''):
    return data_directory + path + '.json'
