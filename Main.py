from fibheap import *

import Utilities
from Algorithms.Astar import Astar
from Algorithms.UCS import UCS
from Algorithms.BiAstar import BiAstar
from DataStructures.PriorityQueue import PriorityQueue
from Entities.Node import Node



# ======================== main ========================


algorithmName,startNode,goalNode,mazeSize,maze = Utilities.readInstance('smallMaze.txt')

UCS(maze,startNode)
print('@@@@@@@@@@@@@@@@@@@@@@@@')
print('@@@@@@@@@@@@@@@@@@@@@@@@')
print('@@@@@@@@@@@@@@@@@@@@@@@@')
print('@@@@@@@@@@@@@@@@@@@@@@@@')
Astar(maze,startNode)
print('@@@@@@@@@@@@@@@@@@@@@@@@')
print('@@@@@@@@@@@@@@@@@@@@@@@@')
print('@@@@@@@@@@@@@@@@@@@@@@@@')
print('@@@@@@@@@@@@@@@@@@@@@@@@')
BiAstar(maze,startNode)

pass


