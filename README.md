# AI-Maze-Solver

In this project we developed an independent agent that can solve a given maze using various search algorithms - both informed and uninformed while using heuristics functions we designed.

The goal of the agent is to solve the maze with the cheapest path possible. The maze is represented by NxN matrix of costs, starting point coordinates and goal point coordinates. The agent can move to all 8 adjacency direction.

We offer 5 different search algorithms: Bi-Astar, AStar, ID-Astar, UCS, IDS to that the agent can use to solve the maze with while using 2 kinds of admissible heuristics we developed.

We provide a GUI interface to run our program, in which you can load mazes, set a time limit, and visualize the solving algorithm and the result path.

The results output is via txt file, which is generated after a run is completed in the same directory as ‘output_results.txt’ in which you will find statistics of the run.
