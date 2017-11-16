
#Je moet alle batterijen & alle huizen meegeven aan aStar voor grid van een bepaalde wijkself.
#aStar moet in een nested loop, loopen door batterijen en daarbinnen in huizen (net zo lang totdat batterij vol is)

# ? op het einde nog een check of alle 150 huizen nu verbonden zijn?


# from: https://gist.github.com/jamiees2/5531924
# pseudocode: http://web.mit.edu/eranki/www/tutorials/search/
def aStar(batteries, houses, grid):

# Loop through all batteries and houses.
for battery in batteries:
    for house in houses:

    # The open and closed sets.
    openset = set()
    closedset = set()

    # Make an empty list for path.
    path = []

    # Current point is the battery.
    current = battery

    # Add the starting point to the open set.
    openset.add(current)

    # While the open set is not empty.
    while openset:
        # Find the item in the open set with the lowest F score.
        current = min(openset)

        # If the current point is a house which we want to connect, return path.
        if current == house:
            path = []
            return path

        # Remove the item from the open set.
        openset.remove(current)

        # Add it to the closed set.
        closedset.add(current)
        
        # Add children of current to the open set.
        openset.add(children(current, grid))

        # Loop through gridPoints of children.
        for gridPoint in openset:
            # If gridPoint is already in closedset, remove from openset.
            if gridPoint in openset == gridPoint in closedset:
                openset.remove(gridPoint)
            # Else gridPoint is in openset for the first time.
            else:
                # Get xLocation, yLocation and manhattanDistance of gridPoint.
                # Add it to a temporary list.

        # Get lowest F score of gridPoints in openset.

        # Add it to path.
        # Empty temopary list.

        # Return path to draw in grid.
        return path


    #Throw an exception if there is no path
    raise ValueError('No Path Found')
