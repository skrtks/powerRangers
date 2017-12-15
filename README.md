# powerRangers

For 'programmeertheorie I' we have to find an efficient solution for connecting houses to batteries in a smartgrid for 3 districts. Houses produce solar energy which have to be stored in a battery if a household doesn't use the energy itself. To keep the cotst low the battery has to be filled as suffiecient as possible without overflowing the barttery. The cables between a house and a battery have to be as short as possible and houses should share cables if these lead to the same battery. 

A district has a size of 50 x 50 and contains 150 houses with different energy outputs and 5 batteries with a capacity of 1500kW each. We use different algorithms to find a solution to connect houses to batteries and algorithms to lay cables between houses and batteries.

## folder pyhtonCode

main.py
smartGrid
    houses 			                                        	List containing house objects
    batteries			                                        List containing battery objects
    gridPoints			                                      List containing gridPoint objects	
    gridFiller(self) 			                                Create grid
    assignGridIDs(self)                                   Assign gridIDs to batteries and houses
    gridDrawer(self)			                                Draw grid with batteries, houses and connections	
    fileReader(self, fileHouses, fileBatteries)			      Read information of houses and batteries from files
    manhattanDistance(self)	  	                          Calculate manhattan distance for every gridpoint to batteries
    children(self, gridPoint)			                        Returns gridpoint ID's for possible moves from current gridpoint

gridClass.py				                                      Class for gridpoints
houseClass.py			                                        Define a class for houses, takes ID, x and coordinates, power output, boolean                                                           connected, score, batteryID and manhattandistances to batteries
batteryClass.py			                                      Define a class for batteries, takes ID, x and y coordinates, capacity and list                                                           of connected houses

connecter.py				 
    connectWithBatteries(smartGrid)                       Connect all houses by sorting them on power output (biggest to smallest) with                                                           nearest batteries
    connectWithHouses1(smartGrid)                         Connect batteries with nearest houses
    connectWithHouses2(smartGrid)                         Connect batteries with nearest houses, battery picks one house at a time
    greedyAlgorithm(smartGrid)                            Connect all houses by sorting them on power output (biggest to smallest)
    randomConnecter(smartGrid)                            Makes random connection for batteries and houses

dijkstra.py				                                        Swap houses once to find better solution to append houses to battery
pathfinder.py                                             Greedy algorithm to find short path between house and battery
CSVWriter.py                                              Make new CSV file containing results
simulatedAnnealing.py                                     Swap houses several times to find better solution to append houses to battery

### Prerequisites

- Mathlib 
- Plotlib
- Python3

## Changing used district

Used district can be changed by setting the filename in main.py

## Built With

* Python3

## Authors

* Sam Kortekaas            [skrtks](https://github.com/skrtks)
* Daphne Witmer            [10588094](https://github.com/10588094)
* Ida Segond von Banchet   [igcsvb](https://github.com/igcsvb)

## Acknowledgments

* Dijkstra inspiration from Amit Patel [redblobgames] (https://www.redblobgames.com/pathfinding/a-star/implementation.html)
* Tech assistent: Maarten
