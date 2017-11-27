import csv
import numpy as np
import itertools
import random
from houseClass import house
from batteryClass import battery
from gridClass import *
from matplotlib import pyplot as plt

def optimalization_algorithm(houses, batteries):
    houseOrderX = []
    houseOrderY = []
    bestScore = 10000
    for x in range(2):
        #print(x)
        connecterScore = 0
        shuffledHousesX = []
        shuffledHousesY = []
        random.shuffle(houses)

        # Set values back to begin values
        for house in houses:
            house.connected = False

        for battery in batteries:
            battery.capacity = 1507
            battery.connectedHouses = []

        for house in houses:
            counter = 0
            shuffledHousesX.append(house.xLocation)
            shuffledHousesY.append(house.yLocation)
            while not house.connected and counter <= 15:
                for battery in batteries:
                    if house.manhattanDistance[battery.ID] == min(house.manhattanDistance):
                        if battery.capacity >= house.power and not house.connected:
                            battery.capacity -= house.power
                            battery.connectedHouses.append(house.ID)
                            house.connected = True
                            connecterScore += house.manhattanDistance[battery.ID]
                            break
                        else:
                            house.manhattanDistance[battery.ID] = 999
                    counter += 1

        for house in houses:
            if house.connected == False:
                connecterScore = 10000

        if connecterScore < bestScore:
            houseOrderX = shuffledHousesX
            houseOrderY = shuffledHousesY
            bestScore = connecterScore
        print("bestScore : {}".format(bestScore))

    # Print statements for checking.
    for battery in batteries:
        print("battery capacity[{}]: {}".format(battery.ID, battery.capacity))

    for house in houses:
        if not house.connected:
            print("unconnected house(s): {}".format(house.ID))
            print("power supply unconnected house(s): {}".format(house.power))

    print(len(houseOrderX), len(houseOrderY))
# [x_h,y_h,s] = connecter()
# print(s)
#return [houseOrderX, houseOrderY, bestScore]
