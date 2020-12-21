import Utilities
from Algorithms.Astar_visualized import Astar
from Algorithms.IDAstar_visualized import IDAstar
from Algorithms.IDS_visualized import IDS
from Algorithms.UCS_visualized import UCS
from Algorithms.BiAstar_visualized import BiAstar


def getAlgorithmFromString(algorithmString):
    if algorithmString.lower() == "biastar":
        return BiAstar, True
    elif algorithmString.lower() == "astar":
       return Astar, True
    elif algorithmString.lower() == "idastar":
        return IDAstar, True
    elif algorithmString.lower() == "ids":
        return IDS, False
    elif algorithmString.lower() == "ucs":
        return UCS, False
    else:
        return "ERROR"


def runOnAll(maze, maxRunTime):
    # solving
    print("Solving with BiAstar, please wait...")
    BiAstar(maze, maxRunTime, 'movesCount')
    print('')
    BiAstar(maze, maxRunTime, 'diagonal')

    print('')
    print(
        '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    print('')
    print("Solving with Astar, please wait...")
    Astar(maze, maxRunTime, 'movesCount')
    print('')
    Astar(maze, maxRunTime, 'diagonal')

    print('')
    print(
        '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    print('')
    print("Solving with UCS, please wait...")
    UCS(maze, maxRunTime)

    print('')
    print(
        '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    print('')
    print("Solving with IDAstar, please wait...")
    IDAstar(maze, maxRunTime, 'movesCount')
    print('')
    IDAstar(maze, maxRunTime, 'diagonal')

    print('')
    print(
        '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    print('')
    print("Solving with IDS, please wait...")
    IDS(maze, maxRunTime)

    print('')
    print(
        '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    print('')
    print("PRESS ENTER TO EXIT")
    input()


# ======================== main ========================

# read max time
print("Please enter maximum run time (seconds)")
maxRunTime = int(input())

# read path to problem
print("Please enter path to problem file")
path = str(input())
# reading problem
algorithmName, startNode, goalNode, mazeSize, maze = Utilities.readInstance(path)

# run on all
runOnAll(maze,maxRunTime)

# # run as requeusted
# algorithm, isHeuristic = getAlgorithmFromString(algorithmName)
# print("solving with "+algorithmName+", please wait...")
# if isHeuristic is True:
#     algorithm(maze, maxRunTime, "diagonal")
# else:
#     algorithm(maze, maxRunTime)

print('')
print("PRESS ENTER TO EXIT")
input()