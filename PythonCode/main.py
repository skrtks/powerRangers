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

    A.fileReader("../Huizen&Batterijen/wijk1_huizen.csv", "../Huizen&Batterijen/wijk1_batterijen.csv")

    A.gridFiller()
    A.manhattanDistance()
    connecters.randomConnecter(A)

    # filename = "results" + str(1) + ".csv"
    # scoreData = hillClimber.hillClimber(A)
    # writeCSV(scoreData, filename)

    # for i in range(1):
    #     filename = "results" + str(i) + ".csv"
    #     randomFunction(A)
    #     scoreData = hillClimber(A)
    #     writeCSV(scoreData, filename)
    # smartGrid.gridDrawer()

    # # Print statements for checking
    # for battery in A.batteries:
    #     print("battery capacity[{}]: {}".format(battery.ID, battery.capacity))
    #
    # for house in A.houses:
    #     if not house.connected:
    #         print("unconnected house(s): {}".format(house.ID))
    #         print("power supply unconnected house(s): {}".format(house.power))


if __name__ == "__main__":
    main()
