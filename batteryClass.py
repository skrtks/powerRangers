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

    def assignGridIDs(batteries, gridPoints):
        # Itterate over gridpoints and append gridpoint that match x and y locations of current battery to a list.
        for battery in batteries:
            for point in gridPoints:
                if point.xLocation == battery.xLocation and point.yLocation == battery.yLocation:
                    battery.gridID = point.ID
