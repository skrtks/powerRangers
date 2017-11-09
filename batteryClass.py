class battery:
    ''' Define a class for batteries, takes ID, x and y coordinates,
        and capacity'''

    def __init__(self, ID, xLocation, yLocation, capacity, connectedHouse):

        self.ID = ID
        self.xLocation = xLocation
        self.yLocation = yLocation
        self.capacity = capacity
        self.connectedHouse = connectedHouse
