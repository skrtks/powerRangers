class house:
    ''' Define a class for houses, takes ID, x and y coordinates,
        and power output'''

    def __init__(self, ID, xLocation, yLocation, power, gridID=None, connected=False, manhattanDistance=None):

        self.ID = ID
        self.xLocation = xLocation
        self.yLocation = yLocation
        self.power = power
        self.gridID = gridID
        self.connected = connected
        if manhattanDistance == None:
            self.manhattanDistance = []

    def assignGridIDs(houses, gridPoints):
        """
        description
        args:
            houses:
            gridPoints:
        returns: True if succes
        """
        # Iterate over gridpoints and append gridpoint that match x and y locations of current house to a list.
        for house in houses:
            for point in gridPoints:
                if point.xLocation == house.xLocation and point.yLocation == house.yLocation:
                    house.gridID = point.ID
        return True
