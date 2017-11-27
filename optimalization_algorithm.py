import csv
import numpy as np
import itertools
import random
from houseClass import house
from batteryClass import battery
from gridClass import *
from matplotlib import pyplot as plt

def optimalization_algorithm(houses, batteries):
    bestScore = 10000
    for x in range(1000):
        #print(x)
        connecterScore = 0
        shuffledHousesX = []
        shuffledHousesY = []
        random.shuffle(houses)
        for house in houses:
            house.connected = False
        for house in houses:
            counter = 0
            while not house.connected and counter <= 15:
                shuffledHousesX.append(house.xLocation)
                shuffledHousesY.append(house.yLocation)
                for battery in batteries:
                    batteryCapacity = battery.capacity
                    if house.manhattanDistance[battery.ID] == min(house.manhattanDistance):
                        if batteryCapacity >= house.power and not house.connected:
                            batteryCapacity -= house.power
                            battery.connectedHouses.append(house.ID)
                            house.connected = True
                            connecterScore += house.manhattanDistance[battery.ID]
                            break
                        else:
                            house.manhattanDistance[battery.ID] = 999

                    counter += 1


# sortedPower = sorted(houses, key=lambda house: house.power, reverse=True)
# for house in sortedPower:
#     while not house.connected:
#         for battery in batteries:
#             if house.manhattanDistance[battery.ID] == min(house.manhattanDistance):
#                 if battery.capacity >= house.power:
#                     battery.capacity -= house.power
#                     battery.connectedHouses.append(house.ID)
#                     house.connected = True
#                     break
#                 else:
#                     house.manhattanDistance[battery.ID] = 999

        for house in houses:
            if house.connected == False:
                connecterScore = 10000

        if connecterScore < bestScore:
            houseOrderX = shuffledHousesX
            houseOrderY = shuffledHousesY
            bestScore = connecterScore
        print(bestScore)

    #return [houseOrderX, houseOrderY, bestScore]
    print(len(houseOrderX), len(houseOrderY))


# [x_h,y_h,s] = connecter()
# print(s)
