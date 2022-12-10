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
import tkinter
import matplotlib.backends.backend_tkagg as tkagg
import matplotlib; matplotlib.use("TkAgg")
import matplotlib.animation

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
f, [ax1, ax2, ax3] = plt.subplots(1,3, figsize= (12 , 3))
pp = ax1.imshow(population, cmap = 'OrRd')
rr = ax2.imshow(rats, cmap = 'Blues')
dd = ax3.imshow(deaths, cmap = 'Greens')
# add titles
ax1.set_title('Population Density')
ax2.set_title('Rats Caught per Week')
ax3.set_title('Deaths per Week')
# add colorbars
f.colorbar(pp, ax=ax1)
f.colorbar(rr, ax=ax2)
f.colorbar(dd, ax=ax3)


'''
STEP 4
'''
# # # save numpy array to a new txt file
# np.savetxt('absolute_deaths.txt', deaths, delimiter = ',', newline = '', fmt = '%i')

# # check it has worked and produces same map as deaths list
# # with open('absolute_deaths.txt', newline='') as ad:
# #     dataset3 = csv.reader(ad, quoting=csv.QUOTE_NONNUMERIC)
# #     absolute_deaths = [line for line in dataset3]
# # ad.close()

# absolute_deaths = np.loadtxt('absolute_deaths.txt', dtype = int, delimiter = ',')

# plt.imshow(absolute_deaths)


# with open('absolute_deaths2.txt', 'w') as ab:
#     for item in deaths:
#         # write each item on a new line
#         ab.write("%s\n" % item)

# with open('absolute_deaths2.txt', newline='') as ab2:
#     dataset3 = csv.reader(ab2, quoting=csv.QUOTE_NONNUMERIC)
#     absolute_deaths = [line for line in dataset3]
# ab2.close()

'''
STEP 5
'''
# total deaths per week. 



'''
STEP 6
'''
# Allows the user to change the parameter weights for the equation (for example with a scrollbar).
# Create GUI

def run():
    pass 


root = tkinter.Tk() 
root.wm_title("Model")

canvas = tkagg.FigureCanvasTkAgg(f, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

menu = tkinter.Menu(root)  # set up menu
root.config(menu=menu)

model_menu = tkinter.Menu(menu)
menu.add_cascade(label="Model", menu=model_menu)

model_menu.add_command(label="Run model", command=run())

w = tkinter.Canvas(root, width=200, height=200)
w.pack()
w.create_rectangle(0, 0, 200, 200, fill="blue")

print('we got this far')
canvas.draw()

tkinter.mainloop()