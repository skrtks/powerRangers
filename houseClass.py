class house:
    ''' Define a class for houses, takes ID, x and y coordinates,
        and power output'''

    def __init__(self, ID, xLocation, yLocation, power, connected):

        self.ID = ID
        self.xLocation = xLocation
        self.yLocation = yLocation
        self.power = power
        self.connected = connected
