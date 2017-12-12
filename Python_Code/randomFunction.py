import itertools
import random
import copy
from smartGrid import smartGrid

def randomFunction():
    """Find best connection for batteries and houses """

    maxScore = 100000
    houseOrderX = []
    houseOrderY = []
    bestScore = maxScore

    shuffledHouses = copy.deepcopy(smartGrid.houses)

    for x in range(200):
        #print(x)
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

                    #print("BatID: {}, ConnectedHouses: {}, house.batteryID: {}, house.ID: {}".format(battery.ID, battery.connectedHouses, shuffledHouses[houseID].batteryId, shuffledHouses[houseID].ID))
                    #print("houseIDold: {}, batteryIDold: {}".format(shuffledHouses[houseID].ID, shuffledHouses[houseID].batteryId))

                # print("battery[{}]: {}".format(battery.ID, battery.connectedHouses))

        #print("bestScore : {}".format(bestScore))
        #print("connecterScore : {}".format(connecterScore))

    # # Print statements for checking.
    # for battery in smartGrid.batteries:
    #     print("battery capacity[{}]: {}".format(battery.ID, battery.capacity))
    #
    # for house in shuffledHouses:
    #     if not house.connected:
    #         print("unconnected house(s): {}".format(house.ID))
    #         print("power supply unconnected house(s): {}".format(house.power))
    #
    # print(len(houseOrderX), len(houseOrderY))
    # print(houseOrderX, houseOrderY)

# return [houseOrderX, houseOrderY, bestScore]
# [xHouse,yHouse,s] = optimalizationAlgorithm()
# print(s)
