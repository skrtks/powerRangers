from dijkstra import dijkstraSearch, reconstructPath
import csv
import random
import copy
import math
from pathFinder import pathFinder


def simulatedAnnealing(smartGrid):
"""
Swaps houses several times to get a lower cost for configuration.

Args: smartgrid
Returns: totalScore
"""

    savedData = []
    numberOfLoops = 10

    # Set initial temp
    temp = 10000

    # Set cooling rate
    coolingRate = 16

    sameRuns = 0

    currentScore = calculateScore(smartGrid)
    bestScore = currentScore
    runs = 0
    backup = copy.deepcopy(smartGrid)

    while temp > 1:
        swap(smartGrid)
        newScore = calculateScore(smartGrid)
        if (acceptanceProbability(currentScore, newScore, temp)
            > random.random()):
            currentScore = newScore
            savedData.append({"runs": runs, "score": bestScore,
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

            print("runs: {}, currentScore: {}, bestScore: {}"
                  .format(runs, currentScore, bestScore))
            sameRuns = 0

        else:
            smartGrid = copy.deepcopy(backup)
            savedData.append({"runs": runs, "score": bestScore,
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

            print("runs: {}, currentScore: {}, bestScore: {}"
                  .format(runs, currentScore, bestScore))
            sameRuns += 1

        if currentScore < bestScore:
            bestScore = currentScore

        for point in smartGrid.gridPoints:
            point.cost = [9, 9, 9, 9, 9]

        if sameRuns == 250:
            return savedData, smartGrid

        temp -= coolingRate
        runs += 1

    return savedData, smartGrid


def calculateScore(smartGrid):
"""
Calculate score of smartGrid configuration.

Args: smartGrid
Returns: totalScore
"""
    totalScore = 0

    for battery in smartGrid.batteries:
        for houseID in battery.connectedHouses:
            resultPathFinder = pathFinder(battery, smartGrid, houseID)
            smartGrid.houses[houseID].score = resultPathFinder["score"]
            totalScore += resultPathFinder["score"]

    for point in smartGrid.gridPoints:
        point.cost = [9, 9, 9, 9, 9]

    return totalScore


def swap(smartGrid):
"""
Swap houses from different batteries if battery has sufficient capacity.
Picks a random house to swap but has a preference to swap with a house that
has the highest gridPoint cost.

Args: smartGrid
"""

    sortedHouses = sorted(smartGrid.houses, key=lambda house: house.score,
                          reverse=True)

    # Select random house
    randomHouse = random.choice(smartGrid.houses)

    # Calculate space in battery connected to random house
    spaceRHBat = smartGrid.batteries[randomHouse.batteryID].capacity
    + randomHouse.power

    # Loop through houses
    for house in sortedHouses:
        # Check if house is not in same battery and space is sufficient
        if (house.batteryID is not randomHouse.batteryID and
            house.power <= spaceRHBat):

            spaceSHBat = (smartGrid.batteries[house.batteryID].capacity
                          + house.power)
            if randomHouse.power <= spaceSHBat:

                (smartGrid.batteries[house.batteryID].connectedHouses
                 .remove(house.ID))
                (smartGrid.batteries[randomHouse.batteryID].connectedHouses
                 .append(house.ID))
                (smartGrid.batteries[randomHouse.batteryID].connectedHouses
                 .remove(randomHouse.ID))
                (smartGrid.batteries[house.batteryID].connectedHouses
                 .append(randomHouse.ID))
                (house.batteryID, randomHouse.batteryID) = (randomHouse
                                                            .batteryID,
                                                            house.batteryID)

                break

def acceptanceProbability(currentScore, bestScore, temp):
"""

Args: currentScore, bestScore, temp
Returns: 
"""
    if currentScore < bestScore:
        return 1
    else:
        return math.exp((bestScore - currentScore) / temp)
