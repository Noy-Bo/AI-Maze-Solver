import time
from DataStructures.HeapDict import HeapDict
from Entities.Node import Node
from Utilities import getCoordsFromDirection, getDirectionFromCoords, evaluateStats

#
#                   failing try of recursive DLS - fuck recursion


def DLS(maze,startNode,limit):

    #maze.maze[startNode.x][startNode.y] = -1
    (result,node) = RecursiveDLS(maze,startNode,limit)
    if result is True:
        return node


def RecursiveDLS(maze,node,limit):

    if limit > 0:
        if maze.isGoal(node):
            return True,node
        elif limit == 0:
            return False,node
        else:
            cutoff_occurred = False
            for direction in ['RU', 'R', 'RD', 'D', 'LD', 'L', 'LU', 'U']:

                x, y = getCoordsFromDirection(direction, node.x, node.y)
                if maze.isValidMove(x, y):
                    newNodeCost = maze.getCost(x, y)
                    heuristicValue = -(node.depth + 1)
                    newNode = Node(x, y, newNodeCost, node, node.pathCost + newNodeCost, heuristicValue, node.depth + 1,
                                   heuristicValue)
                    #maze.maze[node.x][node.y] = -1
                    (result,node) =  RecursiveDLS(maze,newNode,limit-1)
                    if result is False:
                        cutoff_occurred = True
                    elif result is True:
                        return True,node

                if cutoff_occurred is True:
                    return False,node
                else:
                    return False,None


