# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 15:40:26 2024

@author: mdubo
"""

import numpy as np
import math

v0 = 5;
theta = 30;
g = 9.81;

theta = math.radians(theta);

timeintervals = np.linspace(0, 10, 11);

x = np.zeros(timeintervals.size);
y = np.zeros(timeintervals.size);

for i in range(timeintervals.size):
    x[i] = v0*np.cos(theta)*timeintervals[i];
    y[i] = v0*np.sin(theta)*timeintervals[i] - (1/2)*g*timeintervals[i]**2;
    print(f"At t = {timeintervals[i]}, the coordinates of the projectile are x = {x[i]} and y = {y[i]}.");
    
    


