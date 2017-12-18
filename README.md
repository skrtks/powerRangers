# powerRangers

For 'programmeertheorie I' we have to find an efficient solution for connecting houses to batteries in a smartgrid for 3 districts. Houses produce solar energy which have to be stored in a battery if a household doesn't use the energy itself. To keep the cotst low the battery has to be filled as suffiecient as possible without overflowing the barttery. The costs need to be as low as possible so we try to keep the cables between a house and a battery as short as possible. Houses share cables when they lead to the same battery, this reduces the costs. Cables have to go around houses, because it would be very expensive to lay a cable underneath a house. 

A district has a size of 50 x 50 and contains 150 houses with different energy outputs and 5 batteries with a capacity of 1500kW each. We use different algorithms to find a solution to connect houses to batteries and algorithms to lay cables between houses and batteries.

## folder pyhtonCode

smartGrid.py
    - housesList:
    - batteries:

<ul>
    <li>main.py</li
        <ul>
        </ul>
    <li>smartGrid.py</li>
         <ul>
            <li>housesList: List containing house objects</li>
            <li>batteries: List containing battery objects</li>
            <li>gridPoints: List containing gridPoint objects</li>
            <li>gridFiller(self): Create grid</li>
            <li>assignGridIDs(self): Assign gridIDs to batteries and houses</li>
            <li>gridDrawer(self): Draw grid with batteries, houses and connections</li>
            <li>fileReader(self, fileHouses, fileBatteries): Read information of houses and batteries from files</li>
            <li>manhattanDistance(self): Calculate manhattan distance for every gridpoint to batteries</li>
            <li>children(self, gridPoint): Returns gridpoint ID's for possible moves from current gridpoint</li>
        </ul>
    <li>gridClass.py</li>
        <ul>
            <li>Class for grid segments, takes ID, x and y coordinates,cable costs and
    manhattendistrance to batteries</li>
        </ul>
    <li>houseClass.py</li>
        <ul>
            <li>Define a class for houses, takes ID, x and coordinates, power output, boolean connected, score, batteryID and           manhattandistances to batteries</li>
        </ul>
    <li>batteryClass.py</li>
        <ul>
            <li>Define a class for batteries, takes ID, x and y coordinates, capacity and list of connected houses</li>
        </ul>
    <li>connecters.py</li>
        <ul>
             <li>randomConnecter(smartGrid): Finds connection for houses to batteries with preverence for batteries with
                 the smallest manhattan distance.</li>
            <li>randomWithPreference(smartGrid): Connect all houses by sorting them on power output (biggest to smallest) with nearest                   batteries </li>
            <li>greedyAlgorithm(smartGrid): Connect all houses by sorting them on power output (biggest to smallest)</li>
        </ul>
    <li>dijkstra.py</li>
        <ul>
            <li>Dijkstra algorithm to find shortest path between battery and house</li>
        </ul>
    <li>pathfinder.py</li>
        <ul>
            <li>Algorithm to find shortest path between house and battery</li>
        </ul>
    <li>CSVWriter.py</li>
        <ul>
            <li>Make new CSV file containing results</li>
        </ul>
    <li>hillCLimber.py</li>
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

When running main.py you will be asked which district to run and which arlorithm to use. 

To change the number of loops for the connecter and/or the hillClimber change 'numberOfLoops' 
in conneter.py and/or hillClimber.py

## Built With

* Python3

## Authors

* Sam Kortekaas            [skrtks](https://github.com/skrtks)
* Daphne Witmer            [10588094](https://github.com/10588094)
* Ida Segond von Banchet   [igcsvb](https://github.com/igcsvb)

## Acknowledgments

* Dijkstra inspiration from Amit Patel [redblobgames] (https://www.redblobgames.com/pathfinding/a-star/implementation.html)
* Tech assistent: Maarten van der Sande
