from smartGrid import smartGrid
from randomFunction import randomFunction
import connecter
import hillClimber
import sys
from CSVWriter import writeCSV


def main():

    distr1 = "Huizen&Batterijen/wijk1_huizen.csv", "Huizen&Batterijen/wijk1_batterijen.csv"
    distr2 = "Huizen&Batterijen/wijk2_huizen.csv", "Huizen&Batterijen/wijk2_batterijen.csv"
    distr3 = "Huizen&Batterijen/wijk3_huizen.csv", "Huizen&Batterijen/wijk3_batterijen.csv"

    smartGrid.fileReader("../Huizen&Batterijen/wijk1_huizen.csv", "../Huizen&Batterijen/wijk1_batterijen.csv")
    smartGrid.gridFiller()
    smartGrid.manhattanDistance()
    #connecter.connecter()
    randomFunction()
    # scoreData = hillClimber.hillClimber()
    # writeCSV(scoreData)
    smartGrid.gridDrawer()


if __name__ == "__main__":
    main()
