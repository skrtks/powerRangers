from optimalizationAlgorithm import *
import helpers
from houseClass import house as houseClass
from batteryClass import battery as batteryClass
from gridClass import gridPoint as gridClass
import connecter


def main():
    helpers.fileReader("Huizen&Batterijen/wijk3_huizen.csv",
                        "Huizen&Batterijen/wijk3_batterijen.csv")
    gridClass.gridFiller(gridClass.gridPoints)
    helpers.manhattanDistance(gridClass.gridPoints, batteryClass.batteries)
    # connecter.connecter()
    # gridClass.gridDrawer()
    optimalizationAlgorithm(houseClass.houses, batteryClass.batteries)

if __name__ == "__main__":
    main()
