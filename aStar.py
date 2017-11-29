import helpers
from houseClass import house
from batteryClass import battery
from gridClass import *

# A* search algorithm to search the fastest route from a house to a battery.
# The route consits of gridpoints with the lowest manhattan distance from
# house to battery.
# This code is inspired by:  https://gist.github.com/jamiees2/5531924
# and by: http://web.mit.edu/eranki/www/tutorials/search/
def aStar(battery, houses, houseID, gridPoints):
    """ A* search algorithm to search fastest route from house to battery. """

    # Set score to -9 to compensate for first step
    score = -9

    # The open and closed lists
    openset = []
    closedset = []

    # Make an empty list for path
    path = []

    # Itterate over gridpoints and append gridpoint that match x and y location of current house to a list
    for gridpoint in gridPoints:
        if (gridpoint.xLocation == houses[houseID].xLocation and
            gridpoint.yLocation == houses[houseID].yLocation):
                openset.append(gridpoint.ID)

    # While the open set is not empty
    while openset:

        # Make an empty dict distances
        distances = {}

        # Remove gridID if in closedset
        for gridID in openset:
            if gridID in closedset:
                openset.remove(gridID)

        # Append gridID and manhattandistance to distances
        for gridID in openset:
            distances.setdefault('ID',[])
            distances.setdefault('Dist',[])
            distances.setdefault('Cost',[])
            distances['ID'].append(gridPoints[gridID].ID)
            distances['Dist'].append(gridPoints[gridID].manhattanDistance[battery.ID])
            distances['Cost'].append(gridPoints[gridID].cable[battery.ID])

        # Set position counter to zero
        position = 0

        # Make empty list fScores
        fScores = []

        # Current is the gridID with the lowest manhattan distance
        for distance in distances['Dist']:
            fScore = distance + distances['Cost'][position]
            fScores.append(fScore)
            position += 1

        # Set position counter back to zero
        position = 0

        # Current is the gridID with the lowest fScore
        for fScore in fScores:
            if fScore == min(fScores):
                current = distances['ID'][position]
            position += 1

        # Empty distances and fScores
        distances.clear()
        fScores.clear()

        # Update score
        score += 9

        # Add current to path
        path.append(current)

        # If there is an other path to battery, return path
        if gridPoints[current].cable[battery.ID] == 0:
            return {"path": path, "score": score}

        # Cable cost is 0 for battery.ID on gridPoint
        gridPoints[current].cable[battery.ID] = 0

        # If current gridID is on the same location as battery, return path
        if (gridPoints[current].xLocation == battery.xLocation and
            gridPoints[current].yLocation == battery.yLocation):
            return {"path": path, "score": score}

        # Add gridIDs from openset to closedset
        closedset.append(current)

        # Empty openset
        openset.clear()

        # Add children of current to the openset
        openset.append(helpers.children(gridPoints[current], gridPoints))

        # Remove outer brackets of children
        openset = list(itertools.chain.from_iterable(openset))
