from optimalizationAlgorithm import *
import helpers
from houseClass import house as houseClass
from batteryClass import battery as batteryClass
from gridClass import gridPoint as gridClass
import connecter
import Astar_sam


def main():
    helpers.fileReader("Huizen&Batterijen/wijk1_huizen.csv",
                "Huizen&Batterijen/wijk1_batterijen.csv")
    gridClass.gridFiller(gridClass.gridPoints)
    helpers.manhattanDistance(gridClass.gridPoints, batteryClass.batteries)
    connecter.connecter()

    # Itterate over gridpoints and append gridpoint that match x and y locations of current house to a list.
    for house in houseClass.houses:
        for point in gridClass.gridPoints:
            if point.xLocation == house.xLocation and point.yLocation == house.yLocation:
                house.gridID = point.ID

    for battery in batteryClass.batteries:
        for point in gridClass.gridPoints:
            if point.xLocation == battery.xLocation and point.yLocation == battery.yLocation:
                battery.gridID = point.ID

    # for i in range(3):
    #     startGridPointID = houseClass.houses[i].gridID
    #     goalGridPointID = batteryClass.batteries[0].gridID
    #     came_from = Astar_sam.a_star_search(gridClass.gridPoints, batteryClass.batteries[0], startGridPointID, goalGridPointID)

    #path = Astar_sam.reconstruct_path(came_from, startGridPointID, goalGridPointID)
    gridClass.gridDrawer(gridClass.gridPoints)
    # optimalizationAlgorithm(houseClass.houses, batteryClass.batteries)

if __name__ == "__main__":
    main()
