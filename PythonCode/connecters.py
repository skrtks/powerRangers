import copy
import random



"""This file contains several functions to distribute houses over batteries.
Only one has to be used, randomWithPreference gives best results"""


def randomWithPreference(smartGrid):
    """
    Finds connection for houses to batteries with preverence for batteries with
    the smallest manhattan distance. Only replaces connections when the total
    sum of manhatten distances is smaller than the total sum of the previous
    found connection.
    """

    print("connecting houses and batteries...")

    savedData = []
    backup = copy.deepcopy(smartGrid)
    numberOfLoops = 3
    bestScore = 100000

    for run in range(numberOfLoops):
        unconnected = len(smartGrid.houses)

        # Loop untill all houses are connected
        while unconnected > 0:

            # Copy houses and batteries to remember unshuffled order and set
            # changes back in new loop
            unconnected = len(smartGrid.houses)
            connecterScore = 0

            smartGrid = copy.deepcopy(backup)
            shuffledHouses = copy.deepcopy(backup.houses)
            shuffledBatteries = copy.deepcopy(backup.batteries)

            random.shuffle(shuffledHouses)

            # Loop trough random shuffled houses and batteries and connect
            for house in shuffledHouses:

                # Loop trough batteries sorted on closest manhattandistance for
                # current house
                sortedBatteries = sorted(shuffledBatteries, key=lambda battery:
                                         house.manhattanDistance[battery.ID])

                for battery in sortedBatteries:
                    if smartGrid.batteries[battery.ID].capacity >= smartGrid.houses[house.ID].power \
                            and not smartGrid.houses[house.ID].connected:
                        smartGrid.batteries[battery.ID].capacity -= house.power
                        smartGrid.batteries[battery.ID].connectedHouses.append(house.ID)
                        smartGrid.houses[house.ID].connected = True
                        smartGrid.houses[house.ID].batteryID = battery.ID
                        unconnected -= 1
                        connecterScore += house.manhattanDistance[battery.ID]
                        break

        # Remeber values of bestscore
        if connecterScore < bestScore:
            bestConfig = copy.deepcopy(smartGrid)
            bestScore = connecterScore

        savedData.append({"runs": run, "score": connecterScore,
                          "battery0": 0, "battery1": 0, "battery2": 0,
                          "battery3": 0, "battery4": 0})

        print("run: {}, bestscore: {}".format(run, bestScore))

    smartGrid = copy.deepcopy(bestConfig)
    return smartGrid, savedData


def randomConnecter(smartGrid):
    """
    Randomly distributes houses over batteries,
    stops when a solution is found.
    """

    print("distributing houses over batteries...")

    savedData = []
    unconnected = len(smartGrid.houses)
    backup = copy.deepcopy(smartGrid)

    while unconnected > 0:

        # Copy houses and batteries to remember unshuffled order and
        # set changes back in new loop
        unconnected = len(smartGrid.houses)
        connecterScore = 0
        run = 0

        smartGrid = copy.deepcopy(backup)
        shuffledHouses = copy.deepcopy(backup.houses)
        shuffledBatteries = copy.deepcopy(backup.batteries)

        random.shuffle(shuffledHouses)
        random.shuffle(shuffledBatteries)

        # Loop trough random shuffled houses and batteries and connect
        for house in shuffledHouses:
            for battery in shuffledBatteries:
                if (smartGrid.batteries[battery.ID].capacity >=
                    smartGrid.houses[house.ID].power and not
                    smartGrid.houses[house.ID].connected):
                    smartGrid.batteries[battery.ID].capacity -= house.power
                    (smartGrid.batteries[battery.ID].connectedHouses
                     .append(house.ID))
                    smartGrid.houses[house.ID].connected = True
                    smartGrid.houses[house.ID].batteryID = battery.ID
                    unconnected -= 1
                    connecterScore += house.manhattanDistance[battery.ID]
                    break
        run += 1

    savedData.append({"runs": run, "score": connecterScore,
                      "battery0": copy.deepcopy(smartGrid.batteries[0]
                                                .connectedHouses),
                      "battery1": copy.deepcopy(smartGrid.batteries[1]
                                                .connectedHouses),
                      "battery2": copy.deepcopy(smartGrid.batteries[2]
                                                .connectedHouses),
                      "battery3": copy.deepcopy(smartGrid.batteries[3]
                                                .connectedHouses),
                      "battery4": copy.deepcopy(smartGrid.batteries[4]
                                                .connectedHouses)})

    return smartGrid, savedData


def greedyAlgorithm(smartGrid):
    """"
    Connect all houses by sorting them on power, always gives the same solution.
    """

    savedData = []
    connecterScore = 0
    sortedPower = sorted(smartGrid.houses, key=lambda house: house.power,
                         reverse=True)

    # Loop trough batteries
    for battery in smartGrid.batteries:

        # Loop trough houses sorted on power (biggest to smallest power)
        for house in sortedPower:
            if battery.capacity >= house.power and not house.connected:
                battery.capacity -= house.power
                battery.connectedHouses.append(house.ID)
                smartGrid.houses[house.ID].connected = True
                smartGrid.houses[house.ID].batteryID = battery.ID
                connecterScore += house.manhattanDistance[battery.ID]

    savedData.append({"runs": 0, "score": connecterScore,
                      "battery0": copy.deepcopy(smartGrid.batteries[0]
                                                .connectedHouses),
                      "battery1": copy.deepcopy(smartGrid.batteries[1]
                                                .connectedHouses),
                      "battery2": copy.deepcopy(smartGrid.batteries[2]
                                                .connectedHouses),
                      "battery3": copy.deepcopy(smartGrid.batteries[3]
                                                .connectedHouses),
                      "battery4": copy.deepcopy(smartGrid.batteries[4]
                                                .connectedHouses)})

    return smartGrid, savedData

import random
import copy
import itertools
