from smartGrid import smartGrid
import connecters
from hillClimber import hillClimber
from CSVWriter import writeCSV


def main():

    A = smartGrid()

    A.fileReader("../Huizen&Batterijen/wijk2_huizen.csv", "../Huizen&Batterijen/wijk2_batterijen.csv")
    A.gridFiller()
    A.manhattanDistance()
    connecters.randomWithPreverence(A)
    print("connected")
    print("drawing...")
    A.gridDrawer()


    # A = connecters.randomConnecter(A)
    randomFunction(A)


    # for i in range(1):
    #     filename = "results" + str(i) + ".csv"
    #     # A = connecters.randomConnecter(A)
    #     randomFunction(A)
    #     scoreData, A = hillClimber(A)
    #     writeCSV(scoreData, filename)

    A.gridDrawer()

if __name__ == "__main__":
    main()
