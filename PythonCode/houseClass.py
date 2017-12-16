class house:
    ''' Define a class for houses, takes ID, x and y coordinates,
        and power output'''

    def __init__(self, ID, xLocation, yLocation, power, gridID=None,
                 connected=False, manhattanDistance=None):

        self.ID = ID
        self.xLocation = xLocation
        self.yLocation = yLocation
        self.power = power
        self.gridID = gridID
        self.connected = connected
        self.score = None
        self.batteryID = None
        if manhattanDistance is None:
            self.manhattanDistance = []
