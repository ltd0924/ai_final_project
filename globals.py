import random
import math
import numpy as np
'''
Contains all global variables specific to simulation
'''
# Defines range for coordinates when dustbins are randomly scattered
xMax = 1000
yMax = 1000
seedValue = 1
numNodes = 150
numGenerations = 200
# size of population
populationSize = 100
mutationRate = np.random.normal(loc=0.3, scale=0.1, size=None)
crossoverRate = 0.6
tournamentSize = 10
elitism = True
# number of trucks
numTrucks = 5

def random_range(n, total):
    """Return a randomly chosen list of n positive integers summing to total.
    Each such list is equally likely to occur."""

    dividers = sorted(random.sample(range(1, total), n - 1))
    return [a - b for a, b in zip(dividers + [total], [0] + dividers)]

# Randomly distribute number of dustbins to subroutes
# Maximum and minimum values are maintained to reach optimal result
def route_lengths():
    upper = (numNodes + numTrucks - 1)
    fa = upper/numTrucks*1.6 # max route length
    fb = upper/numTrucks*0.6 # min route length
    a = random_range(numTrucks, upper)
    while 1:
        if all( i < fa and i > fb  for i in a):
                break
        else:
                a = random_range(numTrucks, upper)
    return a
