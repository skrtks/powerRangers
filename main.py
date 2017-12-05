from smartGrid import smartGrid
from optimalizationAlgorithm import optimalizationAlgorithm
import connecter


def main():
    smartGrid.fileReader("Huizen&Batterijen/wijk2_huizen.csv",
                        "Huizen&Batterijen/wijk2_batterijen.csv")
    smartGrid.gridFiller()
    smartGrid.manhattanDistance()
    connecter.connecter()

    smartGrid.gridDrawer()
    # optimalizationAlgorithm(houseClass.houses, batteryClass.batteries)

if __name__ == "__main__":
    main()
