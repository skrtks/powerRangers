
#Je moet alle batterijen & alle huizen meegeven aan aStar voor grid van een bepaalde wijkself.
#aStar moet in een nested loop, loopen door batterijen en daarbinnen in huizen (net zo lang totdat batterij vol is)

# ? op het einde nog een check of alle 150 huizen nu verbonden zijn?


# from: https://gist.github.com/jamiees2/5531924
# pseudocode: http://web.mit.edu/eranki/www/tutorials/search/
def aStar(batteries, houses, grid):

for battery in batteries:
    for house in houses:

    #The open and closed sets
    openset = set()
    closedset = set()
    #Maak een lege lijst voor path
    path = []
    #Current point is the battery
    current = battery
    #Add the starting point to the open set
    openset.add(current)
    #While the open set is not empty
    while openset:
        #Find the item in the open set with the lowest G + H score
        # current is de node/gridpoint met de laagste score op ManDist (dus niet de ManDist zelf)
        current = min(openset.gridPoints.manhattanDistance)



        # add current to path
        path.add(current)

        #If it is the item we want, retrace the path and return it
        if current == house:
            path = []
            return path
        #Remove the item from the open set
        openset.remove(current)
        #Add it to the closed set
        closedset.add(current)

        # zoek ID van current
        # bereken children van nieuwe current
        children(ID.gridpoint)
