class house:
    ''' Define a class for houses, takes ID, x and y coordinates,
        and power output'''

    def __init__(self, ID, xLocation, yLocation, power, connected=False, manhattanDistance=None):

        self.ID = ID
        self.xLocation = xLocation
        self.yLocation = yLocation
        self.power = power
        self.connected = connected
        if manhattanDistance == None:
            self.manhattanDistance = []
