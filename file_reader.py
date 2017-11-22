import csv
import numpy as np
import itertools
import aStar as aStar
from houseClass import house
from batteryClass import battery
from gridClass import gridPoint
from matplotlib import pyplot as plt


# Initiate global variables
houses = []
sortedHouses = []
batteries = []
gridPoints = []


def main():
    file_reader("Huizen&Batterijen/wijk1_huizen.csv",
                "Huizen&Batterijen/wijk1_batterijen.csv")
    grid_filler()
    manhattanDistance(gridPoints, batteries)
    connecter()
    draw_grid()

def grid_filler():
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


def file_reader(file_houses, file_batteries):
    """"Read information of houses and batteries from files"""

    # Initiate ID.
    ID = 0

    # Open the file containing houses
    with open(file_houses) as h, open(file_batteries) as b:

        # Read the file and separate values in list.
        reader_houses = csv.reader(h, delimiter=',', quoting=csv.QUOTE_NONE)
        reader_batteries = csv.reader(b, delimiter=',', quoting=csv.QUOTE_NONE)

        # Skip the header of the file.
        next(h)
        next(b)

        # Create instances of houses or batteries.
        for row in reader_houses:
            houses.append(house(ID, int(row[0]), int(row[1]), float(row[2])))
            ID += 1

        ID = 0
        for row in reader_batteries:
            batteries.append(battery(ID, int(row[0]), int(row[1]), float(row[2])))
            ID += 1


def draw_grid():
    """"Draw grid with batteries, houses and connections"""

    # Initiate list for coordinates from houses and batteries
    x_h = []
    y_h = []
    x_b = []
    y_b = []

    # Fill lists with coordinates
    for house in houses:
        x_h.append(house.xLocation)
        y_h.append(house.yLocation)

    for battery in batteries:
        x_b.append(battery.xLocation)
        y_b.append(battery.yLocation)

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

    # # Draw lines
    # for battery in batteries:
    #     xBat.append(battery.xLocation)
    #     yBat.append(battery.yLocation)
    #
    #     for house in battery.connectedHouses:
    #         xBat.append(houses[house].xLocation)
    #         yBat.append(houses[house].yLocation)
    #         plt.plot(xBat, yBat)
    #         xBat = [battery.xLocation]
    #         yBat = [battery.yLocation]
    #     xBat = []
    #     yBat = []

    # Loop through all batteries and houses.
    totalScore = 0
    colors = ["firebrick", "g", "blue", "deeppink", "darkorange"]
    for battery in batteries:
        color = colors[battery.ID]
        for houseID in battery.connectedHouses:

            returnValues = aStar.aStar(battery, houses, houseID, gridPoints)
            path = returnValues["path"]
            totalScore += returnValues["score"]

            path_x = []
            path_y = []

            for ID in path:
                path_x.append(gridPoints[ID].xLocation)
                path_y.append(gridPoints[ID].yLocation)

            # print(path_x)
            # print(path_y)

            # Make points for houses and batteries
            plt.plot(path_x, path_y, color)


    # Make points for houses and batteries
    plt.plot(x_h, y_h, "k.")
    plt.plot(x_b, y_b, "bD")

    print("Score is: {}".format(totalScore))
    plt.show()


def connecter():
    """"Connect houses with nearest batteries """

    # unconnected = len(houses)
    #
    # while unconnected > 0:
    #     for battery in batteries:
    #         sortedHouses = sorted(houses, key=lambda house: house.manhattanDistance[battery.ID])
    #         for house in sortedHouses:
    #             if battery.capacity > house.power and not house.connected:
    #                 battery.capacity -= house.power
    #                 battery.connectedHouses.append(house.ID)
    #                 house.connected = True
    #                 unconnected -= 1
    #                 print("connected")
    #                 break
    #         print("next bat")

    # Connect batteries sorted on power output house
    sortedPower = sorted(houses, key=lambda house: house.power, reverse=True)
    for house in sortedPower:
        while not house.connected:
            for battery in batteries:
                if house.manhattanDistance[battery.ID] == min(house.manhattanDistance):
                    if battery.capacity >= house.power:
                        battery.capacity -= house.power
                        battery.connectedHouses.append(house.ID)
                        house.connected = True
                        break
                    else:
                        house.manhattanDistance[battery.ID] = 999


    for house in houses:
        print(house.connected)


    # # Loop trough batteries and sort houses on shortest manhattenDistance for every battery
    # for battery in batteries:
    #     sortedHouses = sorted(houses, key=lambda house: house.manhattanDistance[battery.ID])
    #
    #     # Loop trough sorted houses and connect house with battery if enough capacity
    #     for house in sortedHouses:
    #         if battery.capacity > house.power and not house.connected:
    #             battery.capacity -= house.power
    #             battery.connectedHouses.append(house.ID)
    #             house.connected = True

    # Print statements for checking.
    for battery in batteries:
        print("battery capacity[{}]: {}".format(battery.ID, battery.capacity))

    for house in sortedHouses:
        if not house.connected:
            print("unconnected house(s): {}".format(house.ID))
            print("power supply unconnected house(s): {}".format(house.power))

def manhattanDistance(gridPoints, batteries):
    """"Calculate mannhattendistance for avery gridpoint to batteries"""

    # Loop trough batteries and gridpoints calculate manhattendistance between them
    for battery in batteries:
        for gridPoint in gridPoints:
            distance = abs(gridPoint.xLocation - battery.xLocation) + abs(gridPoint.yLocation - battery.yLocation)
            gridPoint.manhattanDistance.append(distance)
            gridPoint.cable.append(9)

            # If house on gridPoint, append distance to house
            for house in houses:
                if house.xLocation == gridPoint.xLocation and house.yLocation == gridPoint.yLocation:
                    house.manhattanDistance.append(distance)

    # print(houses[1].manhattanDistance)
    # print(gridPoints[1].xLocation)
    # print(gridPoints[1].yLocation)


def children(gridPoint, gridPoints):
    '''returns gridpoint ID's for possible moves from current gridpoint'''

    # Calculate possible locations for x and y
    childrenX = [gridPoint.xLocation - 1, gridPoint.xLocation, gridPoint.xLocation + 1, gridPoint.xLocation]
    childrenY = [gridPoint.yLocation, gridPoint.yLocation - 1, gridPoint.yLocation, gridPoint.yLocation + 1]

    children = []

    # Itterate over gridpoints and append gridpoints that match x and y locations of children to a list
    for gridpoint in gridPoints:
        for i in range(4):
            if gridpoint.xLocation == childrenX[i] and gridpoint.yLocation == childrenY[i]:
                children.append(gridpoint.ID)

    return children

if __name__ == "__main__":
    main()
