class battery:
    ''' Define a class for batteries, takes ID, x and y coordinates,
        and capacity'''

    def __init__(self, ID, xLocation, yLocation, capacity, gridID=None, connectedHouses=None):

        self.ID = ID
        self.xLocation = xLocation
        self.yLocation = yLocation
        self.capacity = capacity
        self.gridID = gridID
        if connectedHouses == None:
            self.connectedHouses = []

    
