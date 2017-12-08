from dijkstra import dijkstraSearch, reconstructPath
from randomFunction import randomFunction
from smartGrid import smartGrid
import csv
import random

def hillClimber():

    totalScore = 0
    savedData = []
    runs = 0
    bestScore = 100000

    for x in range(5):
        for battery in smartGrid.batteries:
            for houseID in battery.connectedHouses:
                # generate a star path
                (cameFrom, score) = dijkstraSearch(smartGrid.gridPoints, battery, smartGrid.houses[houseID].gridID, battery.gridID)
                totalScore += score[battery.gridID]

                # reconstruct the path
                path = reconstructPath(cameFrom, smartGrid.houses[houseID].gridID, battery.gridID)

                # update the costs for the gridpoints
                for point in path:
                    smartGrid.gridPoints[point].cable[battery.ID] = 0

        if totalScore < bestScore:
            bestScore = totalScore
            savedData.append({"runs": runs, "score": bestScore, "battery0": smartGrid.batteries[0].connectedHouses, "battery1": smartGrid.batteries[1].connectedHouses, "battery2": smartGrid.batteries[2].connectedHouses, "battery3": smartGrid.batteries[3].connectedHouses, "battery4": smartGrid.batteries[4].connectedHouses})
            print(savedData[runs]["runs"], savedData[runs]["score"])
            # Make backup of current grid
            backUpHouses = smartGrid.houses
            backUpBatteries = smartGrid.batteries
            backUpGridpoints = smartGrid.gridPoints
        else:
            smartGrid.houses = backUpHouses
            smartGrid.batteries = backUpBatteries
            smartGrid.gridPoints = backUpGridpoints

        swapHouses()
        print("swapped")
        runs += 1

def swapHouses():
    # Select random house.
    randomHouse = random.choice(smartGrid.houses)

    # Calculate space in battery connected to random house
    spaceRHBat = smartGrid.batteries[randomHouse.batteryId].capacity + randomHouse.power

    # Loop through houses
    for house in smartGrid.houses:

        # Check if house is not in same battery and space is sufficient
        if house.batteryId is not randomHouse.batteryId and house.power <= spaceRHBat:
            spaceSHBat = smartGrid.batteries[house.batteryId].capacity + house.power
            if randomHouse.power <= spaceSHBat:
                smartGrid.batteries[house.batteryId].connectedHouses.remove(house.ID)
                smartGrid.batteries[randomHouse.batteryId].connectedHouses.remove(randomHouse.ID)

                smartGrid.batteries[house.batteryId].connectedHouses.append(randomHouse.ID)
                smartGrid.batteries[randomHouse.batteryId].connectedHouses.append(house.ID)

                (house.batteryId, randomHouse.batteryId) = (randomHouse.batteryId, house.batteryId)

    for point in smartGrid.gridPoints.cable:
        point.cable = [9, 9, 9, 9, 9]
