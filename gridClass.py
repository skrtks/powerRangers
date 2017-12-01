

class gridPoint:
    """ Class for grid segments. """

    gridPoints = []

    def __init__(self, ID, xLocation, yLocation, manhattanDistance=None, cable=None):

        self.ID = ID
        self.xLocation = xLocation
        self.yLocation = yLocation
        self.cable = [9, 9, 9, 9, 9]
        if manhattanDistance == None:
            self.manhattanDistance = []
        if cable == None:
            self.cable = []

    def gridFiller(gridPoints):
        """"Create grid"""

        # Initiate ID, xLocation and yLocation.
        ID = 0
        xLocation = 0
        yLocation = 0

        # Create instances of grid points.
        for i in range(51):
            for j in range(51):
                gridPoints.append(gridPoint(ID, xLocation, yLocation))
                ID += 1
                xLocation += 1
            yLocation += 1
            xLocation = 0


    def gridDrawer(gridPoints):
        """"Draw grid with batteries, houses and connections"""

        # Initiate list for coordinates from houses and batteries
        xHouse = []
        yHouse = []
        xBattery = []
        yBattery = []

        # Fill lists with coordinates
        for house in houseClass.houses:
            xHouse.append(house.xLocation)
            yHouse.append(house.yLocation)

        # [xHouse,yHouse,s] = optimalizationAlgorithm()
        # print(s)

        for battery in batteryClass.batteries:
            xBattery.append(battery.xLocation)
            yBattery.append(battery.yLocation)

        # Make figure and draw axis and ticks
        fig = plt.figure()
        plt.axis([-1, 51, -1, 51])
        ax = fig.add_subplot(1, 1, 1)

        ax.set_xticks(np.arange(0, 51, 1), minor=True)
        ax.set_yticks(np.arange(0, 51, 1), minor=True)

        # Draw gridlines
        ax.grid(which='minor', alpha=0.2, linestyle='-')
        ax.grid(which='major', alpha=0.5, linestyle='-')

        xBat = []
        yBat = []

        # Loop through all batteries and houses.
        totalScore = 0
        colors = ["firebrick", "g", "blue", "deeppink", "darkorange"]
        for battery in batteryClass.batteries:
            color = colors[battery.ID]  
            for houseID in battery.connectedHouses:

                # generate a star path
                came_from = aStar.a_star_search(gridPoints, battery, houseClass.houses[houseID].gridID, battery.gridID)

                # reconstruct the path
                path = aStar.reconstruct_path(came_from, houseClass.houses[houseID].gridID, battery.gridID)

                # update the costs for the gridpoints
                for point in path:
                    gridPoints[point].cable[battery.ID] = 0

                # totalScore += returnValues["score"]

                pathX = []
                pathY = []

                for ID in path:
                    pathX.append(gridPoint.gridPoints[ID].xLocation)
                    pathY.append(gridPoint.gridPoints[ID].yLocation)

                # Make points for houses and batteries
                plt.plot(pathX, pathY, color)


        # Make points for houses and batteries
        plt.plot(xHouse, yHouse, "k.")
        plt.plot(xBattery, yBattery, marker="s", linestyle="None", color="blue")
        for battery in batteryClass.batteries:
            ax.annotate(battery.ID, (xBattery[battery.ID],yBattery[battery.ID]))

        print("Score is: {}".format(totalScore))
        plt.title(totalScore)
        plt.show()

from houseClass import house as houseClass
from batteryClass import battery as batteryClass
import numpy as np
import itertools
import Astar_sam as aStar
from matplotlib import pyplot as plt
