#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 15:22:40 2022

@author: lucynelson
"""
# Import packages

import csv
import matplotlib.pyplot as plt

deaths = []
population = []
rats = []


# Load in dataset for population density and rats caught
with open('population.txt', newline='') as p:
    dataset = csv.reader(p, quoting=csv.QUOTE_NONNUMERIC)
    population = [line for line in dataset]


with open('rats.txt', newline='') as r:
    dataset = csv.reader(r, quoting=csv.QUOTE_NONNUMERIC)
    rats = [line for line in dataset]
    dataset = csv.reader(r, quoting=csv.QUOTE_NONNUMERIC)
    rats = [line for line in dataset]
 
# Test both txt files has been loaded in as raster maps
plt.imshow(population)
plt.imshow(rats)


for x in len(rats):
    line_deaths = []
    for i, pop in enumerate(population[x]):
        line_deaths.append((0.8*rats[x][i])*(1.3*pop))

    deaths += line_deaths
    
for j, rat_line in enumerate(rats):
   line_deaths = []
   for i, pop in enumerate(population[j]):
       line_deaths.append((0.8*rat_line[i])*(1.3*pop))

   deaths += [line_deaths]

plt.imshow(deaths)
plt.show()


x = 9




# d = (0.8*r)(1.3*p)
# need to create a new list and run the pairs of data from the rastor map through the equation. Then write to a CSV file.