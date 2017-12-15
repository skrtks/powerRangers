from smartGrid import smartGrid
from randomFunction import randomFunction
import connecters
from hillClimber import hillClimber
from simulatedAnnealing import simulatedAnnealing
from CSVWriter import writeCSV

def main():

    A = smartGrid()

    A.fileReader("../Huizen&Batterijen/wijk2_huizen.csv", "../Huizen&Batterijen/wijk2_batterijen.csv")
    A.gridFiller()
    A.manhattanDistance()


    # A = connecters.randomConnecter(A)
    #randomFunction(A)


    for i in range(100000):
        filename = "resultsOfSimAn15DEC" + str(i) + ".csv"
        # A = connecters.randomConnecter(A)
        randomFunction(A)
        scoreData, A = simulatedAnnealing(A)
        writeCSV(scoreData, filename)

    A.gridDrawer()

if __name__ == "__main__":
    main()
