#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 18:09:13 2023

@author: meteo_procs
"""

# Import Libraries 
import pandas as pd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.patheffects as path_effects
from scipy.ndimage.filters import gaussian_filter1d

# Read final data
data=pd.read_csv("data/berk.csv")
data=data[data.Year>=1940].reset_index(drop=True)

# Initialize figure plot
fig = plt.figure(figsize = (50, 50))
ax = plt.subplot(111)

# Hide axis from figure, we want only the line
for axis in ['top', 'bottom', 'left', 'right']:
    ax.spines[axis].set_linewidth(0)

# Smoothing line with gaussian filter and sigma=1
ysmoothed = gaussian_filter1d(data["ERA5"], sigma=1)

# Plotting of final plot as well
temp=plt.plot(data["Year"],ysmoothed, linewidth=30, color="black")
plt.tick_params(left = False, right = False , labelleft = False , 
                labelbottom = False, bottom = False) 

# Save the plot as .png and transparent
plt.savefig('plots/temp_anomalies_pre_industrial_line_ERA52.png', bbox_inches='tight', transparent=True)