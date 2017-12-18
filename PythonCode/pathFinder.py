from smartGrid import smartGrid
import itertools

def pathFinder(battery, smartGrid, houseID):
    """
    Search algorithm to search a fast route from house to battery.
    Inspired by: http://web.mit.edu/eranki/www/tutorials/search/
                 https://gist.github.com/jamiees2/5531924
    """

    # Score is minus 9 (cost of a cable) to compensate for first move
    score = -9

    # Make openlist for gridIDs which have to be calculated,closedlist for
    # gridIDs which have been calculated already
    openlist = []
    closedlist = []

    # Empty list path for storing route
    path = []

    # Append gridpointID where current house is on
    for gridpoint in smartGrid.gridPoints:
        if (gridpoint.xLocation == smartGrid.houses[houseID].xLocation and
                gridpoint.yLocation == smartGrid.houses[houseID].yLocation):
            openlist.append(gridpoint.ID)

    #
    while openlist:

        # Dict gridPointInfo
        gridPointInfo = {'ID': [], 'Dist':[], 'Cost': []}

        # Remove gridID if in closedlist
        for gridID in openlist:
            if gridID in closedlist:
                openlist.remove(gridID)

        # Append gridID, manhattandistance and cost to gridPointInfo
        for gridID in openlist:
            gridPointInfo['ID'].append(gridID)
            gridPointInfo['Dist'].append(smartGrid.gridPoints[gridID]
                                         .manhattanDistance[battery.ID])
            gridPointInfo['Cost'].append(smartGrid.gridPoints[gridID]
                                         .cable[battery.ID])

        # Set position counter to zero
        position = 0

        # Make empty list fScores
        gridPointScores = []

        # Calculate gridPointScore, manhattandistance to battery plus cost of
        # gridPoint, for gridPoints in openlist
        for gridID in openlist:
            gridPointScore = (gridPointInfo['Dist'][position] +
                              gridPointInfo['Cost'][position])
            gridPointScores.append(gridPointScore)
            position += 1

        # Set position counter to zero
        position = 0

        # Current is the gridID with the lowest gridPointScore
        for gridPointScore in gridPointScores:
            if gridPointScore == min(gridPointScores):
                current = gridPointInfo['ID'][position]
            position += 1

        gridPointInfo.clear()
        gridPointScores.clear()

        # Update score
        score += 9

        # Add current gridID to path
        path.append(current)

        # If current gridID found a cable to the same battery,
        # return path and score
        if smartGrid.gridPoints[current].cable[battery.ID] == 0:
            return {"path": path, "score": score}

        # Cable cost is 0 for battery.ID on gridPoint
        smartGrid.gridPoints[current].cable[battery.ID] = 0

        # If current gridID is on the same location as battery,
        # return path and score
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
