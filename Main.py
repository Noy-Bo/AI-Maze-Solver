from fibheap import *
import Utilities
from Algorithms.Astar import Astar
from Algorithms.DLS import RecursiveDLS, DLS
from Algorithms.IDAstar import IDAstar
from Algorithms.IDS import IDS
from Algorithms.UCS import UCS
from Algorithms.BiAstar import BiAstar
from DataStructures.HeapDict import HeapDict
from Entities.Node import Node



# ======================== main ========================


#algorithmName,startNode,goalNode,mazeSize,maze = Utilities.readInstance('verySmallMaze.txt')
#algorithmName,startNode,goalNode,mazeSize,maze = Utilities.readInstance('mediumMaze.txt')
algorithmName,startNode,goalNode,mazeSize,maze = Utilities.readInstance('smallMaze.txt')



BiAstar(maze,startNode)
print('@@@@@@@@@@@@@@@@@@@@@@@@')
print('@@@@@@@@@@@@@@@@@@@@@@@@')
print('@@@@@@@@@@@@@@@@@@@@@@@@')
print('@@@@@@@@@@@@@@@@@@@@@@@@')
Astar(maze,startNode)
print('@@@@@@@@@@@@@@@@@@@@@@@@')
print('@@@@@@@@@@@@@@@@@@@@@@@@')
print('@@@@@@@@@@@@@@@@@@@@@@@@')
print('@@@@@@@@@@@@@@@@@@@@@@@@')
UCS(maze,startNode)
print('@@@@@@@@@@@@@@@@@@@@@@@@')
print('@@@@@@@@@@@@@@@@@@@@@@@@')
print('@@@@@@@@@@@@@@@@@@@@@@@@')
print('@@@@@@@@@@@@@@@@@@@@@@@@')
IDAstar(maze,startNode)
print('@@@@@@@@@@@@@@@@@@@@@@@@')
print('@@@@@@@@@@@@@@@@@@@@@@@@')
print('@@@@@@@@@@@@@@@@@@@@@@@@')
print('@@@@@@@@@@@@@@@@@@@@@@@@')
IDS(maze,startNode)
print('@@@@@@@@@@@@@@@@@@@@@@@@')
print('@@@@@@@@@@@@@@@@@@@@@@@@')
print('@@@@@@@@@@@@@@@@@@@@@@@@')
print('@@@@@@@@@@@@@@@@@@@@@@@@')

pass


