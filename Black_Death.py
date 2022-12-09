#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 15:22:40 2022

@author: lucynelson
"""

'''
STEP 1
'''
# Import packages
import csv
import matplotlib.pyplot as plt
import numpy as np

population = []
rats = []


# Load in dataset for population density and rats caught
with open('population.txt', newline='') as p:
    dataset = csv.reader(p, quoting=csv.QUOTE_NONNUMERIC)
    population = [line for line in dataset]
p.close()

with open('rats.txt', newline='') as r:
    dataset2 = csv.reader(r, quoting=csv.QUOTE_NONNUMERIC)
    rats = [line for line in dataset2]
r.close()

# Test population density has loaded in and display
print(population[0][:10])
plt.imshow(population)
plt.show()


# Test rats caught data has loaded in and display
print(rats[0][:10])
plt.imshow(rats)
plt.show()

'''
STEP 2
'''

# deaths = [[] for i in range(len(population))]

# for i in range(len(population)):
#     line_deaths = []
#     for j in range(len(population[i])):
#         line_deaths.append((0.8*rats[i][j])*(1.3*population[i][j]))
#     deaths[i] = line_deaths

# print(len(deaths))

# plt.imshow(deaths)


# use numpy to create a daa array with the same length parameters as population
deaths = np.zeros((len(population), len(population[0])))
print(deaths)

# calculate deaths for every line in the list of population densities using the equation
for i in range(len(population)):
    line_deaths = []
    for j in range(len(population[i])):
        deaths[i][j] = ((0.8*rats[i][j])*(1.3*population[i][j]))

# plot deaths
plt.imshow(deaths)

'''
STEP 3
'''
# Display all 3 maps

f, [ax1, ax2, ax3] = plt.subplots(1,3)
pp = ax1.imshow(population)
rr = ax2.imshow(rats)
dd = ax3.imshow(deaths)
ax1.set_title('Population Density')
ax2.set_title('Rats Caught')
ax3.set_title('Deaths')

f.colorbar(pp, ax=ax1)
f.colorbar(rr, ax=ax2)
f.colorbar(dd, ax=ax3)



'''
STEP 4
'''



'''
STEP 5
'''


'''
STEP 6
'''

# d = (0.8*r)(1.3*p)
# need to create a new list and run the pairs of data from the rastor map through the equation. Then write to a CSV file.