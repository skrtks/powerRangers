### Algorithms
This folder contains several files with algorithms that try to find the best
solution. The problem is divided in two parts: (1)distribute houses over
batteries and (2)find the shortest path between a house and a battery.

## Connecters
This file contains several functions to distribute houses over batteries.
Only one has to be used, 'randomWithPreference' gives best results.

## Dijkstra and pathFinder
These files find the shortest path between a house and a battery. Only one
has to be used. 'Dijkstra' finds the best solution, but 'pathFinder' is much
quicker and therefor still usefull for the hillclimber.

## HillClimber
Tries to optimize the result found by a connecter function and pathfinder.
