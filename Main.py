import Utilities
from Algorithms.Astar import Astar
from Algorithms.IDAstar import IDAstar
from Algorithms.IDS import IDS
from Algorithms.UCS import UCS
from Algorithms.BiAstar import BiAstar



# ======================== main ========================

# read max time
print("Please enter maximum run time (seconds)")
maxRunTime = int(input())

# read path to maze
print("Please enter path to problem file")
path = str(input())

# reading file
algorithmName,startNode,goalNode,mazeSize,maze = Utilities.readInstance(path)

# solving
print("Solving with BiAstar, please wait...")
BiAstar(maze,startNode,'movesCount',maxRunTime)
print('')
BiAstar(maze,startNode,'diagonal',maxRunTime)

print('')
print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
print('')
print("Solving with Astar, please wait...")
Astar(maze,startNode,'movesCount',maxRunTime)
print('')
Astar(maze,startNode,'diagonal',maxRunTime)


print('')
print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
print('')
print("Solving with UCS, please wait...")
UCS(maze,startNode,maxRunTime)


print('')
print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
print('')
print("Solving with IDAstar, please wait...")
IDAstar(maze,startNode,'movesCount',maxRunTime)
print('')
IDAstar(maze,startNode,'diagonal',maxRunTime)


print('')
print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
print('')
print("Solving with IDS, please wait...")
IDS(maze,startNode,maxRunTime)

print('')
print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
print('')
print("PRESS ENTER TO EXIT")
input()

pass


