import csv
from houseClass import house as houseClass
from batteryClass import battery as batteryClass
from gridClass import gridPoint as gridClass

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
            houseClass.houses.append(houseClass(ID, int(row[0]), int(row[1]), float(row[2])))
            ID += 1

        ID = 0
        for row in readerBatteries:
            batteryClass.batteries.append(batteryClass(ID, int(row[0]), int(row[1]), float(row[2])))
            ID += 1


def manhattanDistance(gridPoints, batteries):
    """"Calculate mannhattendistance for avery gridpoint to batteries"""

    # Loop trough batteries and gridpoints calculate manhattendistance between them
    for battery in batteries:
        for gridPoint in gridClass.gridPoints:
            distance = abs(gridPoint.xLocation - battery.xLocation) + abs(gridPoint.yLocation - battery.yLocation)
            gridPoint.manhattanDistance.append(distance)
            gridPoint.cable.append(9)

            # If house on gridPoint, append distance to house
            for house in houseClass.houses:
                if house.xLocation == gridPoint.xLocation and house.yLocation == gridPoint.yLocation:
                    house.manhattanDistance.append(distance)



def children(gridPoint, gridPoints):
    '''returns gridpoint ID's for possible moves from current gridpoint'''

    # Calculate possible locations for x and y
    childrenX = [gridPoint.xLocation - 1, gridPoint.xLocation, gridPoint.xLocation + 1, gridPoint.xLocation]
    childrenY = [gridPoint.yLocation, gridPoint.yLocation - 1, gridPoint.yLocation, gridPoint.yLocation + 1]

    children = []

    # Itterate over gridpoints and append gridpoints that match x and y locations of children to a list
    for gridpoint in gridClass.gridPoints:
        for i in range(4):
            if gridpoint.xLocation == childrenX[i] and gridpoint.yLocation == childrenY[i]:
                children.append(gridpoint.ID)

    return children
