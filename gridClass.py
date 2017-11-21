class gridPoint:
    """ Class for grid segments. """

    def __init__(self, ID, xLocation, yLocation, manhattanDistance=None, cable=None):

        self.ID = ID
        self.xLocation = xLocation
        self.yLocation = yLocation
        self.cable = [9, 9, 9, 9, 9]
        if manhattanDistance == None:
            self.manhattanDistance = []
        if cable == None:
            self.cable = []
