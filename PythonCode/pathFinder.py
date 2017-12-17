from smartGrid import smartGrid
import itertools


# A* search algorithm to search the fastest route from a house to a battery.
# The route consits of gridpoints with the lowest manhattan distance from
# house to battery.
# This code is inspired by:  https://gist.github.com/jamiees2/5531924
# and by: http://web.mit.edu/eranki/www/tutorials/search/
def pathFinder(battery, smartGrid, houseID):
    """ A* search algorithm to search fastest route from house to battery. """

    # Set score to -9 to compensate for first step
    score = -9

    # The open and closed lists
    openlist = []
    closedlist = []

    # Make an empty list for path
    path = []

    # Itterate over gridpoints and append gridpoint that match x and y location
    # of current house to a list
    for gridpoint in smartGrid.gridPoints:
        if (gridpoint.xLocation == smartGrid.houses[houseID].xLocation and
                gridpoint.yLocation == smartGrid.houses[houseID].yLocation):
            openlist.append(gridpoint.ID)

    # While the open set is not empty
    while openlist:

        # Make an empty dict distances
        distances = {}

        # Remove gridID if in closedlist
        for gridID in openlist:
            if gridID in closedlist:
                openlist.remove(gridID)

        # Append gridID and manhattandistance to distances
        for gridID in openlist:
            distances.setdefault('ID', [])
            distances.setdefault('Dist', [])
            distances.setdefault('Cost', [])
            distances['ID'].append(smartGrid.gridPoints[gridID].ID)
            distances['Dist'].append(smartGrid.gridPoints[gridID]
                                     .manhattanDistance[battery.ID])
            distances['Cost'].append(smartGrid.gridPoints[gridID]
                                     .cable[battery.ID])

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
        if smartGrid.gridPoints[current].cable[battery.ID] == 0:
            return {"path": path, "score": score}

        # Cable cost is 0 for battery.ID on gridPoint
        smartGrid.gridPoints[current].cable[battery.ID] = 0

        # If current gridID is on the same location as battery, return path
        if (smartGrid.gridPoints[current].xLocation == battery.xLocation and
                smartGrid.gridPoints[current].yLocation == battery.yLocation):
            return {"path": path, "score": score}

        # Add gridIDs from openlist to closedlist
        closedlist.append(current)

        # Empty openlist
        openlist.clear()

        # Add children of current to the openlist
        openlist.append(smartGrid.children(smartGrid.gridPoints[current]))

        # Remove outer brackets of children
        openlist = list(itertools.chain.from_iterable(openlist))
