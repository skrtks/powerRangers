from smartGrid import smartGrid
import connecters
from hillClimber import hillClimber
from simulatedAnnealing import simulatedAnnealing
from CSVWriter import writeCSV

def main():

    A = smartGrid()

    A.fileReader("../Huizen&Batterijen/wijk2_huizen.csv", "../Huizen&Batterijen/wijk2_batterijen.csv")
    A.gridFiller()
    A.manhattanDistance()

    A = connecters.randomConnecter(A)
    print(A.batteries)
    scoreData, A = hillClimber(A)

    # A = connecters.randomConnecter(A)

    # for i in range(1):
    #     filename = "results" + str(i) + ".csv"
    #     A = connecters.randomConnecter(A)
    #     # connecters.randomWithPreverence(A)
    #     scoreData, A = hillClimber(A)
    #     writeCSV(scoreData, filename)

    # for i in range(100000):
    #     filename = "resultsOfSimAn15DEC" + str(i) + ".csv"
    #     # A = connecters.randomConnecter(A)
    #     randomFunction(A)
    #     scoreData, A = simulatedAnnealing(A)
    #     writeCSV(scoreData, filename)

    print("connected")
    print("drawing...")

    A.gridDrawer()

if __name__ == "__main__":
    main()
