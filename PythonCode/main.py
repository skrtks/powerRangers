from smartGrid import smartGrid
import connecters
from hillClimber import hillClimber
from simulatedAnnealing import simulatedAnnealing
from CSVWriter import writeCSV

def main():

    A = smartGrid()

    A.fileReader("../Huizen&Batterijen/wijk1_huizen.csv", "../Huizen&Batterijen/wijk1_batterijen.csv")
    A.gridFiller()
    A.manhattanDistance()

    # A, scoreData = connecters.randomWithPreference(A)
    # filename = "results" + "RandomWithPreference" + ".csv"
    # writeCSV(scoreData, filename)

    for i in range(1):
        # filename = "results" + str(i) + ".csv"
        # A = connecters.randomConnecter(A)
        A, scoreRandom = connecters.randomWithPreference(A)
        # scoreData, A = hillClimber(A)
        # writeCSV(scoreData, filename)

    A.gridDrawer()

if __name__ == "__main__":
    main()
