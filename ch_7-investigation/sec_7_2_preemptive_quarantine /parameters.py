import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
import os

plt.rc('font', size=18)         
plt.rc('axes', titlesize=15)     
plt.rc('axes', labelsize=17)    
plt.rc('xtick', labelsize=13)    
plt.rc('ytick', labelsize=13)    
plt.rc('legend', fontsize=15)   
plt.rc('figure', titlesize=13)

# Model Parameters
p_infect = 0.1 
p_detects = np.linspace(0, 1.0, 100)
p_remove = 1 # Implicitly Defined

# Network Parameters 
n = 10000 # 'N'
k_mean = 40 # 'average_degree'

# Monitor Parameters
delta = 1

# Experiment Parameters 
ens = 100
cores = 50


data_directory = 'datasets/'

def create_data_output_directory(path=''):
    if not os.path.exists(data_directory+ path):
        Path(data_directory + path).mkdir(parents=True, exist_ok=True)

def get_out_path(path=''):
    return data_directory + path + '.json'
