class smartGrid:

    def __init__(self):
        self.gridPoints = []
        self.houses = []
        self.batteries = []

    def gridFiller(self):
        """"
        Create grid
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
        Assign gridID to houses and batteries
        Change cable cost of gridPoint if it has a house on it
        returns: True if succes
        """

        for point in self.gridPoints:
            for house in self.houses:
                if (point.xLocation == house.xLocation and
                point.yLocation == house.yLocation):
                    house.gridID = point.ID
                    point.cable = [5000, 5000, 5000, 5000, 5000]
            for battery in self.batteries:
                if (point.xLocation == battery.xLocation and
                        point.yLocation == battery.yLocation):
                    battery.gridID = point.ID
        return True

    def gridDrawer(self):
        """"
        Draw grid with batteries, houses and connections
        """

        # The price of laying a cable underneath a house
        priceUnderHouse = 5000

        # The price of five batteries
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
        colors = ["firebrick", "g", "blue", "deeppink", "darkorange"]

        numberOfCables = {}

        for point in self.gridPoints:
          numberOfCables[point.ID] = 0

        for battery in self.batteries:

            closed = set()
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
                    # decrease cable cost if it's not already 'free'
                    if self.gridPoints[point].cable[battery.ID] != 0:
                        self.gridPoints[point].cable[battery.ID] -= 9

                # Append route of cables to battery
                pathX = []
                pathY = []


                for ID in path:
                  if ID in closed:
                    pathX.append(self.gridPoints[ID].xLocation)
                    pathY.append(self.gridPoints[ID].yLocation)
                    closed.add(ID)
                    break
                  else:
                    pathX.append(self.gridPoints[ID].xLocation + numberOfCables[ID])
                    pathY.append(self.gridPoints[ID].yLocation + numberOfCables[ID])
                    numberOfCables[ID] += 0.2
                    closed.add(ID)

                # Draw cables
                plt.plot(pathX, pathY, color)

        # Make points for houses and batteries
        plt.plot(xHouse, yHouse, "k.")
        plt.plot(xBattery, yBattery, marker="s", color="blue", ls='None')

        # Draw batteries
        for battery in self.batteries:
            ax.annotate(battery.ID, (xBattery[battery.ID],
                                     yBattery[battery.ID]))

        # Show graph and cost of smartGrid
        totalCost = totalScore + costBatteries
        plt.title("Cable cost: " + str(totalScore) + " Battery cost: 25000 " +
                  "Total cost: " + str(totalCost))
        plt.show()

    def fileReader(self, fileHouses, fileBatteries):
        """"
        Read information of houses and batteries from files
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
        """"
        Calculate mannhattandistance for every gridpoint to batteries
        """

        # Loop trough batteries and gridpoints calculate
        # manhattandistance between them
        for battery in self.batteries:
            for gridPoint in self.gridPoints:
                distance = (abs(gridPoint.xLocation - battery.xLocation)
                            + abs(gridPoint.yLocation - battery.yLocation))
                gridPoint.manhattanDistance.append(distance)
                gridPoint.cable.append(9)

                # If house on gridPoint, append distance to house
                for house in self.houses:
                    if (house.xLocation == gridPoint.xLocation and
                            house.yLocation == gridPoint.yLocation):
                        house.manhattanDistance.append(distance)

    def children(self, gridPoint):
        '''
        returns gridpoint IDs for possible moves from current gridpoint
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

import houseClass
import batteryClass
import gridClass
import numpy as np
import dijkstra as dijkstra
from matplotlib import pyplot as plt
import csv
