# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 13:45:40 2024

@author: mdubo
"""

names = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'];
gs = [3.61, 8.83, 9.81, 3.75, 26.00, 11.2, 10.5, 13.3];

planets = [];
for i in range(len(names)):
    planets.append(({'Name': str(names[i]), 'Gravitational Constant': float(gs[i])}))
    
print("Please input your mass in kilograms ");
m = float(input());
print("Please input the name of your desired planet (Please capitalize the first letter of the name of the planet) ");
namedesired = str(input());

for i in range(len(names)):
    if planets[i].get('Name') == namedesired:
        userWeight = float(planets[i].get('Gravitational Constant'))*m;
        

    
print("Your weight on " + namedesired + " would be " + str(round(userWeight, 4)) + " N");
    
    