# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 14:59:53 2024

@author: mdubo
"""

import numpy

print("Please enter the x component of the vector");
x = float(input());
print("Please enter the y component of the vector");
y = float(input());
vector = (x, y);
print("The components of this vector are " + str(vector[0]) + "i + " + str(vector[1]) + "j. The magnitude of the vector is " + str(numpy.sqrt((vector[0])**2 + (vector[1])**2)));