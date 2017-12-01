import itertools
import random
from houseClass import house as houseClass
from batteryClass import battery as batteryClass

def optimalizationAlgorithm(houses, batteries):
    """Find best connection for batteries and houses """

    maxScore = 100000
    houseOrderX = []
    houseOrderY = []
    bestScore = maxScore
    for x in range(200):
        #print(x)
        connecterScore = 0
        shuffledHousesX = []
        shuffledHousesY = []
        random.shuffle(houses)

        # Set values back to begin values
        for house in houses:
            house.connected = False

        for battery in batteries:
            battery.capacity = 1507
            battery.connectedHouses = []

        # Connect shuffledhouses with preverence for closest batteries
        for house in houses:
            shuffledHousesX.append(house.xLocation)
            shuffledHousesY.append(house.yLocation)

            sortedBatteries = sorted(batteries, key=lambda battery: house.manhattanDistance[battery.ID])
            # random.shuffle(batteries)

            for battery in sortedBatteries:
                if battery.capacity >= house.power:
                    battery.capacity -= house.power
                    battery.connectedHouses.append(house.ID)
                    house.connected = True
                    connecterScore += house.manhattanDistance[battery.ID]
                    break

        # Set connecterscore to 10000 when a house is not connected to make sure it's not an option
        for house in houses:
            if house.connected == False:
                connecterScore = maxScore

        # Remeber values of bestscore
        if connecterScore < bestScore:
            houseOrderX = shuffledHousesX
            houseOrderY = shuffledHousesY
            bestScore = connecterScore
        print("bestScore : {}".format(bestScore))
        print("connecterScore : {}".format(connecterScore))

    # Print statements for checking.
    for battery in batteries:
        print("battery capacity[{}]: {}".format(battery.ID, battery.capacity))

    for house in houses:
        if not house.connected:
            print("unconnected house(s): {}".format(house.ID))
            print("power supply unconnected house(s): {}".format(house.power))

    print(len(houseOrderX), len(houseOrderY))
    print(houseOrderX, houseOrderY)

# return [houseOrderX, houseOrderY, bestScore]
# [xHouse,yHouse,s] = optimalizationAlgorithm()
# print(s)
