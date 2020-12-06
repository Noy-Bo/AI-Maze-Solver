from fibheap import *

import Utilities
from Algorithms.Astar import Astar
from Algorithms.UCS import UCS
from DataStructures.PriorityQueue import PriorityQueue
from Entities.Node import Node



# ======================== main ========================


algorithmName,startNode,goalNode,mazeSize,maze = Utilities.readInstance('smallMaze.txt')


Astar(maze,startNode)
print('@@@@@@@@@@@@@@@@@@@@@@@@')
print('@@@@@@@@@@@@@@@@@@@@@@@@')
print('@@@@@@@@@@@@@@@@@@@@@@@@')
print('@@@@@@@@@@@@@@@@@@@@@@@@')
UCS(maze,startNode)

pass


