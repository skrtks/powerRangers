from gridClass import gridPoint as gridClass
from smartGrid import smartGrid
from houseClass import house as houseClass
from batteryClass import battery as batteryClass

# From https://www.redblobgames.com/pathfinding/a-star/implementation.html

import heapq


class PriorityQueue:
    """
    this is a prio queue stolen
    from https://www.redblobgames.com/pathfinding/a-star/implementation.html
    """
<<<<<<< HEAD
    # Initiate with empty list
=======

>>>>>>> 536319d90bdfe8321ab185ff7a177bc500405823
    def __init__(self):
        self.elements = []

    # Empty the list
    def empty(self):
        return len(self.elements) == 0

    # Add an item to the queue
    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    # Get an item from the queue
    def get(self):
        return heapq.heappop(self.elements)[1]


def dijkstraSearch(battery, smartGrid, startGridPointID, goalGridPointID):
<<<<<<< HEAD

    # Variables
=======
    """
    Find shortes path from house to battery
    """

>>>>>>> 536319d90bdfe8321ab185ff7a177bc500405823
    frontier = PriorityQueue()
    frontier.put(startGridPointID, 0)
    cameFrom = {startGridPointID: None}
    costSoFar = {startGridPointID: 0}

    # Loop until the frontier is empty
    while not frontier.empty():

        # Set current to the first node in the queue
        current = frontier.get()

        # Check if goal has been reached
        if current == goalGridPointID:
            break

        # Get the children of the current node
        childrenList = smartGrid.children(smartGrid.gridPoints[current])

        # Loop through the childrenList and set cost for stepping to child
        for child in childrenList:
            newCost = (costSoFar[current]
                       + smartGrid.gridPoints[current].cable[battery.ID])

            # Make sure child is not visited twice inless with lower cost
            if child not in costSoFar or newCost < costSoFar[child]:
                # Set cost to reach child
                costSoFar[child] = newCost

                # Set priority score for child
                priority = (newCost
                            + smartGrid.gridPoints[child]
                            .manhattanDistance[battery.ID])

                # Add child to the frontier
                frontier.put(child, priority)

                # Remember what last step was
                cameFrom[child] = current

    return (cameFrom, costSoFar)


def reconstructPath(cameFrom, start, goal):
<<<<<<< HEAD
    # Start at end
=======
    """
    battery - house
    """
>>>>>>> 536319d90bdfe8321ab185ff7a177bc500405823
    current = goal
    path = []

    # Loop until start is reached
    while current != start:
        # Trace back the path from goal to start
        path.append(current)
        current = cameFrom[current]
    path.append(start)
    path.reverse()
    return path
