#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 15:22:40 2022

@author: lucynelson
"""
# Import packages

import csv
import matplotlib


# Load in dataset for population density and rat deaths
with open('population.txt', newline='') as p:
    dataset = csv.reader(p, quoting=csv.QUOTE_NONNUMERIC)
    population = [line for line in dataset]


with open('rats.txt', newline='') as r:
    dataset = csv.reader(r, quoting=csv.QUOTE_NONNUMERIC)
    rats = [line for line in dataset]
 
# Test both datasets has been loaded in
matplotlib.pyplot.imshow(population)
matplotlib.pyplot.imshow(rats)

d = (0.8*r)(1.3*p)