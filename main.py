from PythonCode.Classes.smartGrid import smartGrid as smartGrid
import PythonCode.Algorithms.connecters as connecters
from PythonCode.Algorithms.hillClimber import hillClimber as hillClimber
from PythonCode.Helpers.CSVWriter import writeCSV as writeCSV
import copy

def main():

    A = smartGrid()
    scoreData = {}
    algorithm = ""
    MaxScore = 100000

    # Choose how many times you want to find new connections and hillclimb
    numberOfLoops = 2

    # Choose how many connections you want to try to optimalize
    numberOfConnections = 10

    # Choose how many times you want to let the hillclimber swap houses
    numberOfSwaps = 3

    # Dict for every district file
    distr1 = {"house": "Huizen&Batterijen/wijk1_huizen.csv", "battery":
              "Huizen&Batterijen/wijk1_batterijen.csv"}
    distr2 = {"house": "Huizen&Batterijen/wijk2_huizen.csv", "battery":
              "Huizen&Batterijen/wijk2_batterijen.csv"}
    distr3 = {"house": "Huizen&Batterijen/wijk3_huizen.csv", "battery":
              "Huizen&Batterijen/wijk3_batterijen.csv"}

    # Select csv file for district that the user wants
    print("district one     = 1")
    print("district two     = 2")
    print("district three   = 3")
    print("For which district would you like to find a solution?")

    while True:
        district = input("District: ")

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

    # Read data from file, safe information in classes and calculate
    # manhattan distance for each gridpoint
    A.fileReader(distrFile["house"], distrFile["battery"])
    A.gridFiller()
    A.manhattanDistance()

    # Make backup of smartGrid to make the original available
    backup = copy.deepcopy(A)

    # Select the algortihm that the user wants to use
    print("randomWithPreference         = 1")
    print("randomConnecter              = 2")
    print("greedyAlgorithm              = 3")
    print("How would you like to connect house to battery?")

    while True:
        algorithm = input("Algorithm: ")

        if algorithm is '1' or algorithm is '2' or algorithm is '3':
            break
        else:
            print("Please type: 1, 2 or 3")

    # Let the user choose a name for the CSV file
    print("How would you like to call your CSV file with results?")

    while True:
        CSVfileName = input("filename: ")
        if CSVfileName is not None:
            break

    # Ask the user whether they want to apply the hillClimber
    while True:
        climbing = input('Would you like to apply the hill climber (y / n)? ')

        bestScore = MaxScore

        if climbing == 'y':

            # Run with randomWithPreference algorithm
            if algorithm is '1':
                for i in range(numberOfLoops):
                    filename = str(CSVfileName) + str(i) + ".csv"

                    A = copy.deepcopy(backup)
                    A, scoreRandom = connecters.randomWithPreference(A, numberOfConnections)

                    scoreData, A = hillClimber(A, numberOfSwaps)

                    if scoreData[numberOfSwaps - 1]["score"] <= bestScore:
                        bestScore = scoreData[numberOfSwaps - 1]["score"]
                        bestConfig = copy.deepcopy(A)

                    writeCSV(scoreData, filename)

                A = copy.deepcopy(bestConfig)
                break

            # Run with randomConnecter
            elif algorithm is '2':
                for i in range(numberOfLoops):
                    filename = str(CSVfileName) + str(i) + ".csv"

                    A = copy.deepcopy(backup)
                    A, scoreRandom = connecters.randomConnecter(A)

                    scoreData, A = hillClimber(A)

                    if scoreData[numberOfSwaps - 1]["score"] <= bestScore:
                        bestScore = scoreData[numberOfSwaps - 1]["score"]
                        bestConfig = copy.deepcopy(A)

                    writeCSV(scoreData, filename)

                A = copy.deepcopy(bestConfig)
                break

            # Run with greedyAlgorithm
            elif algorithm is '3':
                A, scoreData = connecters.greedyAlgorithm(A)
                scoreData, A = hillClimber(A)
                filename = str(CSVfileName) + ".csv"
                writeCSV(scoreData, filename)
                break

        # Run algorithms wihtout hillclimber
        elif climbing == 'n':
            if algorithm == '1':
                A, scoreData = connecters.randomWithPreference(A, numberOfConnections)

            elif algorithm == '2':
                A, scoreData = connecters.randomConnecter(A)

            elif algorithm == '3':
                A, scoreData = connecters.greedyAlgorithm(A)

            filename = str(CSVfileName) + ".csv"
            writeCSV(scoreData, filename)
            break

        # Else ask for valid input
        else:
            print("Please type: y or n")

    # Draw grid
    A.gridDrawer()


if __name__ == "__main__":
    main()
