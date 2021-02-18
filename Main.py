import Utilities
from Algorithms.Astar import Astar
from Algorithms.Astar_visualized import AstarVisual
from Algorithms.BiAstar import BiAstar
from Algorithms.IDAstar import IDAstar
from Algorithms.IDAstar_visualized import IDAstarVisual
from Algorithms.BiAstar_visualized import BiAstarVisual
from Algorithms.IDS import IDS
from Algorithms.IDS_visualized import IDSVisual
from Algorithms.UCS import UCS
from Algorithms.UCS_visualized import UCSVisual
from GUI.GUI_interface import GuiInterface


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
    #solving
    print("Solving with BiAstar, please wait...")
    BiAstar(maze, maxRunTime, 'movesCount')
    print('')
    BiAstar(maze, maxRunTime, 'minimumMoves')

    print('')
    print(
        '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    print('')
    print("Solving with Astar, please wait...")
    Astar(maze, maxRunTime, 'movesCount')
    print('')
    Astar(maze, maxRunTime, 'minimumMoves')

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
    IDAstar(maze, maxRunTime, 'minimumMoves')
    print('')
    IDAstar(maze, maxRunTime, 'movesCount')


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

# # ......................................................................................................................
# # ====================================================== MAIN ==========================================================
# # ......................................................................................................................

# # # ===============================================  GUI INTERFACE =====================================================
# gui = GuiInterface()
# gui.setupInterface()

# ================================================== CONSOLE INTERFACE ====================================================
#
#
# # read max time
print("Please enter maximum run time (seconds)")
maxRunTime = int(input())

# read path to problem
print("Please enter path to problem file")
path = str(input())
# reading problem
algorithmName, startNode, goalNode, mazeSize, maze = Utilities.readInstance(path)

#
# # #  OPTION 1 Run All Algorithms with all heuristics
# runOnAll(maze,maxRunTime)

# # OPTION 2 run as file request.
algorithm, isHeuristic = getAlgorithmFromString(algorithmName)
print("solving with "+algorithmName+", please wait...")
if isHeuristic is True:
    algorithm(maze, maxRunTime, "minimumMoves")
else:
    algorithm(maze, maxRunTime)

print('')
print("PRESS ENTER TO EXIT")
input()