from smartGrid import smartGrid
import connecters
from hillClimber import hillClimber
from simulatedAnnealing import simulatedAnnealing
from CSVWriter import writeCSV

def main():

    A = smartGrid()

    A.fileReader("../Huizen&Batterijen/wijk3_huizen.csv", "../Huizen&Batterijen/wijk3_batterijen.csv")
    A.gridFiller()
    A.manhattanDistance()

    A, scoreData = connecters.randomWithPreference(A)
    filename = "results" + "RandomWithPreference" + ".csv"
    writeCSV(scoreData, filename)


    # for i in range(1):
    #     filename = "results" + str(i) + ".csv"
    #     # A = connecters.randomConnecter(A)
    #     A, scoreRandom = connecters.randomWithPreference(A)
    #     scoreData, A = hillClimber(A)
    #     writeCSV(scoreData, filename)

    print("connected")
    print("drawing...")

    # Print statements for checking.
    for battery in A.batteries:
        print("battery capacity[{}]: {}".format(battery.ID, battery.capacity))

    for house in A.houses:
        if not house.connected:
            print("unconnected house(s): {}".format(house.ID))
            print("power supply unconnected house(s): {}".format(house.power))

    A.gridDrawer(A)

if __name__ == "__main__":
    main()
