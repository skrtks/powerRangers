class gridPoint:
    """
    Class for grid segments: takes ID, x and y coordinates, cable costs and
    manhattendistrance to batteries.
    """

    def __init__(self, ID, xLocation, yLocation, manhattanDistance=None):

        self.ID = ID
        self.xLocation = xLocation
        self.yLocation = yLocation
        self.cable = [9, 9, 9, 9, 9]
        if manhattanDistance is None:
            self.manhattanDistance = []
