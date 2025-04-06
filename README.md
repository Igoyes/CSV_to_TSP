# CSV_to_TSP
csv to tsp converter for travelling salesman problem solvers


WIP

This python script is used to translate csv files in a specific format into TSP files readable by TSPlib compatible software like Concorde TSP solver

The script takes in input a csv file formatted like in the example (node 1,node 2,distance), the first line is ignored as an header, and outputs a TSP file in the TSP95 format (http://comopt.ifi.uni-heidelberg.de/software/TSPLIB95/tsp95.pdf)

In the prototype folder the first and narrower version of the script can be inspected, this was used to find an optimal route for santa claus to travel to 169 countries for this Instagram post (https://www.instagram.com/p/DD95MgSNdO5/?img_index=12)
