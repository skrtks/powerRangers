from houseClass import house as houseClass
from batteryClass import battery as batteryClass

def connecter():
    """"Connect houses with nearest batteries """

    # unconnected = len(houses)
    #
    # while unconnected > 0:
    #     for battery in batteries:
    #         sortedHouses = sorted(houses, key=lambda house: house.manhattanDistance[battery.ID])
    #         for house in sortedHouses:
    #             if battery.capacity > house.power and not house.connected:
    #                 battery.capacity -= house.power
    #                 battery.connectedHouses.append(house.ID)
    #                 house.connected = True
    #                 unconnected -= 1
    #                 print("connected")
    #                 break
    #         print("next bat")

    # Connect batteries sorted on power output house
    sortedPower = sorted(houseClass.houses, key=lambda house: house.power, reverse=True)
    for house in sortedPower:
        while not house.connected:
            for battery in batteryClass.batteries:
                if house.manhattanDistance[battery.ID] == min(house.manhattanDistance):
                    if battery.capacity >= house.power:
                        battery.capacity -= house.power
                        battery.connectedHouses.append(house.ID)
                        house.connected = True
                        break
                    else:
                        house.manhattanDistance[battery.ID] = 999

    # connect all houses to batteries (not efficient!)
    # for battery in batteries:
    #     for house in sortedPower:
    #         if battery.capacity >= house.power and not house.connected:
    #             battery.capacity -= house.power
    #             battery.connectedHouses.append(house.ID)
    #             house.connected = True

    # # Loop trough batteries and sort houses on shortest manhattenDistance for every battery
    # for battery in batteries:
    #     sortedHouses = sorted(houses, key=lambda house: house.manhattanDistance[battery.ID])
    #
    #     # Loop trough sorted houses and connect house with battery if enough capacity
    #     for house in sortedHouses:
    #         if battery.capacity > house.power and not house.connected:
    #             battery.capacity -= house.power
    #             battery.connectedHouses.append(house.ID)
    #             house.connected = True

    # Print statements for checking.
    for battery in batteryClass.batteries:
        print("battery capacity[{}]: {}".format(battery.ID, battery.capacity))

    for house in houseClass.houses:
        if not house.connected:
            print("unconnected house(s): {}".format(house.ID))
            print("power supply unconnected house(s): {}".format(house.power))
