class battery:
    """
    Class for batteries: takes ID, x and y coordinates, power capactity, gridID
    of battery location, houseID of connected house.  
    """

    def __init__(self, ID, xLocation, yLocation, capacity, gridID=None,
                 connectedHouses=None):

        self.ID = ID
        self.xLocation = xLocation
        self.yLocation = yLocation
        self.capacity = capacity
        self.gridID = gridID
        if connectedHouses is None:
            self.connectedHouses = []
