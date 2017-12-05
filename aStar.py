from gridClass import gridPoint as gridClass
from smartGrid import smartGrid
from houseClass import house as houseClass
from batteryClass import battery as batteryClass

# From https://www.redblobgames.com/pathfinding/a-star/implementation.html

class Queue:
    def __init__(self):
        self.elements = collections.deque()

    def empty(self):
        return len(self.elements) == 0

    def put(self, x):
        self.elements.append(x)

    def get(self):
        return self.elements.popleft()

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


def a_star_search(gridPoints, battery, startGridPointID, goalGridPointID):
    frontier = PriorityQueue()
    frontier.put(startGridPointID, 0)
    came_from = {startGridPointID: None}
    cost_so_far = {startGridPointID: 0}
    # came_from[startGridPointID] = None
    # cost_so_far[startGridPointID] = 0

    while not frontier.empty():
        current = frontier.get()
        # print("current: {}".format(current))
        # print("goal: {}".format(goalGridPointID))
        # print("queue is {}".format(frontier.elements))

        if current == goalGridPointID:
            break

        childrenList = smartGrid.children(gridPoints[current])
        for child in childrenList:
            # print("child: {}".format(child))
            new_cost = cost_so_far[current] + gridPoints[current].cable[battery.ID]
            if child not in cost_so_far or new_cost < cost_so_far[child]:
                cost_so_far[child] = new_cost
                priority = new_cost + gridPoints[child].manhattanDistance[battery.ID]
                frontier.put(child, priority)
                came_from[child] = current

    return (came_from, cost_so_far)

def reconstruct_path(came_from, start, goal):
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start) # optional
    path.reverse() # optional
    return path
