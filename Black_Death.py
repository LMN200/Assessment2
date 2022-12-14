#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 16:56:18 2022

@author: lucynelson
"""

# Import packages
import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import tkinter
from tkinter import simpledialog
import matplotlib.backends.backend_tkagg as tkagg
import matplotlib; matplotlib.use("TkAgg")
import matplotlib.animation
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

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
# print(population[0][:10])
plt.imshow(population)
plt.show()

# Test rats caught data has loaded in and display
# print(rats[0][:10])
plt.imshow(rats)
plt.show()

'''
STEP 2
'''

# use numpy to create a data array with the same length parameters as population
deaths = np.zeros((len(population), len(population[0])))
print(deaths)

# calculate deaths for every line in the list of population densities using the equation
for i in range(len(population)):
    line_deaths = []
    for j in range(len(population[i])):
        deaths[i][j] = ((0.8*rats[i][j])*(1.3*population[i][j]))

# # plot deaths
# plt.imshow(deaths)
# plt.show()


# define calculation for deaths using weighting. set default for the weights as 1. 
def calc_deaths(population=None, rats=None, pop_weight=1, rats_weight=1):
    # don't forget scope of population is within this function. This means population doesn't get changed on the outside
    # All this does is go through a list of lists and multiply every value by the weighting
    #
    population = [[entry * pop_weight for entry in line] for line in population]
    rats = [[entry * rats_weight for entry in line] for line in rats]

    deaths = np.zeros((len(population), len(population[0])))
    print(deaths)

    # calculate deaths for every line in the list of population densities using the equation
    # we don't need to multiply by the weighting here as its already been done for us earlier
    for i in range(len(population)):
        for j in range(len(population[i])):
            deaths[i][j] = ((0.8 * rats[i][j]) * (1.3 * population[i][j]))

    # This effectivly retuns a tuple of three things
    return deaths, population, rats


'''
STEP 3
'''

def set_up_canvas(deaths=None, rats=None, population=None):
    # Display all 3 maps
    f, [ax1, ax2, ax3] = plt.subplots(1, 3, figsize=(12, 3))
    pp = ax1.imshow(population, cmap='OrRd')
    rr = ax2.imshow(rats, cmap='Blues')
    dd = ax3.imshow(deaths, cmap='Greens')
    # add titles
    ax1.set_title('Population Density')
    ax2.set_title('Rats Caught per Week')
    ax3.set_title('Deaths per Week')
    # add colorbars
    f.colorbar(pp, ax=ax1)
    f.colorbar(rr, ax=ax2)
    f.colorbar(dd, ax=ax3)

    return f

'''
STEP 4
'''
# Write to a txt file
# Put deaths into a Pandas dataframe, rounding numbers to 3 decimals places
df_deaths = pd.DataFrame(deaths)
df_deaths = df_deaths.astype(float).round(3)

# Write the deaths dataframe to a txt file
df_deaths.to_csv('absolute_deaths.txt')

# # Test it has worked
# # Read the saved absolute_deaths txt file back in
# df_new_deaths = pd.read_csv ('absolute_deaths.txt')
# # drop the exra columns
# cols_to_drop = ['Unnamed: 0']
# df_new_deaths.drop(columns=cols_to_drop, inplace=True)
# # Plot on graph to check it matches the original deaths graph. 
# plt.imshow(df_new_deaths)

'''
STEP 5
'''
# total overall deaths per week as a count

overall_deaths = (deaths.sum()) / 10**4 
print(f'Overall Deaths per Week = {overall_deaths}')

'''
STEP 6
'''
# Allows the user to change the parameter weights for the equation (for example with a scrollbar).
# Create GUI

def run(root):

    if not root:
        pass
    else:
        root.destroy()

    popup = tkinter.Tk()

    popup.withdraw()
    # popup.minsize(1800, 1800)
    # popup.focus_set()
    # the input dialog
    pop_weight = simpledialog.askstring(title="Test",
                                      prompt="Enter weight to population density:")

    if pop_weight.isnumeric():
        pop_weight = float(pop_weight)
    else:
        print('input is not numeric weighting will be set to 1')
        pop_weight = 1


    # check it out
    print("Hello", pop_weight)

    popup.destroy()

    popup = tkinter.Tk()

    popup.withdraw()
    # the input dialog
    rats_weight = simpledialog.askstring(title="Test",
                                      prompt="Enter weight to rats_caught:")

    if rats_weight.isnumeric():
        rats_weight = float(pop_weight)
    else:
        print('input is not numeric weighting will be set to 1')
        rats_weight = 1


    # check it out
    print("Hello", rats_weight)

    popup.destroy()



    # pop_weight = float(input("Enter weight to population density:"))
    # rats_weight = float(input("Enter weight to rats_caught:"))
    deaths, new_pop, new_rats = calc_deaths(population=population, rats=rats, pop_weight=pop_weight, rats_weight=rats_weight)

    root = tkinter.Tk()
    root.wm_title("Model")
    f = set_up_canvas(deaths=deaths, rats=new_rats, population=new_pop)

    canvas = tkagg.FigureCanvasTkAgg(f, master=root)
    canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

    # button that displays the plot
    plot_button = tkinter.Button(master=root,
                                  command=lambda: run(root),
                                  height=2,
                                  width=30,
                                  bg="red", fg="yellow",
                                  text="Change weightings")

    # place the button
    # in main window
    plot_button.pack()

    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas, root)
    toolbar.update()

    menubar = tkinter.Menu(root)  # set up menu
    root.config(menu=menubar)

    model_menu = tkinter.Menu(menubar)

    menubar.add_separator()

    menubar.add_cascade(label="Model", menu=model_menu)
    menubar.add_command(label="Exit", command=exit)

    print('we got this far')
    # canvas.draw()

    tkinter.mainloop()

run(False)
