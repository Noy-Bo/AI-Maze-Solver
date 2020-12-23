import time
from turtle import TurtleScreen, RawTurtle, Screen, RawPen, Turtle

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

from tkinter import*
from tkinter import ttk, filedialog

from GUI.GUI_interface import GuiInterface
from Heuristics.Heuristics import calculateMinimumMovesMatrix
from Heuristics.MinimumMoves import HeuristicEvauluationSearch


def getAlgorithmFromString(algorithmString, isVisual):
    if algorithmString.lower() == "biastar":
        if isVisual is True:
            return BiAstarVisual, True
        else:
            return BiAstar, True

    elif algorithmString.lower() == "astar":
        if isVisual is True:
            return AstarVisual, True
        else:
            return Astar, True

    elif algorithmString.lower() == "idastar":
        if isVisual is True:
            return IDAstarVisual, True
        else:
            return IDAstar, True

    elif algorithmString.lower() == "ids":
        if isVisual is True:
            return IDSVisual, False
        else:
            return IDS, False

    elif algorithmString.lower() == "ucs":
        if isVisual is True:
            return UCSVisual, False
        else:
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


# ======= GUI INTERFACE
gui = GuiInterface()
gui.setupInterface()

# ======================== main ========================
# ask if to visualize
# print("would you like to see visualization? Y/N ")
# isVisual = str(input())
# if isVisual.lower() == 'y':
#     isVisual = True
# else:
#     isVisual = False
# # read max time
# print("Please enter maximum run time (seconds)")
# maxRunTime = int(input())
#
# # read path to problem
# print("Please enter path to problem file")
# path = str(input())
# # reading problem
# algorithmName, startNode, goalNode, mazeSize, maze = Utilities.readInstance(path)
#
# #test
# tick = time.time()
# heuristicEvaluationMatrix = calculateMinimumMovesMatrix(maze,maze.goalNode)
# tock = time.time() - tick
# print(tock)
# # run on all
# #runOnAll(maze,maxRunTime)
#
# # # run as requeusted
#
# algorithm, isHeuristic = getAlgorithmFromString(algorithmName,isVisual)
# print("solving with "+algorithmName+", please wait...")
# if isHeuristic is True:
#     algorithm(maze, maxRunTime, "movesCount")
#     algorithm(maze, maxRunTime, "minimumMoves")
# else:
#     algorithm(maze, maxRunTime)
#
# print('')
# print("PRESS ENTER TO EXIT")
# input()