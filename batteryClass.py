class battery:
    ''' Define a class for batteries, takes ID, x and y coordinates,
        and capacity'''

    batteries = []

    def __init__(self, ID, xLocation, yLocation, capacity, connectedHouses=None):

        self.ID = ID
        self.xLocation = xLocation
        self.yLocation = yLocation
        self.capacity = capacity
        if connectedHouses == None:
            self.connectedHouses = []
