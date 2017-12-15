from dijkstra import dijkstraSearch, reconstructPath
import csv
import random
import copy
import math
from pathFinder import pathFinder

def simulatedAnnealing(smartGrid):

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
    backup =  copy.deepcopy(smartGrid)

    for point in smartGrid.gridPoints:
        point.cable = [9, 9, 9, 9, 9]


    while temp > 1:
        swap(smartGrid)
        newScore = calculateScore(smartGrid)
        if acceptanceProbability(currentScore, newScore, temp) > random.random():
            currentScore = newScore
            savedData.append({"runs": runs, "score": bestScore, "battery0": copy.deepcopy(smartGrid.batteries[0].connectedHouses), "battery1": copy.deepcopy(smartGrid.batteries[1].connectedHouses), "battery2": copy.deepcopy(smartGrid.batteries[2].connectedHouses), "battery3": copy.deepcopy(smartGrid.batteries[3].connectedHouses), "battery4": copy.deepcopy(smartGrid.batteries[4].connectedHouses)})
            print("runs: {}, currentScore: {}, bestScore: {}".format(runs, currentScore, bestScore))
            sameRuns = 0

        else:
            smartGrid = copy.deepcopy(backup)
            savedData.append({"runs": runs, "score": bestScore, "battery0": copy.deepcopy(smartGrid.batteries[0].connectedHouses), "battery1": copy.deepcopy(smartGrid.batteries[1].connectedHouses), "battery2": copy.deepcopy(smartGrid.batteries[2].connectedHouses), "battery3": copy.deepcopy(smartGrid.batteries[3].connectedHouses), "battery4": copy.deepcopy(smartGrid.batteries[4].connectedHouses)})
            print("runs: {}, currentScore: {}, bestScore: {}".format(runs, currentScore, bestScore))
            sameRuns += 1

        if currentScore < bestScore:
            bestScore = currentScore

        for point in smartGrid.gridPoints:
            point.cable = [9, 9, 9, 9, 9]

        if sameRuns == 250:
            return savedData, smartGrid

        temp -= coolingRate
        runs += 1

    return savedData, smartGrid


def calculateScore(smartGrid):
    totalScore = 0
    for battery in smartGrid.batteries:
        for houseID in battery.connectedHouses:
            # Oude AStar!
            resultPathFinder = pathFinder(battery, smartGrid, houseID)
            smartGrid.houses[houseID].score = resultPathFinder["score"]
            totalScore += resultPathFinder["score"]

    return totalScore

    # Dijkstra!
    # # generate dijkstra path
    # (cameFrom, score) = dijkstraSearch(battery, smartGrid, house.ID, battery.ID)
    # totalScore += score[battery.gridID]
    #
    # # reconstruct the path
    # path = reconstructPath(cameFrom, smartGrid.houses[houseID].gridID, battery.gridID)
    #
    # # update the costs for the gridpoints
    # for point in path:
    #     smartGrid.gridPoints[point].cable[battery.ID] = 0


def swap(smartGrid):
    sortedHouses = sorted(smartGrid.houses, key=lambda house: house.score, reverse=True)

    # Select random house.
    randomHouse = random.choice(smartGrid.houses)

    # Calculate space in battery connected to random house
    spaceRHBat = smartGrid.batteries[randomHouse.batteryId].capacity + randomHouse.power

    # Loop through houses
    for house in sortedHouses:

        # Check if house is not in same battery and space is sufficient
        if house.batteryId is not randomHouse.batteryId and house.power <= spaceRHBat:
            spaceSHBat = smartGrid.batteries[house.batteryId].capacity + house.power
            if randomHouse.power <= spaceSHBat:
                # print("randomhouse {}".format(randomHouse.ID))
                # print("Connectedhousesbat0 = {}" .format(smartGrid.batteries[0].connectedHouses))
                # print("Connectedhousesbat1 = {}" .format(smartGrid.batteries[1].connectedHouses))
                # print("Connectedhousesbat2 = {}" .format(smartGrid.batteries[2].connectedHouses))
                # print("Connectedhousesbat3 = {}" .format(smartGrid.batteries[3].connectedHouses))
                # print("Connectedhousesbat4 = {}" .format(smartGrid.batteries[4].connectedHouses))
                # print("houseID: {}, batteryID for houseID: {}".format(house.ID, house.batteryId))

                smartGrid.batteries[house.batteryId].connectedHouses.remove(house.ID)
                # print("battery {} removed {}".format(smartGrid.batteries[house.batteryId].ID, house.ID))
                smartGrid.batteries[randomHouse.batteryId].connectedHouses.append(house.ID)
                # print("battery {} append {}".format(smartGrid.batteries[randomHouse.batteryId].ID, house.ID))
                smartGrid.batteries[randomHouse.batteryId].connectedHouses.remove(randomHouse.ID)
                # print("battery {} remove {}".format(smartGrid.batteries[randomHouse.batteryId].ID, randomHouse.ID))
                smartGrid.batteries[house.batteryId].connectedHouses.append(randomHouse.ID)
                # print("battery {} append {}".format(smartGrid.batteries[house.batteryId].ID, randomHouse.ID))

                # print("bat with house {}, bat with randomHouse {}".format(house.batteryId, randomHouse.batteryId))
                (house.batteryId, randomHouse.batteryId) = (randomHouse.batteryId, house.batteryId)
                # print("after swap: bat with house {}, bat with randomHouse {}".format(house.batteryId, randomHouse.batteryId))
                # print("__________________________________")
                # print("Connectedhousesbat0 = {}" .format(smartGrid.batteries[0].connectedHouses))
                # print("Connectedhousesbat1 = {}" .format(smartGrid.batteries[1].connectedHouses))
                # print("Connectedhousesbat2 = {}" .format(smartGrid.batteries[2].connectedHouses))
                # print("Connectedhousesbat3 = {}" .format(smartGrid.batteries[3].connectedHouses))
                # print("Connectedhousesbat4 = {}" .format(smartGrid.batteries[4].connectedHouses))
                # print("houseID: {}, batteryID for houseID: {}".format(house.ID, house.batteryId))

                break

def acceptanceProbability(currentScore, bestScore, temp):
    if currentScore < bestScore:
        return 1
    else:
        return math.exp((bestScore - currentScore) / temp)
