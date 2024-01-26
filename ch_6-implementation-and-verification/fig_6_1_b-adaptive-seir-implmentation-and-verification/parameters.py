import numpy as np
from pathlib import Path
import os

# This file defines the parameters used for the SIRQ model. These parameters are taken from Dobson  :
# Code: https://github.com/simoninireland/introduction-to-epidemics/blob/master/src/seir.ipynb

# Model Parameters
p_exposed = 0.001
p_infect = 0.000075
p_remove = 0.002
p_rewire = 0.8
p_detect = np.linspace(0.0, 1.0, 100)

# Network Parameters 
n = 10000
k_mean = 40

# Experiment Parameters 
ens = 100
cores = 30


data_directory = 'datasets/'

def create_data_output_directory(path=''):
    if not os.path.exists(data_directory+ path):
        Path(data_directory + path).mkdir(parents=True, exist_ok=True)

def get_out_path(path=''):
    return data_directory + path + '.json'
