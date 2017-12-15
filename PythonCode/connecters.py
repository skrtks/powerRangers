def connectWithBatteries(smartGrid):
    """"Connect houses with nearest batteries """

    sortedPower = sorted(smartGrid.houses, key=lambda house: house.power, reverse=True)

    # Loop trough houses sorted on power (biggest to smallest power)
    for house in sortedPower:
        sortedBatteries = sorted(smartGrid.batteries, key=lambda battery: house.manhattanDistance[battery.ID])

        # Loop trough batteries sorted on manhattanDistance (smallest to biggest manhattanDistance)
        for battery in sortedBatteries:
            if battery.capacity >= house.power:
                battery.capacity  = house.power
                battery.connectedHouses.append(house.ID)
                house.batteryId = battery.ID
                house.connected = True
                break

    return True

def connectWithHouses1(smartGrid):
    """ Connect batteries with nearest houses """

    # Loop trough batteries
    for battery in smartGrid.batteries:
        sortedHouses = sorted(smartGrid.houses, key=lambda house: house.manhattanDistance[battery.ID])

        # Loop trough houses sorted on manhattanDistance (smallest to biggest manhattanDistance)
        for house in sortedHouses:
            if battery.capacity > house.power and not house.connected:
                battery.capacity  = house.power
                battery.connectedHouses.append(house.ID)
                house.batteryId = battery.ID
                house.connected = True

    return True

def connectWithHouses2(smartGrid):
    """Connect batteries with nearest houses, let every battery pick one house at a time"""

    unconnected = len(smartGrid.houses)

    while unconnected > 2:

        # Loop trough batteries
        for battery in smartGrid.batteries:
            sortedHouses = sorted(smartGrid.houses, key=lambda house: house.manhattanDistance[battery.ID])

            # Loop trough houses sorted on manhattanDistance (smallest to biggest manhattanDistance)
            for house in sortedHouses:
                if battery.capacity > house.power and not house.connected:
                    battery.capacity  = house.power
                    battery.connectedHouses.append(house.ID)
                    house.connected = True
                    house.batteryId = battery.ID
                    unconnected  = 1
                    break

    return True

def greedyAlgorithm(smartGrid):
    """"Connect all houses by sorting them on power"""

    sortedPower = sorted(smartGrid.houses, key=lambda house: house.power, reverse=True)

    # Loop trough batteries
    for battery in smartGrid.batteries:

        # Loop trough houses sorted on power (biggest to smallest power)
        for house in sortedPower:
            if battery.capacity >= house.power and not house.connected:
                battery.capacity  = house.power
                battery.connectedHouses.append(house.ID)
                house.connected = True
                house.batteryId = battery.ID
                house.connected = True

    return True


def randomConnecter(smartGrid):
    """Makes random connection for batteries and houses"""

    unconnected = len(smartGrid.houses)
    backup = copy.deepcopy(smartGrid)
    print(unconnected)
    print(smartGrid.batteries[0].connectedHouses)
    # Loop untill all houses are connected
    while unconnected >= 1:
        # Copy houses and batteries to remember unshuffled order and set changes back in new loop
        unconnected = len(smartGrid.houses)

        smartGrid = copy.deepcopy(backup)
        shuffledHouses = copy.deepcopy(backup.houses)
        shuffledBatteries = copy.deepcopy(backup.batteries)

        random.shuffle(shuffledHouses)
        random.shuffle(shuffledBatteries)

        # Loop trough random shuffled houses and batteries and connect
        for house in shuffledHouses:
            for battery in shuffledBatteries:
                if smartGrid.batteries[battery.ID].capacity >= smartGrid.houses[house.ID].power and not smartGrid.houses[house.ID].connected:
                    smartGrid.batteries[battery.ID].capacity  = house.power
                    smartGrid.batteries[battery.ID].connectedHouses.append(house.ID)
                    smartGrid.houses[house.ID].connected = True
                    smartGrid.houses[house.ID].batteryId = battery.ID
                    unconnected  = 1
                    break

    return smartGrid


def randomWithPreverence(smartGrid):
    """Find connection for houses to batteries with preverence for batteries with
    the smallest manhattan distance. Only replaces connections when the total sum
    of manhatten distances is smaller than the total sum of the previous found connection"""

    maxScore = 100000
    houseOrderX = []
    houseOrderY = []
    bestScore = maxScore

    shuffledHouses = copy.deepcopy(smartGrid.houses)

    for x in range(100):
        print(x)
        connecterScore = 0
        shuffledHousesX = []
        shuffledHousesY = []
        random.shuffle(shuffledHouses)
        connectedTemp = {0: [], 1: [], 2: [], 3: [], 4: []}

        # Set values back to begin values
        for house in shuffledHouses:
            house.connected = False

        for battery in smartGrid.batteries:
            battery.capacity = 1507
            # battery.connectedHouses = []

        # Connect shuffledhouses with preverence for closest batteries
        for house in shuffledHouses:
            shuffledHousesX.append(house.xLocation)
            shuffledHousesY.append(house.yLocation)

            sortedBatteries = sorted(smartGrid.batteries, key=lambda battery: house.manhattanDistance[battery.ID])
            # random.shuffle(smartGrid.batteries)

            for battery in sortedBatteries:
                if battery.capacity >= house.power:
                    battery.capacity -= house.power
                    connectedTemp[battery.ID].append(house.ID)
                    house.connected = True
                    #house.batteryId = battery.ID
                    connecterScore += house.manhattanDistance[battery.ID]
                    break

            # Set connecterscore to 10000 when a house is not connected to make sure it's not an option
            for house in shuffledHouses:
                if not house.connected:
                    connecterScore = maxScore

            # Remeber values of bestscore
            if connecterScore < bestScore:
                bestScore = connecterScore

    for battery in smartGrid.batteries:
        battery.connectedHouses = connectedTemp[battery.ID]

    for houseID in battery.connectedHouses:
        smartGrid.houses[houseID].batteryId = battery.ID

     # Print statements for checking.
    for battery in smartGrid.batteries:
        print("battery capacity[{}]: {}".format(battery.ID, battery.capacity))

    for house in shuffledHouses:
        if not house.connected:
            print("unconnected house(s): {}".format(house.ID))
            print("power supply unconnected house(s): {}".format(house.power))


import random
import copy
import itertools
