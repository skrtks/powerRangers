# powerRangers

For 'programmeertheorie I' we have to find an efficient solution for connecting houses to batteries in a smartgrid for 3 districts. Houses produce solar energy which have to be stored in a battery if a household doesn't use the energy itself. To keep the cotst low the battery has to be filled as suffiecient as possible without overflowing the barttery. The cables between a house and a battery have to be as short as possible and houses should share cables if these lead to the same battery. 

A district has a size of 50 x 50 and contains 150 houses with different energy outputs and 5 batteries with a capacity of 1500kW each. We use different algorithms to find a solution to connect houses to batteries and algorithms to lay cables between houses and batteries.

## folder pyhtonCode

<ul>
    <li>main.py</li>
         <ul>
            <li>housesList: List containing house objects</li>
            <li>batteries: List containing battery objects</li>
            <li>gridPoints: List containing gridPoint objects</li>
            <li>gridFiller(self): Create grid</li>
            <li>assignGridIDs(self): Assign gridIDs to batteries and houses</li>
            <li>gridDrawer(self): Draw grid with batteries, houses and connections</li>
            <li>fileReader(self, fileHouses, fileBatteries): Read information of houses and batteries from files</li>
            <li>  manhattanDistance(self): Calculate manhattan distance for every gridpoint to batteries</li>
            <li> children(self, gridPoint): Returns gridpoint ID's for possible moves from current gridpoint</li>
        </ul>
    <li>gridClass.py</li>
        <ul>
            <li>Class for gridpoints</li>
        </ul>
    <li>houseClass.py</li>
        <ul>
            <li>Define a class for houses, takes ID, x and coordinates, power output, boolean connected, score, batteryID and manhattandistances to batteries</li>
        </ul>
    <li>batteryClass.py</li>
        <ul>
            <li>Define a class for batteries, takes ID, x and y coordinates, capacity and list of connected houses</li>
        </ul>
    <li>connecter.py</li>
        <ul>
            <li>connectWithBatteries(smartGrid): Connect all houses by sorting them on power output (biggest to smallest) with nearest batteries </li>
            <li>connectWithHouses1(smartGrid): Connect batteries with nearest houses</li>
            <li>connectWithHouses2(smartGrid): Connect batteries with nearest houses, battery picks one house at a time</li>
            <li>greedyAlgorithm(smartGrid): Connect all houses by sorting them on power output (biggest to smallest)</li>
            <li>randomConnecter(smartGrid): Makes random connection for batteries and houses</li>
        </ul>
    <li>dijkstra.py</li>
        <ul>
            <li>Swap houses once to find better solution to append houses to battery</li>
        </ul>
    <li>pathfinder.py</li>
        <ul>
            <li>Greedy algorithm to find short path between house and battery</li>
        </ul>
    <li>CSVWriter.py</li>
        <ul>
            <li>Make new CSV file containing results</li>
        </ul>
    <li>simulatedAnnealing.py</li>
        <ul>
            <li>Swap houses several times to find better solution to append houses to battery</li>
        </ul>
    </li>
</ul>

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
