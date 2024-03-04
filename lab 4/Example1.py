# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 12:10:55 2024

@author: mdubo
"""

import numpy as np

G = 6.674e-11;

mass = np.array([3.3e23, 4.87e24, 5.97e24, 6.42e23, 1.8898e27, 5.68e26, 8.68e25, 1.02e26]);
distancefromsun = np.array([57.9e9, 108.2e9, 149.6e9, 228.0e9, 778.5e9, 1432e9, 2867e9, 4515e9]);
forces = np.zeros(int(mass.size/2));

for i in range(int(mass.size/2)):
    forces[i] = float(((G*mass[2*i]*mass[2*i+1])/(distancefromsun[2*i] - distancefromsun[2*i+1])**2));
print(forces);

#This code currently does four force calculations, the gravitational forces
#between Mercury and Venus, Earth and Mars, Jupiter and Saturn, and Uranus
#and Neptune.
