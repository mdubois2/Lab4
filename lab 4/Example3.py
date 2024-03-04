# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 16:01:22 2024

@author: mdubo
"""

import numpy as np

resistors_series = np.array([1, 5, 14, 2]);
resistors_parallel = np.array([1, 5, 14, 2]);

totalseries = 0;
totalparallel = 0;

#this is assuming that these arrays are the same length, if not, we would 
#have to use two separate for loops
for i in range(resistors_series.size):
    totalseries += resistors_series[i];
    totalparallel += 1/resistors_parallel[i];
totalparallel = 1/totalparallel

print(f"The total resistance of the circuit if it was connnected in series would be {totalseries}, and if it were in parallel, it would be {totalparallel:.2f}.");

    
    