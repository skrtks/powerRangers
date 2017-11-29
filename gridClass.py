from houseClass import house as houseClass
from batteryClass import battery as batteryClass
import numpy as np
import itertools
import aStar
from matplotlib import pyplot as plt

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


    def gridDrawer():
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

        for battery in batteryClass.batteries:
            xBattery.append(battery.xLocation)
            yBattery.append(battery.yLocation)

        # Make figure and draw axis and ticks
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        ax.set_xticks(np.arange(0, 51, 1), minor=True)
        ax.set_yticks(np.arange(0, 51, 1), minor=True)

        # Draw gridlines
        ax.grid(which='minor', alpha=0.2, linestyle='-')
        ax.grid(which='major', alpha=0.5, linestyle='-')

        # Draw connections from houses to batteries in grid
        totalScore = 0
        colors = ["firebrick", "g", "blue", "deeppink", "darkorange"]
        for battery in batteryClass.batteries:
            color = colors[battery.ID]
            for houseID in battery.connectedHouses:

                returnValues = aStar.aStar(battery, houseClass.houses, houseID, gridPoint.gridPoints)
                path = returnValues["path"]
                totalScore += returnValues["score"]

                pathX = []
                pathY = []

                for ID in path:
                    pathX.append(gridPoint.gridPoints[ID].xLocation)
                    pathY.append(gridPoint.gridPoints[ID].yLocation)

                # Draw lines
                plt.plot(pathX, pathY, color)

        # Make points for houses and batteries
        plt.plot(xHouse, yHouse, "k.")
        plt.plot(xBattery, yBattery, marker="s", linestyle="None", color="blue")
        for battery in batteryClass.batteries:
            ax.annotate(battery.ID, (xBattery[battery.ID],yBattery[battery.ID]))

        print("Score is: {}".format(totalScore))
        plt.title("Score: " + str(totalScore))
        plt.show()
