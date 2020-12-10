import copy
import time
from heapq import siftup

from DataStructures.HeapDict import HeapDict
from DataStructures.PriorityQueue import PriorityQueue
from DataStructures.PriorityQueueDictionary import PriorityQueueDictionary
from Entities.Node import Node
from Heuristics.Heuristics import diagonalHeuristic, movesCountHeuristic
from Utilities import getCoordsFromDirection, evaluateStats

# this was programmed using 'AI modern approach' pseudo code for Astar algorithm.
#                      @@@@ Astar algorithm. @@@
#      this algorithm is searching the path from start to goal by evaluating
#      heuristic cost + actual cost. the solution is guaranteed to be optimal


heuristicCounter = 0
heuristicSum = 0


def Astar (maze,startPoint):
    # initialization
    isHeuristic = True

    exploredCounter = 0

    global heuristicSum
    global heuristicCounter
    heuristicCounter = 0
    heuristicSum = 0

    frontierPriorityQueue = HeapDict()
    frontierHashTable = {}
    exploredHashTable = {}

    maxRuntime = 60*60  # seconds

    # calculating heuristic to first node
    startPoint.heuristicCost = movesCountHeuristic(startPoint.x,startPoint.y,maze.goalNode)
    startPoint.pathCostWithHeuristic = startPoint.pathCost + startPoint.heuristicCost

    # inserting first node
    frontierHashTable[startPoint.key] = startPoint
    frontierPriorityQueue.push(startPoint)

    # Algorithm
    startTime = time.time()
    while time.time() < (startTime + maxRuntime):
        if frontierPriorityQueue.isEmpty():
            return False

        # deleting node from frontierPriorityQueue
        node = frontierPriorityQueue.pop()
        frontierHashTable.pop(node.key)
        # checking to see if we hit the solution
        if maze.isGoal(node):
            # stop the timer
            runTime = time.time() - startTime
            evaluateStats('Astar', maze, True, node, frontierPriorityQueue, exploredCounter, runTime, isHeuristic,'Diagonal',(heuristicSum/heuristicCounter) )
            return True

        if node.key not in exploredHashTable:
            exploredCounter += 1
        exploredHashTable[node.key] = node
        expandNode(maze, node, frontierPriorityQueue, frontierHashTable, exploredHashTable)

    # time's up!
    runTime = time.time() - startTime
    evaluateStats('Astar', maze, False, node, frontierPriorityQueue, exploredCounter, runTime, isHeuristic,isHeuristic,'Diagonal',(heuristicSum/heuristicCounter))
    return False


# this functions receives a node and expand it in order to all direction, inserting the new expanded nodes into frontierPriorityQueue aswell.
def expandNode(maze, node, frontierPriorityQueue, frontierHashTable, exploredHashTable):

    global heuristicSum
    global heuristicCounter


    # the expansion order is opposite because last element becomes first in the heap, thus it will expand in the right order
    for direction in  ['U', 'LU', 'L', 'LD', 'D', 'RD', 'R', 'RU']:

        x,y = getCoordsFromDirection(direction, node.x, node.y)
        if maze.isValidMove(x,y):
            newNodeCost = maze.getCost(x, y)
            heuristicValue = movesCountHeuristic(x,y,maze.goalNode)
            newNode = Node(x,y,newNodeCost,node,node.pathCost + newNodeCost,node.pathCost + newNodeCost +heuristicValue,node.depth+1,heuristicValue)

            heuristicSum += heuristicValue
            heuristicCounter += 1

            # new node
            if newNode.key not in exploredHashTable and newNode.key not in frontierHashTable:
                frontierPriorityQueue.push(newNode)
                frontierHashTable[newNode.key] = newNode

            # node is in frontier
            elif newNode.key in frontierHashTable:
                if newNode.pathCost < frontierHashTable[newNode.key].pathCost or (
                        newNode.pathCostWithHeuristic == frontierHashTable[
                    newNode.key].pathCostWithHeuristic and newNode.heuristicCost < frontierHashTable[
                            newNode.key].heuristicCost):

                    # # pqdict
                    # frontierPriorityQueue.replace(frontierHashTable[newNode.key],newNode)
                    # frontierHashTable[newNode.key] = newNode

                    # heapdict try
                    frontierPriorityQueue.popSpecific(frontierHashTable[newNode.key])
                    frontierPriorityQueue.push(newNode)
                    frontierHashTable[newNode.key] = newNode



                    # #updating node heapdict
                    # node = frontierHashTable[newNode.key]
                    # node.fatherNode = copy.copy(newNode.fatherNode)
                    # node.pathCost = copy.copy(newNode.pathCost)
                    # node.heuristicCost = copy.copy(newNode.heuristicCost)
                    # node.depth = copy.copy(newNode.depth)
                    # node.pathCostWithHeuristic = copy.copy(newNode.pathCostWithHeuristic)
                    # frontierPriorityQueue.decreaseKey(node, node.pathCostWithHeuristic,node.heuristicCost)
                    # #frontierHashTable[newNode.key] = node

                    # #test reg pq
                    # i = 0
                    # for e in frontierPriorityQueue.heap:
                    #
                    #     if e[1].x == newNode.x and e[1].y == newNode.y:
                    #         e[1].fatherNode = newNode.fatherNode
                    #         e[1].pathCost = newNode.pathCost
                    #         e[1].heuristicCost = newNode.heuristicCost
                    #         e[1].depth = newNode.depth
                    #         e[1].pathCostWithHeuristic = newNode.pathCostWithHeuristic
                    #         siftup(frontierPriorityQueue.heap,i)
                    #     i+=1

            # node in explored and not in frontier
            elif newNode.key in exploredHashTable and newNode.key not in frontierHashTable:
                if newNode.pathCost < exploredHashTable[newNode.key].pathCost or\
                        (newNode.pathCost == exploredHashTable[newNode.key].pathCost and newNode.pathCostWithHeuristic < exploredHashTable[
                            newNode.key].pathCostWithHeuristic):
                    frontierPriorityQueue.push(newNode)
                    frontierHashTable[newNode.key] = newNode




