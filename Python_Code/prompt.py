from smartGrid import smartGrid
from randomFunction import randomFunction
import connecter
import hillClimber
import sys
from CSVWriter import writeCSV

distr1 = {"house": "../Huizen&Batterijen/wijk1_huizen.csv", "battery": "../Huizen&Batterijen/wijk1_batterijen.csv"}
distr2 = {"house": "../Huizen&Batterijen/wijk2_huizen.csv", "battery": "../Huizen&Batterijen/wijk2_batterijen.csv"}
distr3 = {"house": "../Huizen&Batterijen/wijk3_huizen.csv", "battery": "../Huizen&Batterijen/wijk3_batterijen.csv"}

print("district one     = 1")
print("district two     = 2")
print("district three   = 3")

while True:
    district = input('For which district would you like to find an solution: ')

    if district == '1':
        distrFile = distr1
        break

    elif district == '2':
        distrFile = distr2
        break

    elif district == '3':
        distrFile = distr3
        break

    else:
        print("Please type: 1, 2 or 3")

smartGrid.fileReader(distrFile["house"], distrFile["battery"])

print("random           = 1")
print("greedy           = 2")

while True:
    district = input('How would you like to connect house to battery: ')

    if district == '1':
        randomFunction()
        break

    elif district == '2':
        connecter()
        break

    else:
        print("Please type: 1 or 3")
