from queue import Queue

import numpy as np
from heapdict import heapdict

from DataStructures.HeapDict import HeapDict
from Utilities import getCoordsFromDirection
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
    m = movesMatrix
    # movesMatrix = [[0 for x in range(int(mazeSize))] for y in range(int(mazeSize))]
    # for i in range (0,int(mazeSize)):
    #     for j in range(0,int(mazeSize)):
    #         movesMatrix[j][i] = maxMoves

    #orderStack[str(maze.goalNode.x)+","+str(maze.goalNode.y)] = (0,maze.goalNode.x,maze.goalNode.y)
    orderStack.append((0,goalNode.x,goalNode.y))
    iterativeBFS(maze)
    return movesMatrix

def iterativeBFS(maze):
    global movesMatrix
    global orderStack
    global visited

    while len(orderStack) is not 0:

        moves,x,y  = orderStack.pop(0)

        if (str(x)+","+str(y)) not in visited:
            visited[str(x)+","+str(y)] = 1

            if movesMatrix[x][y] > moves:
                movesMatrix[x][y] = moves

                for direction in ['RU', 'R', 'RD', 'D', 'LD', 'L', 'LU', 'U']:

                    newX, newY = getCoordsFromDirection(direction, x, y)
                    if maze.isValidMove(newX, newY):
                        orderStack.append((moves+1,newX,newY))



# def iterativeBFS(maze, start, end)
#
#     q = Queue.Queue()
#     path = [start]
#     q.put(path)
#     visited = set([start])
#
#     while not q.empty():
#         path = q.get()
#         last_node = path[-1]
#         if last_node == end:
#             return path
#         for node in maze[last_node]:
#             if node not in visited:
#                 visited.add(node)
#                 q.put(path + [node])

        #     newNodeCost = maze.getCost(x, y)
        #     heuristicValue = -(node.depth + 1)
        #     newNode = Node(x, y, newNodeCost, node, node.pathCost + newNodeCost, heuristicValue, node.depth + 1,
        #                    heuristicValue)
        #     # maze.maze[node.x][node.y] = -1
        #     (result, node) = RecursiveDLS(maze, newNode, limit - 1)
        #     if result is False:
        #         cutoff_occurred = True
        #     elif result is True:
        #         return True, node
        #
        # if cutoff_occurred is True:
        #     return False, node
        # else:
        #     return False, None



