class smartGrid:

    def __init__(self):
        self.gridPoints = []
        self.houses = []
        self.batteries = []

    def gridFiller(self):
        """
        Create grid.

        Args: self
        """

        # Initiate ID, xLocation and yLocation
        ID = 0
        xLocation = 0
        yLocation = 0

        # Create instances of grid points
        for i in range(51):
            for j in range(51):
                self.gridPoints.append(gridClass.gridPoint(ID, xLocation,
                                                           yLocation))
                ID += 1
                xLocation += 1
            yLocation += 1
            xLocation = 0

        self.assignGridInfo()

    def assignGridInfo(self):
        """
        Assign gridID to houses and batteries.
        Change cost of gridPoint if it has a house on it.

        Args: self
        Returns: True
        """

        for point in self.gridPoints:
            for house in self.houses:
                if (point.xLocation == house.xLocation and
                point.yLocation == house.yLocation):
                    house.gridID = point.ID
                    point.cost = [5000, 5000, 5000, 5000, 5000]
            for battery in self.batteries:
                if (point.xLocation == battery.xLocation and
                        point.yLocation == battery.yLocation):
                    battery.gridID = point.ID
        return True

    def gridDrawer(self):
        """
        Draw grid with batteries, houses and connections.

        Args: self
        """

        # Price of laying a cable underneath a house
        priceUnderHouse = 5000

        # Price of five batteries
        costBatteries = 25000

        print("drawing...")

        # Initiate list for coordinates from houses and batteries
        xHouse = []
        yHouse = []
        xBattery = []
        yBattery = []

        # Fill lists with coordinates
        for house in self.houses:
            xHouse.append(house.xLocation)
            yHouse.append(house.yLocation)

        for battery in self.batteries:
            xBattery.append(battery.xLocation)
            yBattery.append(battery.yLocation)

        # Make square figure and draw axis and ticks
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        ax.set_aspect('equal')
        ax.set_xticks(np.arange(0, 51, 1), minor=True)
        ax.set_yticks(np.arange(0, 51, 1), minor=True)

        # Draw gridlines
        ax.grid(which='minor', alpha=0.2, linestyle='-')
        ax.grid(which='major', alpha=0.5, linestyle='-')

        # Draw connections from houses to batteries in grid,
        # give cable to battery its own color
        totalScore = 0
        colors = ["firebrickred", "g", "blue", "deeppink", "darkorange"]

        for battery in self.batteries:

            # Make closedSet and set color for cable line
            closedSet = set()
            color = colors[battery.ID]

            for houseID in battery.connectedHouses:

                # Generate dijkstra path
                (cameFrom, score) = dijkstra.dijkstraSearch(battery, self,
                                                            self.houses[houseID]
                                                            .gridID,
                                                            battery.gridID)
                totalScore += score[battery.gridID] - priceUnderHouse

                # Reconstruct the path
                path = dijkstra.reconstructPath(cameFrom,
                                                self.houses[houseID].gridID,
                                                battery.gridID)

                # Update the costs for the gridpoints
                for point in path:
                    # Decrease cost if not 'free'
                    if self.gridPoints[point].cost[battery.ID] != 0:
                        self.gridPoints[point].cost[battery.ID] -= 9

                # Append route of cables to battery
                pathX = []
                pathY = []

                for ID in path:
                  if ID in closedSet:
                    pathX.append(self.gridPoints[ID].xLocation)
                    pathY.append(self.gridPoints[ID].yLocation)
                    closedSet.add(ID)
                    break
                  else:
                    pathX.append(self.gridPoints[ID].xLocation)
                    pathY.append(self.gridPoints[ID].yLocation)
                    closedSet.add(ID)

                # Draw cables
                plt.plot(pathX, pathY, color, alpha=0.5)

        # Draw markers for houses and batteries
        plt.plot(xHouse, yHouse, "k.")
        plt.plot(xBattery, yBattery, marker="s", color="blue", ls='None')

        # Show battery ID next to battery markers
        for battery in self.batteries:
            ax.annotate(battery.ID, (xBattery[battery.ID],
                                     yBattery[battery.ID]))

        # Show graph and cost of smartGrid
        totalCost = totalScore + costBatteries
        plt.title("Cable cost: " + str(totalScore) + " Battery cost: 25000 " +
                  "Total cost: " + str(totalCost))
        plt.show()

    def fileReader(self, fileHouses, fileBatteries):
        """
        Read information of houses and batteries from files.

        Args: self, fileHouses, fileBatteries
        """

        # Initiate ID
        ID = 0

        # Open the file containing houses
        with open(fileHouses) as h, open(fileBatteries) as b:

            # Read the file and separate values in list
            readerHouses = csv.reader(h, delimiter=',', quoting=csv.QUOTE_NONE)
            readerBatteries = csv.reader(b, delimiter=',',
                                         quoting=csv.QUOTE_NONE)

            # Skip the header of the file
            next(h)
            next(b)

            # Create instances of houses or batteries
            for row in readerHouses:
                self.houses.append(houseClass.house(ID, int(row[0]),
                                                    int(row[1]),
                                                    float(row[2])))
                ID += 1

            ID = 0

            for row in readerBatteries:
                self.batteries.append(batteryClass.battery(ID, int(row[0]),
                                      int(row[1]), float(row[2])))
                ID += 1

    def manhattanDistance(self):
        """
        Calculate mannhattan distance for every gridpoint to batteries.

        Args: self
        """

        # Loop trough batteries and gridpoints calculate
        # manhattan distance between them
        for battery in self.batteries:
            for gridPoint in self.gridPoints:
                distance = (abs(gridPoint.xLocation - battery.xLocation)
                            + abs(gridPoint.yLocation - battery.yLocation))
                gridPoint.manhattanDistance.append(distance)

                # If house on gridPoint, append distance to house
                for house in self.houses:
                    if (house.xLocation == gridPoint.xLocation and
                            house.yLocation == gridPoint.yLocation):
                        house.manhattanDistance.append(distance)

    def children(self, gridPoint):
        '''
        Returns gridpoint IDs for possible moves from current gridpoint.

        Args: self and gridPoint
        Returns: children
        '''

        # Calculate location of children
        childrenX = [gridPoint.xLocation - 1, gridPoint.xLocation,
                     gridPoint.xLocation + 1, gridPoint.xLocation]
        childrenY = [gridPoint.yLocation, gridPoint.yLocation - 1,
                     gridPoint.yLocation, gridPoint.yLocation + 1]

        children = []

        # Itterate over gridpoints and append gridpoints
        # that match x and y locations of children to a list
        for gridpoint in self.gridPoints:
            for i in range(4):
                if (gridpoint.xLocation == childrenX[i] and
                        gridpoint.yLocation == childrenY[i]):
                    children.append(gridpoint.ID)

        return children

import PythonCode.Classes.houseClass as houseClass
import PythonCode.Classes.batteryClass as batteryClass
import PythonCode.Classes.gridClass as gridClass
import numpy as np
import PythonCode.Algorithms.dijkstra as dijkstra
from matplotlib import pyplot as plt
import csv
