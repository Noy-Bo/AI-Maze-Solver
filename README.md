# AI-Maze-Solver

In this project we developed an independent agent that can solve a given maze using various search algorithms - both informed and uninformed while using heuristics functions we designed.

The goal of the agent is to solve the maze with the cheapest path possible. The maze is represented by NxN matrix of costs, starting point coordinates and goal point coordinates. The agent can move to all 8 adjacency direction.

We offer 5 different search algorithms: Bi-Astar, AStar, ID-Astar, UCS, IDS to that the agent can use to solve the maze with while using 2 kinds of admissible heuristics we designed.

We provide a GUI interface to run our program, in which you can load mazes, set a time limit, and visualize the solving algorithm and the result path.

The results output is via txt file, which is generated after a run is completed in the same directory as ‘output_results.txt’ in which you will find statistics of the run.


<p float="center">
  <img src="https://raw.githubusercontent.com/Noy-Bo/AI-Maze-Solver/main/readme/GUI.png" alt="alt text" width="400" height="450">
</p>

<p float="center">
 <img src="https://github.com/Noy-Bo/AI-Maze-Solver/blob/main/readme/BIASTAR.gif" alt="alt text" width="400" height="450">
</p>

<p float="center">
 <img src="https://github.com/Noy-Bo/AI-Maze-Solver/blob/main/readme/UCS%20VS%20ASTAR.gif" alt="alt text" width="800" height="450">
</p>
