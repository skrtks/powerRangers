class gridPoint:
    """ Class for grid segments. """

    def __init__(self, ID, xLocation, yLocation, manhattanDistance=None):

        self.ID = ID
        self.xLocation = xLocation
        self.yLocation = yLocation
        if manhattanDistance == None:
            self.manhattanDistance = []
