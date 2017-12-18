from PythonCode.Algorithms.dijkstra import dijkstraSearch, reconstructPath
import csv
import random
import copy
from PythonCode.Algorithms.pathFinder import pathFinder


def hillClimber(smartGrid, numberOfLoops):
    """
    Find a more effective distribution of houses over batteries, by swapping
    random houses from different batteries and calculating the score.

    Args: smartGrid, numberOfLoops
    Returns: savedData, smartGrid
    """

    print("\nhillClimbing...")

    savedData = []
    sameRuns = 0

    # Calculate total cost for given distribution
    currentScore = calculateScore(smartGrid)
    print("start score: {}".format(currentScore))
    bestScore = currentScore

    # Make a backup to replace if swap score is higher than previous score
    backup = copy.deepcopy(smartGrid)

    for runs in range(numberOfLoops):

        # Swap houses and calculate new score
        swap(smartGrid)
        currentScore = calculateScore(smartGrid)

        # If score is lower change into bestscore and safe data
        if currentScore <= bestScore:
            backup = copy.deepcopy(smartGrid)
            bestScore = currentScore
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

            sameRuns = 0
            print("runs: {}, currentScore: {}, bestScore: {}"
                  .format(runs, currentScore, bestScore))

        # Else place backup back and safe data
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

            sameRuns += 1
            print("runs: {}, currentScore: {}, bestScore: {}"
                  .format(runs, currentScore, bestScore))

        # Stop hillClimber automatically when no better option has been
        # found for 200 runs
        if sameRuns == 200:
            smartGrid = backup
            return savedData, smartGrid

    return savedData, smartGrid


def calculateScore(smartGrid):
    """
    Use a connecter function to calculate the total cost. Use pathfinder for
    a quicker result compared to dijkstra algorithm.

    Args: smartGrid
    Returns: totalScore
    """

    totalScore = 0
    for battery in smartGrid.batteries:
        for houseID in battery.connectedHouses:

            # Pathfinder algorithm
            resultPathFinder = pathFinder(battery, smartGrid, houseID)
            smartGrid.houses[houseID].score = resultPathFinder["score"]
            totalScore += resultPathFinder["score"]

    # Reset costs for gridpoints
    for point in smartGrid.gridPoints:
        point.cost = [9, 9, 9, 9, 9]

        for house in smartGrid.houses:
            if point.ID == house.gridID:
                point.cost = [5000, 5000, 5000, 5000, 5000]

    return totalScore


def swap(smartGrid):
    """
    Swap houses from different batteries if battery has sufficient capacity.
    Picks a random house to swap but has a preference to swap with a house that
    has the highest gridPoint cost.

    Args: smartGrid
    """

    # Sort houses by cost, from high to low
    sortedHouses = sorted(smartGrid.houses, key=lambda house:
                          house.score, reverse=True)

    # Select random house
    randomHouse = random.choice(smartGrid.houses)

    # Calculate space in battery connected to random house
    spaceRHBat = (smartGrid.batteries[randomHouse.batteryID].capacity
                  + randomHouse.power)

    # Loop through houses
    for house in sortedHouses:

        # Check if house is not in same battery and space is sufficient
        if (house.batteryID is not randomHouse.batteryID and
                house.power <= spaceRHBat):
            spaceSHBat = (smartGrid.batteries[house.batteryID].capacity +
                          house.power)
            if randomHouse.power <= spaceSHBat:
                # Swap houses
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
