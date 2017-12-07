
class smartGrid:

    gridPoints = []
    houses = []
    batteries = []

    def gridFiller():
        """"Create grid"""

        # Initiate ID, xLocation and yLocation.
        ID = 0
        xLocation = 0
        yLocation = 0

        # Create instances of grid points.
        for i in range(51):
            for j in range(51):
                smartGrid.gridPoints.append(gridClass.gridPoint(ID, xLocation, yLocation))
                ID += 1
                xLocation += 1
            yLocation += 1
            xLocation = 0

        batteryClass.battery.assignGridIDs(smartGrid.batteries, smartGrid.gridPoints)
        houseClass.house.assignGridIDs(smartGrid.houses, smartGrid.gridPoints)


    def gridDrawer():
        """"Draw grid with batteries, houses and connections"""

        # Initiate list for coordinates from houses and batteries
        xHouse = []
        yHouse = []
        xBattery = []
        yBattery = []

        # Make square figure and draw axis and ticks
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        ax.set_aspect('equal')
        ax.set_xticks(np.arange(0, 51, 1), minor=True)
        ax.set_yticks(np.arange(0, 51, 1), minor=True)

        # Draw gridlines
        ax.grid(which='minor', alpha=0.2, linestyle='-')
        ax.grid(which='major', alpha=0.5, linestyle='-')

        # Fill lists with coordinates
        for house in smartGrid.houses:
            xHouse.append(house.xLocation)
            yHouse.append(house.yLocation)

        for battery in smartGrid.batteries:
            xBattery.append(battery.xLocation)
            yBattery.append(battery.yLocation)

        # Draw connections from houses to batteries in grid
        totalScore = 0
        colors = ["firebrick", "g", "blue", "deeppink", "darkorange"]
        for battery in smartGrid.batteries:

            # # Make square figure and draw axis and ticks
            # fig = plt.figure()
            # ax = fig.add_subplot(1, 1, 1)
            # ax.set_aspect('equal')
            # ax.set_xticks(np.arange(0, 51, 1), minor=True)
            # ax.set_yticks(np.arange(0, 51, 1), minor=True)
            #
            # # Draw gridlines
            # ax.grid(which='minor', alpha=0.2, linestyle='-')
            # ax.grid(which='major', alpha=0.5, linestyle='-')

            color = colors[battery.ID]
            for houseID in battery.connectedHouses:
                # generate a star path
                (cameFrom, score) = dijkstra.dijkstraSearch(smartGrid.gridPoints, battery, smartGrid.houses[houseID].gridID, battery.gridID)
                totalScore += score[battery.gridID]
                # reconstruct the path
                path = dijkstra.reconstructPath(cameFrom, smartGrid.houses[houseID].gridID, battery.gridID)

                # update the costs for the gridpoints
                for point in path:
                    smartGrid.gridPoints[point].cable[battery.ID] = 0

                # totalScore += returnValues["score"]

                pathX = []
                pathY = []

                for ID in path:
                    pathX.append(smartGrid.gridPoints[ID].xLocation)
                    pathY.append(smartGrid.gridPoints[ID].yLocation)

                # Draw lines
                plt.plot(pathX, pathY, color)

        # Make points for houses and batteries
        plt.plot(xHouse, yHouse, "k.")
        plt.plot(xBattery, yBattery, marker="s", linestyle="None", color="blue")
        for battery in smartGrid.batteries:
            ax.annotate(battery.ID, (xBattery[battery.ID],yBattery[battery.ID]))

        # totalScore plus battery cost
        totalScore += 25000
        plt.title("Score: " + str(totalScore))
        plt.show()

    def fileReader(fileHouses, fileBatteries):
        """"Read information of houses and batteries from files"""

        # Initiate ID.
        ID = 0

        # Open the file containing houses
        with open(fileHouses) as h, open(fileBatteries) as b:

            # Read the file and separate values in list.
            readerHouses = csv.reader(h, delimiter=',', quoting=csv.QUOTE_NONE)
            readerBatteries = csv.reader(b, delimiter=',', quoting=csv.QUOTE_NONE)

            # Skip the header of the file.
            next(h)
            next(b)

            # Create instances of houses or batteries.
            for row in readerHouses:
                smartGrid.houses.append(houseClass.house(ID, int(row[0]), int(row[1]), float(row[2])))
                ID += 1

            ID = 0
            for row in readerBatteries:
                smartGrid.batteries.append(batteryClass.battery(ID, int(row[0]), int(row[1]), float(row[2])))
                ID += 1


    def manhattanDistance():
        """"Calculate mannhattendistance for avery gridpoint to batteries"""

        # Loop trough batteries and gridpoints calculate manhattendistance between them
        for battery in smartGrid.batteries:
            for gridPoint in smartGrid.gridPoints:
                distance = abs(gridPoint.xLocation - battery.xLocation) + abs(gridPoint.yLocation - battery.yLocation)
                gridPoint.manhattanDistance.append(distance)
                gridPoint.cable.append(9)

                # If house on gridPoint, append distance to house
                for house in smartGrid.houses:
                    if house.xLocation == gridPoint.xLocation and house.yLocation == gridPoint.yLocation:
                        house.manhattanDistance.append(distance)



    def children(gridPoint):
        '''returns gridpoint ID's for possible moves from current gridpoint'''

        # Calculate possible locations for x and y
        childrenX = [gridPoint.xLocation - 1, gridPoint.xLocation, gridPoint.xLocation + 1, gridPoint.xLocation]
        childrenY = [gridPoint.yLocation, gridPoint.yLocation - 1, gridPoint.yLocation, gridPoint.yLocation + 1]

        children = []

        # Itterate over gridpoints and append gridpoints that match x and y locations of children to a list
        for gridpoint in smartGrid.gridPoints:
            for i in range(4):
                if gridpoint.xLocation == childrenX[i] and gridpoint.yLocation == childrenY[i]:
                    children.append(gridpoint.ID)

        return children

import houseClass
import batteryClass
import gridClass
import numpy as np
import itertools
import dijkstra as dijkstra
from matplotlib import pyplot as plt
import csv
