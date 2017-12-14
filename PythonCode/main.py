from smartGrid import smartGrid
from randomFunction import randomFunction
import connecters
from hillClimber import hillClimber
import sys
from CSVWriter import writeCSV


def main():

    distr1 = "Huizen&Batterijen/wijk1_huizen.csv", "Huizen&Batterijen/wijk1_batterijen.csv"
    distr2 = "Huizen&Batterijen/wijk2_huizen.csv", "Huizen&Batterijen/wijk2_batterijen.csv"
    distr3 = "Huizen&Batterijen/wijk3_huizen.csv", "Huizen&Batterijen/wijk3_batterijen.csv"

    A = smartGrid()

    A.fileReader("../Huizen&Batterijen/wijk2_huizen.csv", "../Huizen&Batterijen/wijk2_batterijen.csv")

    A.gridFiller()
    A.manhattanDistance()
    connecters.randomConnecter(A)
    A.gridDrawer()

    # print(A.batteries[0].connectedHouses)
    # print(A.batteries[1].connectedHouses)
    # print(A.batteries[2].connectedHouses)
    # print(A.batteries[3].connectedHouses)
    # print(A.batteries[4].connectedHouses)
    #
    # filename = "results" + str(1) + ".csv"
    # scoreData = hillClimber(A)
    # writeCSV(scoreData, filename)
    # print(scoreData)
    #
    # print(A.batteries[0].connectedHouses)
    # print(A.batteries[1].connectedHouses)
    # print(A.batteries[2].connectedHouses)
    # print(A.batteries[3].connectedHouses)
    # print(A.batteries[4].connectedHouses)

    # for i in range(1):
    #     filename = "results" + str(i) + ".csv"
    #     randomFunction(A)
    #     scoreData = hillClimber(A)
    #     writeCSV(scoreData, filename)


if __name__ == "__main__":
    main()
