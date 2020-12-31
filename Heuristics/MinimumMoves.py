from queue import Queue

import numpy as np
from heapdict import heapdict
from DataStructures.HeapDict import HeapDict
from Utilities import getCoordsFromDirection
class miniNode(object):
    def __init__(self, x, y,moves,fatherNode = None):

        self.x= int(x)
        self.y = int(y)
        self.fatherNode = fatherNode
        self.key = str(self.x) + "," + str(self.y)

orderStack = []
movesMatrix = None
visited = {}

def HeuristicEvauluationSearch(maze,goalNode):
    global movesMatrix
    global orderStack
    global visited


    orderStack = []
    movesMatrix = None
    visited = {}
    # initializing the maze

    mazeSize = maze.size
    maxMoves = (mazeSize*mazeSize)+1
    movesMatrix = np.ones((mazeSize,mazeSize))*maxMoves


    #orderStack[str(maze.goalNode.x)+","+str(maze.goalNode.y)] = (0,maze.goalNode.x,maze.goalNode.y)
    startNode = miniNode(goalNode.x,goalNode.y,0)
    orderStack.append((0,goalNode.x,goalNode.y))
    iterativeBFS(maze)
    return movesMatrix

# #killing dead ends
# def iterativeBFS(maze):
#     global movesMatrix
#     global orderStack
#     global visited
#
#     while len(orderStack) is not 0:
#
#         moves,node = orderStack.pop(0)
#         visited[node.key] = 1
#         x = node.x
#         y = node.y
#         if movesMatrix[x][y] > moves:
#             movesMatrix[x][y] = moves
#
#             successExpands = 0
#             invalidCounter = 0
#             for direction in ['RU', 'R', 'RD', 'D', 'LD', 'L', 'LU', 'U']:
#
#                 newX, newY = getCoordsFromDirection(direction, x, y)
#                 newNode = miniNode(newX,newY,moves+1,node)
#                 if maze.isValidMove(newX, newY):
#                     if(newNode.key) not in visited:
#                         orderStack.append((moves+1,newNode))
#                         successExpands += 1
#                 else:
#                     invalidCounter +=1
#
#             if successExpands == 0 and invalidCounter == 7 and x != maze.goalNode.x and y != maze.goalNode.y:
#                 movesMatrix[x][y] = 99999
#                 killDeadEndsPath(maze,node.fatherNode)



def killDeadEndsPath(maze,node):
    global movesMatrix
    x = node.x
    y = node.y


    successExpands = 0
    for direction in ['RU', 'R', 'RD', 'D', 'LD', 'L', 'LU', 'U']:
        newX, newY = getCoordsFromDirection(direction, x, y)
        if maze.isValidMove(newX, newY) and node.fatherNode.x != newX and node.fatherNode.y != newY:
                successExpands += 1

    if successExpands == 1 and x != maze.goalNode.x and y != maze.goalNode.y:
        movesMatrix[x][y] = 99999
        killDeadEndsPath(maze,node.fatherNode)
    else:
        return



def iterativeBFS(maze):
    global movesMatrix
    global orderStack
    global visited

    while len(orderStack) is not 0:

        moves,x,y = orderStack.pop(0)
        visited[str(x)+","+str(y)] = 1

        if movesMatrix[x][y] > moves:
            movesMatrix[x][y] = moves


            for direction in ['RU', 'R', 'RD', 'D', 'LD', 'L', 'LU', 'U']:

                newX, newY = getCoordsFromDirection(direction, x, y)
                if maze.isValidMove(newX, newY) and (str(newX)+","+str(newY)) not in visited:
                        orderStack.append((moves+1,newX,newY))
