from smartGrid import smartGrid
from optimalizationAlgorithm import optimalizationAlgorithm
import connecter


def main():
    smartGrid.fileReader("Huizen&Batterijen/wijk1_huizen.csv",
                        "Huizen&Batterijen/wijk1_batterijen.csv")
    smartGrid.gridFiller()
    smartGrid.manhattanDistance()
    #connecter.connecter()
    optimalizationAlgorithm()
    smartGrid.gridDrawer()


if __name__ == "__main__":
    main()
