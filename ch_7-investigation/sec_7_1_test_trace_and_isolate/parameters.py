import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
import os

plt.rc('font', size=18)         
plt.rc('axes', titlesize=15)     
plt.rc('axes', labelsize=17)    
plt.rc('xtick', labelsize=13)    
plt.rc('ytick', labelsize=13)    
plt.rc('legend', fontsize=15,markerscale=3.)   
plt.rc('figure', titlesize=13)


# Model Parameters
p_exposed = 0.001
p_infect = 0.000075
p_remove = 0.002
p_rewire = 0.8
p_detect = np.linspace(0, 1.0, 100)

# Network Parameters 
n = 10000
k_mean = 40 

# Monitor Parameters
delta = 20000.0 

# Experiment Parameters 
ens =  50
cores = 50


data_directory = 'datasets/'

def create_data_output_directory(path=''):
    if not os.path.exists(data_directory+ path):
        Path(data_directory + path).mkdir(parents=True, exist_ok=True)

def get_out_path(path=''):
    return data_directory + path + '.json'
