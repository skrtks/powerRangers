
import csv
import numpy as np
import itertools
from file_reader import children
from houseClass import house
from batteryClass import battery
from gridClass import *
from matplotlib import pyplot as plt



# from: https://gist.github.com/jamiees2/5531924
# pseudocode: http://web.mit.edu/eranki/www/tutorials/search/
def aStar(batteries, houses, gridPoints):

    # Loop through all batteries and houses.
    for battery in batteries:
        for house in houses:

            # The open and closed lists.
            openset = []
            closedset = []

            # Make an empty list for path.
            path = []

            # Itterate over gridpoints and append gridpoint that match x and y locations of current house to a list.
            for gridpoint in gridPoints:
                if gridpoint.xLocation == house.xLocation and gridpoint.yLocation == house.yLocation:
                    openset.append(gridpoint.ID)

            # While the open set is not empty.
            while openset:

                print("openset: ")
                print(openset)

                # Append gridID and manhattandistance to dict distances.
                distances = {}

                for gridID in openset:
                    distances.setdefault('ID',[])
                    distances.setdefault('Dist',[])
                    distances['ID'].append(gridPoints[gridID].ID)
                    distances['Dist'].append(gridPoints[gridID].manhattanDistance[house.ID])

                print("distances: ")
                print(distances)

                # Current is the gridID with the lowest manhattan distance.
                smallest = min(distances['Dist'])
                print("smallest: {}".format(smallest))

                position = 0

                for distance in distances['Dist']:
                    if distance == smallest:
                        current = distances['ID'][position]
                    position += 1


                print("current: ")
                print(current)

                # Empty dict distances.
                distances.clear()

                # Add current to path.
                path.append(current)
                print("path: ")
                print(path)

                # If current gridID is on the same location as battery, return path
                if gridPoints[current].xLocation == battery.xLocation and gridPoints[current].yLocation == battery.yLocation:
                    print("final path: ")
                    print(path)
                    return path

                # Add gridID to the closed set
                closedset.append(openset)

                # Empty open set.
                openset.clear()

                # Add children of current to the open set.
                openset.append(children(gridPoints[current], gridPoints))

                # Remove outer brackets of children.
                openset = list(itertools.chain.from_iterable(openset))

        #Throw an exception if there is no path.
        raise ValueError("No path found!")



if __name__ == "__main__":
    main()
