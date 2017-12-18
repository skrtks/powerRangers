from smartGrid import smartGrid
import connecters
import copy
from hillClimber import hillClimber
from simulatedAnnealing import simulatedAnnealing
from CSVWriter import writeCSV

def main():

    A = smartGrid()
    scoreData = {}
    algorithm = ""

    # Dict for every district file
    distr1 = {"house": "../Huizen&Batterijen/wijk1_huizen.csv", "battery":
              "../Huizen&Batterijen/wijk1_batterijen.csv"}
    distr2 = {"house": "../Huizen&Batterijen/wijk2_huizen.csv", "battery":
              "../Huizen&Batterijen/wijk2_batterijen.csv"}
    distr3 = {"house": "../Huizen&Batterijen/wijk3_huizen.csv", "battery":
              "../Huizen&Batterijen/wijk3_batterijen.csv"}

    print("district one     = 1")
    print("district two     = 2")
    print("district three   = 3")

    while True:
        district = input("For which district would you like to find a " +
                         "solution: ")

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

    print("randomWithPreference         = 1")
    print("randomConnecter              = 2")
    print("greedyAlgorithm              = 3")

    # Make backup of smartGrid to make the original available
    backup = copy.deepcopy(A)

    while True:
        algorithm = input('How would you like to connect house to battery: ')

        if algorithm == '1':
            A, scoreData = connecters.randomWithPreference(A)
            break

        elif algorithm == '2':
            A, scoreData = connecters.randomConnecter(A)
            break

        elif algorithm == '3':
            A, scoreData = connecters.greedyAlgorithm(A)
            break

        else:
            print("Please type: 1, 2 or 3")

    print("How would you like to call your CSV file with results?")

    while True:
        CSVfileName = input('filename: ')
        if CSVfileName is not None:
            break

    while True:
        climbing = input('Would you like to apply the hill climber (y / n)? ')

        if climbing == 'y':
            if algorithm is '1':
                for i in range(2):
                    filename = str(CSVfileName) + str(i) + ".csv"

                    if i > 0:
                        A = copy.deepcopy(backup)
                        A, scoreRandom = connecters.randomWithPreference(A)

                    scoreData, A = hillClimber(A)
                    writeCSV(scoreData, filename)

                break

            elif algorithm is '2':
                for i in range(2):
                    filename = str(CSVfileName) + str(i) + ".csv"

                    if i > 0:
                        A = copy.deepcopy(backup)
                        A, scoreRandom = connecters.randomConnecter(A)

                    scoreData, A = hillClimber(A)
                    writeCSV(scoreData, filename)

                break

            elif algorithm is '3':
                scoreData, A = hillClimber(A)
                filename = str(CSVfileName) + ".csv"
                writeCSV(scoreData, filename)
                break

        elif climbing == 'n':
            filename = str(CSVfileName) + ".csv"
            writeCSV(scoreData, filename)
            break

        else:
            print("Please type: y or n")

    A.gridDrawer()


if __name__ == "__main__":
    main()
