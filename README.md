# GEOG5995M - Assignment 2

This repository contains the the code and files needed to caculate the number of deaths per week during the Black Death in 1665, based off an equation using the population density and rats caught per week. The data is contained in a raster format, with 1 pixel representing a 100m x 100m area and the overall area of the map representing a 400m x 400m square area. 

The code produces three maps: population density, rats caught per week and deaths per week. The deaths per week is then written to a csv and saved as a txt file. The absolute death count per week is calculated before a GUI is created using Tkinter to pass through the three maps with options to change the weighting and save the maps.

### Files:
This repository contains the main python script black_death.py with two additional txt files (rats.txt and population.txt) needed to read in data. The code then produces the absolute_deaths.txt file based off a calculation from an equation using the data from the rats.txt and population.txt files. 

Please Note: The model uses Tkinter to run and therefore the backend of python graphics needs to be changed into Tkinter to run properly.
