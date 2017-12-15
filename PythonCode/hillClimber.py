from dijkstra import dijkstraSearch, reconstructPath
import csv
import random
import copy
from pathFinder import pathFinder

def hillClimber(smartGrid):

    print("hillClimbing...")
    savedData = []
    numberOfLoops = 3
    sameRuns = 0

    currentScore = calculateScore(smartGrid)
    bestScore = currentScore
    backup =  copy.deepcopy(smartGrid)

    for runs in range(numberOfLoops):
        swap(smartGrid)
        currentScore = calculateScore(smartGrid)
        if currentScore <= bestScore:
            backup = copy.deepcopy(smartGrid)
            bestScore = currentScore
            savedData.append({"runs": runs, "score": bestScore, "battery0": copy.deepcopy(smartGrid.batteries[0].connectedHouses), "battery1": copy.deepcopy(smartGrid.batteries[1].connectedHouses), "battery2": copy.deepcopy(smartGrid.batteries[2].connectedHouses), "battery3": copy.deepcopy(smartGrid.batteries[3].connectedHouses), "battery4": copy.deepcopy(smartGrid.batteries[4].connectedHouses)})
            sameRuns = 0
            print("runs: {}, currentScore: {}, bestScore: {}".format(runs, currentScore, bestScore))

        else:
            smartGrid = copy.deepcopy(backup)
            savedData.append({"runs": runs, "score": bestScore, "battery0": copy.deepcopy(smartGrid.batteries[0].connectedHouses), "battery1": copy.deepcopy(smartGrid.batteries[1].connectedHouses), "battery2": copy.deepcopy(smartGrid.batteries[2].connectedHouses), "battery3": copy.deepcopy(smartGrid.batteries[3].connectedHouses), "battery4": copy.deepcopy(smartGrid.batteries[4].connectedHouses)})
            sameRuns += 1
            print("runs: {}, currentScore: {}, bestScore: {}".format(runs, currentScore, bestScore))

        if sameRuns == 150:
            return savedData, smartGrid

    return savedData, smartGrid


def calculateScore(smartGrid):
    totalScore = 0
    for battery in smartGrid.batteries:
        for houseID in battery.connectedHouses:
            # Oude AStar!
            resultPathFinder = pathFinder(battery, smartGrid, houseID)
            smartGrid.houses[houseID].score = resultPathFinder["score"]
            totalScore += resultPathFinder["score"]

    for point in smartGrid.gridPoints:
        point.cable = [9, 9, 9, 9, 9]
        for house in smartGrid.houses:
            if point.ID == house.gridID:
                #cost of gridPoint if house on gridpoint
                point.cable = [5000, 5000, 5000, 5000, 5000]

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
    spaceRHBat = smartGrid.batteries[randomHouse.batteryID].capacity + randomHouse.power

    # Loop through houses
    for house in sortedHouses:

        # Check if house is not in same battery and space is sufficient
        if house.batteryID is not randomHouse.batteryID and house.power <= spaceRHBat:
            spaceSHBat = smartGrid.batteries[house.batteryID].capacity + house.power
            if randomHouse.power <= spaceSHBat:

                smartGrid.batteries[house.batteryID].connectedHouses.remove(house.ID)
                smartGrid.batteries[randomHouse.batteryID].connectedHouses.append(house.ID)
                smartGrid.batteries[randomHouse.batteryID].connectedHouses.remove(randomHouse.ID)
                smartGrid.batteries[house.batteryID].connectedHouses.append(randomHouse.ID)

                (house.batteryID, randomHouse.batteryID) = (randomHouse.batteryID, house.batteryID)

                break
