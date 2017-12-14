from gridClass import gridPoint as gridClass
from smartGrid import smartGrid
from houseClass import house as houseClass
from batteryClass import battery as batteryClass

# From https://www.redblobgames.com/pathfinding/a-star/implementation.html

import heapq

class PriorityQueue:
    """
this is a prio queue stolen from https://www.redblobgames.com/pathfinding/a-star/implementation.html

    """
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]


def dijkstraSearch(battery, smartGrid, startGridPointID, goalGridPointID):
    frontier = PriorityQueue()
    frontier.put(startGridPointID, 0)
    cameFrom = {startGridPointID: None}
    costSoFar = {startGridPointID: 0}

    while not frontier.empty():
        current = frontier.get()

        if current == goalGridPointID:
            break

        childrenList = smartGrid.children(smartGrid.gridPoints[current])
        for child in childrenList:
            newCost = costSoFar[current] + smartGrid.gridPoints[current].cable[battery.ID]
            if child not in costSoFar or newCost < costSoFar[child]:
                costSoFar[child] = newCost
                priority = newCost + smartGrid.gridPoints[child].manhattanDistance[battery.ID]
                frontier.put(child, priority)
                cameFrom[child] = current

    return (cameFrom, costSoFar)

def reconstructPath(cameFrom, start, goal):
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = cameFrom[current]
    path.append(start)
    path.reverse()
    return path
