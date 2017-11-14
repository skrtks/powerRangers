import csv
import numpy as np
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
    children(gridPoints[0], gridPoints)



def grid_filler():

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

    # Initiate ID.
    ID = 0

    # Open the file containing houses.
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
        # get coordinates
        x_h = []
        y_h = []
        x_b = []
        y_b = []

        for i in range(150):
            x_h.append(houses[i].xLocation)
            y_h.append(houses[i].yLocation)

        for i in range(5):
            x_b.append(batteries[i].xLocation)
            y_b.append(batteries[i].yLocation)

        fig = plt.figure()
        plt.axis([-1, 51, -1, 51])
        ax = fig.add_subplot(1, 1, 1)

        ax.set_xticks(np.arange(0, 51, 1), minor=True)
        ax.set_yticks(np.arange(0, 51, 1), minor=True)

        # or if you want different settings for the grids:
        ax.grid(which='minor', alpha=0.2, linestyle='-')
        ax.grid(which='major', alpha=0.5, linestyle='-')

        xBat = []
        yBat = []

        for battery in batteries:
            xBat.append(battery.xLocation)
            yBat.append(battery.yLocation)

            for ID in battery.connectedHouses:
                xBat.append(houses[ID].xLocation)
                yBat.append(houses[ID].yLocation)
                plt.plot(xBat, yBat)
                xBat = [battery.xLocation]
                yBat = [battery.yLocation]

        fig = plt.figure()
        plt.axis([-1, 51, -1, 51])
        ax = fig.add_subplot(1, 1, 1)
        plt.plot(x_h, y_h, "ro")
        plt.plot(x_b, y_b, "D")

        ax.set_xticks(np.arange(0, 51, 1), minor=True)
        ax.set_yticks(np.arange(0, 51, 1), minor=True)

        # or if you want different settings for the grids:
        ax.grid(which='minor', alpha=0.2, linestyle='-')
        ax.grid(which='major', alpha=0.5, linestyle='-')

        plt.show()


def connecter():
    for battery in batteries:
        sortedHouses = sorted(houses, key=lambda house: house.manhattanDistance[battery.ID])

        for house in sortedHouses:
            if battery.capacity > house.power and not house.connected:
                battery.capacity -= house.power
                battery.connectedHouses.append(house.ID)
                house.connected = True

def manhattanDistance(gridPoints, batteries):
    for battery in batteries:
        for gridPoint in gridPoints:
            distance = abs(gridPoint.xLocation - battery.xLocation) + abs(gridPoint.yLocation - battery.yLocation)
            gridPoint.manhattanDistance.append(distance)

            # If house on gridPoint, append distance to house
            for house in houses:
                if house.xLocation == gridPoint.xLocation and house.yLocation == gridPoint.yLocation:
                    house.manhattanDistance.append(distance)

    print(houses[1].manhattanDistance)
    print(gridPoints[1].xLocation)
    print(gridPoints[1].yLocation)

def children(gridPoint, gridPoints):
    '''returns gridpoint ID's for possible moves from current gridpoint'''

    # calculate possible locations for x and y
    childrenX = [gridPoint.xLocation - 1, gridPoint.xLocation, gridPoint.xLocation + 1, gridPoint.xLocation]
    childrenY = [gridPoint.yLocation, gridPoint.yLocation -1, gridPoint.yLocation, gridPoint.yLocation +1]

    children = []

    # itterate over gridpoints and append gridpoints that match x and y locations of children to a list
    for gridpoint in gridPoints:
        for i in range(4):
            if gridpoint.xLocation == childrenX[i] and gridpoint.yLocation == childrenY[i]:
                children.append(gridpoint.ID)

    return children

if __name__ == "__main__":
    main()
