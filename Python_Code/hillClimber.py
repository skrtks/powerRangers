from dijkstra import dijkstraSearch, reconstructPath
from randomFunction import randomFunction
from smartGrid import smartGrid
import csv
import random
import copy
from pathFinder import pathFinder

def hillClimber():


    savedData = []
    runs = 0
    sameRuns = 0
    bestScore = 100000
    numberOfLoops = 100000

    for x in range(numberOfLoops):
        for point in smartGrid.gridPoints:
            point.cable = [9, 9, 9, 9, 9]
        totalScore = 0
        for battery in smartGrid.batteries:
            for houseID in battery.connectedHouses:
                # Oude AStar!
                resultPathFinder = pathFinder(battery, smartGrid.houses, houseID, smartGrid.gridPoints)
                smartGrid.houses[houseID].score = resultPathFinder["score"]
                totalScore += resultPathFinder["score"]

                # Dijkstra!
                # # generate dijkstra path
                # (cameFrom, score) = dijkstraSearch(smartGrid.gridPoints, battery, smartGrid.houses[houseID].gridID, battery.gridID)
                # totalScore += score[battery.gridID]
                #
                # # reconstruct the path
                # path = reconstructPath(cameFrom, smartGrid.houses[houseID].gridID, battery.gridID)
                #
                # # update the costs for the gridpoints
                # for point in path:
                #     smartGrid.gridPoints[point].cable[battery.ID] = 0

        if totalScore < bestScore:
            bestScore = totalScore
            #print(savedData[runs]["runs"], savedData[runs]["score"])
            # Make backup of current grid

            backUpHouses = copy.deepcopy(smartGrid.houses)
            backUpBatteries = copy.deepcopy(smartGrid.batteries)
            backUpGridpoints = copy.deepcopy(smartGrid.gridPoints)

            sameRuns = 0
        else:
            smartGrid.houses = backUpHouses
            smartGrid.batteries = backUpBatteries
            smartGrid.gridPoints = backUpGridpoints

            backUpHouses = copy.deepcopy(smartGrid.houses)
            backUpBatteries = copy.deepcopy(smartGrid.batteries)
            backUpGridpoints = copy.deepcopy(smartGrid.gridPoints)

            sameRuns += 1
            if sameRuns == 100:
                print("Break Hill Climber")
                print("__________________")
                break





        savedData.append({"runs": runs, "score": bestScore, "battery0": smartGrid.batteries[0].connectedHouses, "battery1": smartGrid.batteries[1].connectedHouses, "battery2": smartGrid.batteries[2].connectedHouses, "battery3": smartGrid.batteries[3].connectedHouses, "battery4": smartGrid.batteries[4].connectedHouses})

        if runs < numberOfLoops:
            swapHouses()

        print("runs: {}, totalScore: {}, bestScore: {}".format(runs, totalScore, bestScore))
        runs += 1

    for point in smartGrid.gridPoints:
        point.cable = [9, 9, 9, 9, 9]

    return savedData


def swapHouses():
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
