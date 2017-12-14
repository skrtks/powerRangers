import random
import copy

def connectWithBatteries(smartGrid):
    """"Connect houses with nearest batteries """

    sortedPower = sorted(smartGrid.houses, key=lambda house: house.power, reverse=True)

    # Loop trough houses sorted on power (biggest to smallest power)
    for house in sortedPower:
        sortedBatteries = sorted(smartGrid.batteries, key=lambda battery: house.manhattanDistance[battery.ID])

        # Loop trough batteries sorted on manhattanDistance (smallest to biggest manhattanDistance)
        for battery in sortedBatteries:
            if battery.capacity >= house.power:
                battery.capacity -= house.power
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
                battery.capacity -= house.power
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
                    battery.capacity -= house.power
                    battery.connectedHouses.append(house.ID)
                    house.connected = True
                    house.batteryId = battery.ID
                    unconnected -= 1
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
                battery.capacity -= house.power
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
                    smartGrid.batteries[battery.ID].capacity -= house.power
                    smartGrid.batteries[battery.ID].connectedHouses.append(house.ID)
                    smartGrid.houses[house.ID].connected = True
                    smartGrid.houses[house.ID].batteryId = battery.ID
                    unconnected -= 1
                    break



        # Print statements for checkingss
        for battery in smartGrid.batteries:
            print("battery capacity[{}]: {}".format(battery.ID, battery.capacity))
    for house in smartGrid.houses:
        if not house.connected:
            print("unconnected house(s): {}".format(house.ID))
            print("power supply unconnected house(s): {}".format(house.power))

    print(smartGrid.batteries[0].connectedHouses)
    return smartGrid
