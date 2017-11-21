import csv
import numpy as np
import itertools
from file_reader import children
from houseClass import house
from batteryClass import battery
from gridClass import *
from matplotlib import pyplot as plt

# A* search algorithm to search the fastest route from a house to a battery.
# The route consits of gridpoints with the lowest manhattan distance from a battery.
# This code is inspired by:  https://gist.github.com/jamiees2/5531924
# and by: http://web.mit.edu/eranki/www/tutorials/search/
def aStar(battery, houses, houseID, gridPoints):

    score = -9

    # The open and closed lists.
    openset = []
    #closedset = []

    # Make an empty list for path.
    path = []

    # Itterate over gridpoints and append gridpoint that match x and y locations of current house to a list.
    for gridpoint in gridPoints:
        if gridpoint.xLocation == houses[houseID].xLocation and gridpoint.yLocation == houses[houseID].yLocation:
            openset.append(gridpoint.ID)

    # While the open set is not empty.
    while openset:

        # Make an empty dict distances.
        distances = {}

        # Append gridID and manhattandistance to distances.
        for gridID in openset:
            distances.setdefault('ID',[])
            distances.setdefault('Dist',[])
            distances['ID'].append(gridPoints[gridID].ID)
            distances['Dist'].append(gridPoints[gridID].manhattanDistance[battery.ID])

        # Set position counter to zero.
        position = 0

        # Current is the gridID with the lowest manhattan distance.
        for distance in distances['Dist']:
            if distance == min(distances['Dist']):
                current = distances['ID'][position]
            position += 1

        # Empty distances.
        distances.clear()

        # Add current to path.
        path.append(current)
        score += 9

        # If current gridID is on the same location as battery, return path.
        if gridPoints[current].xLocation == battery.xLocation and gridPoints[current].yLocation == battery.yLocation:
            return {"path": path, "score": score}

        # Add gridIDs from openset to closedset.
        #closedset.append(openset)

        # Empty openset.
        openset.clear()

        # Add children of current to the openset.
        openset.append(children(gridPoints[current], gridPoints))

        # Remove outer brackets of children.
        openset = list(itertools.chain.from_iterable(openset))

    # Throw an exception if there is no path.
    raise ValueError("No path found!")
