# powerRangers

For 'programmeertheorie I' we have to find an efficient solution for connecting houses to batteries in a smartgrid for 3 districts. Houses produce solar energy which have to be stored in a battery if a household doesn't use the energy itself. To keep the cotst low the battery has to be filled as suffiecient as possible without overflowing the barttery. The costs need to be as low as possible so we try to keep the cables between a house and a battery as short as possible. Houses share cables when they lead to the same battery, this reduces the costs. Cables have to go around houses, because it would be very expensive to lay a cable underneath a house. 

A district has a size of 50 x 50 and contains 150 houses with different energy outputs and 5 batteries with a capacity of 1500kW each. We use different algorithms to find a solution to connect houses to batteries and algorithms to lay cables between houses and batteries.

## python files

**main.py:**

**smartGrid.py:**
- housesList: List containing house objects
- batteries: List containing battery objects
- gridPoints: List containing gridPoint objects
- gridFiller(self): Create grid
- assignGridIDs(self): Assign gridIDs to batteries and houses
- gridDrawer(self): Draw grid with batteries, houses and connections
- fileReader(self, fileHouses, fileBatteries): Read information of houses and batteries from files
- manhattanDistance(self): Calculate manhattan distance for every gridpoint to batteries
- children(self, gridPoint): Returns gridpoint ID's for possible moves from current gridpoint

**gridClass.py:** Class for grid segments, takes ID, x and y coordinates,cable costs and manhattendistrance to batteries

**houseClass.py:** Define a class for houses, takes ID, x and coordinates, power output, boolean connected, score, batteryID and           manhattandistances to batteries

**batteryClass.py:** Define a class for batteries, takes ID, x and y coordinates, capacity and list of connected houses

**connecters.py:**
- randomConnecter(smartGrid): Finds connection for houses to batteries with preverence for batteries with
                 the smallest manhattan distance.</li>
- randomWithPreference(smartGrid): Connect all houses by sorting them on power output (biggest to smallest) with nearest                   batteries
- greedyAlgorithm(smartGrid): Connect all houses by sorting them on power output (biggest to smallest)

**dijkstra.py:** Dijkstra algorithm to find shortest path between battery and house

**pathfinder.py:** Algorithm to find shortest path between house and battery

**CSVWriter.py:** Make new CSV file containing results

**hillCLimber.py:** Swap houses several times to find better solution to append houses to battery

## Prerequisites
```
  Mathlib 
  Plotlib
  Python3
```

## Changing used district

  When running main.py you will be asked which district to run, which algorithm to use and whether to apply the hillclimber.

  To change the number of loops for running there are three variables defined in main.py at the top of the file that can be changed: 
  
  - numberOfLoops: Choose how many times you want to find new connections and hillclimb (within these loops you can define the number of  swaps and connection trials as explaind next)
  
  - numberOfConnections: Choose how many connections you want to try to optimalize the connections. This option is for the randomWithPreference algorithm. 
    
 - numberOfSwaps: Choose how many times you want to let the hillclimber swap houses
 
 For demonstrating the code these variables are set low. For generating our results we set these values to (numberOfLoops: 50, numberOfConnections: 25, numberOfSwaps: 100000).
 
## Built With
```
  Python3
```

## Authors
```
  Sam Kortekaas            [skrtks](https://github.com/skrtks)
  Daphne Witmer            [10588094](https://github.com/10588094)
  Ida Segond von Banchet   [igcsvb](https://github.com/igcsvb)
```

## Acknowledgments
```
  Dijkstra inspiration from Amit Patel [redblobgames] (https://www.redblobgames.com/pathfinding/a-star/implementation.html)
  Tech assistent: Maarten van der Sande
```
