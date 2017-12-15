from smartGrid import smartGrid
import connecters
from hillClimber import hillClimber
from simulatedAnnealing import simulatedAnnealing
from CSVWriter import writeCSV

def main():

    A = smartGrid()

    # Dict for every district file
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

    A.fileReader(distrFile["house"], distrFile["battery"])
    A.gridFiller()
    A.manhattanDistance()

    print("connectWithBatteries         = 1")
    print("connectWithHouses1           = 2")
    print("connectWithHouses2           = 3")
    print("greedyAlgorithm              = 4")
    print("randomConnecter              = 5")
    print("randomWithPreference         = 6")

    while True:
        district = input('How would you like to connect house to battery: ')

        if district == '1':
            A, scoreData = connecters.connectWithBatteries(A)
            break

        elif district == '2':
            A, scoreData = connecters.connectWithHouse1(A)
            break

        elif district == '3':
            A, scoreData = connecters.connectWithHouse2(A)
            break

        elif district == '4':
            A, scoreData = connecters.greedyAlgorithm(A)
            break

        elif district == '5':
            A, scoreData = connecters.randomConnecter(A)
            break

        elif district == '6':
            A, scoreData = connecters.randomWithPreference(A)
            break

        else:
            print("Please type: 1, 2, 3, 4, 5 or 6")

    print("How would you like to call your CSV file with results?")

    while True:
        CSVfile = input('filename:')
        if str(CSVfile) != None:
            filename = "results" + str(CSVfile) + ".csv"
            writeCSV(scoreData, filename)
            break

    A.gridDrawer()

# if __name__ == "__main__":
#     main()
