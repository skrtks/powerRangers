# from smartGrid import smartGrid
import random

def connecter(smartGrid):
    """"Connect houses with nearest batteries """

    # Connect batteries sorted on power output house
    # sortedPower = sorted(smartGrid.houses, key=lambda house: house.power, reverse=True)
    # for house in sortedPower:
    #     while not house.connected:
    #         for battery in smartGrid.batteries:
    #             if house.manhattanDistance[battery.ID] == min(house.manhattanDistance):
    #                 if battery.capacity >= house.power:
    #                     battery.capacity -= house.power
    #                     battery.connectedHouses.append(house.ID)
    #                     house.connected = True
    #                     break
    #                 else:
    #                     house.manhattanDistance[battery.ID] = 999

    # -> zelfde als bovenstaande, maar met batterij lijst op voglorde (zo veranderen we geen data maar kunnen we geen batterij ID onthouden) <- #
    sortedPower = sorted(smartGrid.houses, key=lambda house: house.power, reverse=True)
    for house in sortedPower:
        sortedBatteries = sorted(smartGrid.batteries, key=lambda battery: house.manhattanDistance[battery.ID])
        for battery in sortedBatteries:
            print(house.manhattanDistance[battery.ID])
        for battery in sortedBatteries:
            if battery.capacity >= house.power:
                battery.capacity -= house.power
                battery.connectedHouses.append(house.ID)
                house.batteryId = battery.ID
                house.connected = True
                break

    #  -> Houses sorted on manhattenDistance <- #
    # unconnected = len(smartGrid.houses)
    #
    # while unconnected > 0:
    #     for battery in smartGrid.batteries:
    #         sortedHouses = sorted(smartGrid.houses, key=lambda house: house.manhattanDistance[battery.ID])
    #         for house in sortedHouses:
    #             if battery.capacity > house.power and not house.connected:
    #                 battery.capacity -= house.power
    #                 battery.connectedHouses.append(house.ID)
    #                 house.connected = True
    #                 house.batteryId = battery.ID
    #                 unconnected -= 1
    #                 print("connected")
    #                 break
    #         print("next bat")

    # -> houses sorted on power <- #
    # connect all houses to batteries (not efficient!)
    # for battery in batteries:
    #     for house in sortedPower:
    #         if battery.capacity >= house.power and not house.connected:
    #             battery.capacity -= house.power
    #             battery.connectedHouses.append(house.ID)
    #             house.connected = True

    # -> houses sorted on shortest manhattenDistance for every battery <- #
    # for battery in smartGrid.batteries:
    #     sortedHouses = sorted(smartGrid.houses, key=lambda house: house.manhattanDistance[battery.ID])
    #
    #     # Loop trough sorted houses and connect house with battery if enough capacity
    #     for house in sortedHouses:
    #         if battery.capacity > house.power and not house.connected:
    #             battery.capacity -= house.power
    #             battery.connectedHouses.append(house.ID)
    #             house.batteryId = battery.ID
    #             house.connected = True

    # Print statements for checking
    for battery in smartGrid.batteries:
        print("battery capacity[{}]: {}".format(battery.ID, battery.capacity))

    for house in smartGrid.houses:
        if not house.connected:
            print("unconnected house(s): {}".format(house.ID))
            print("power supply unconnected house(s): {}".format(house.power))

def randomConnecter(smartGrid):
    """Makes random connection for batteries and houses"""

    numberOfHouses = 150
    unconnected = numberOfHouses

    # Loop untill all houses are connected
    while unconnected > 0:

        # Copy houses and batteries to remember unshuffled order and set changes back in new loop
        shuffledHouses = copy.deepcopy(smartGrid.houses)
        shuffledBatteries = copy.deepcopy(smartGrid.batteries)

        random.shuffle(shuffledHouses)
        random.shuffle(shuffledBatteries)

        # Loop trought random shuffled houses and batteries and connect
        for battery in shuffledBatteries:
            for house in shuffledHouses:
                if battery.capacity >= house.power:
                    battery.capacity -= house.power
                    battery.connectedHouses.append(house.ID)
                    house.connected = True
                    house.batteryId = battery.ID
                    connecterScore += house.manhattanDistance[battery.ID]
                    unconnected -= 1
                    break

    return True
