import time
from DataStructures.HeapDict import HeapDict
from Entities.Node import Node
from Heuristics.Heuristics import chooseHeuristic, calculateMinimumMovesMatrix
from Utilities import getCoordsFromDirection, evaluateStats

# this was programmed using 'AI modern approach' pseudo code for Astar algorithm.
#                      @@@@ Astar algorithm. @@@
#      this algorithm is searching the path from start to goal by evaluating
#      heuristic cost + actual cost. the solution is guaranteed to be optimal

h_time = 0
heuristicCounter = 0
heuristicSum = 0


def Astar (maze,maxRunTime,heuristicName):
    global h_time
    # starting the timer
    startTime = time.time()

    # checking if heuristic requires pre-processing
    if heuristicName == "minimumMoves":
        calculateMinimumMovesMatrix(maze, maze.goalNode)


    # initialization
    isHeuristic = True
    heuristic = chooseHeuristic(heuristicName)
    exploredCounter = 0

    global heuristicSum
    global heuristicCounter
    heuristicCounter = 0
    heuristicSum = 0

    startPoint = maze.startNode
    startPoint.childNodes = []
    startPoint.fatherNode = None
    frontierPriorityQueue = HeapDict()
    frontierHashTable = {}
    exploredHashTable = {}

    # calculating heuristic to first node
    startPoint.heuristicCost = heuristic(startPoint.x,startPoint.y,maze.goalNode)
    startPoint.pathCostWithHeuristic = startPoint.pathCost + startPoint.heuristicCost

    # inserting first node
    frontierHashTable[startPoint.key] = startPoint
    frontierPriorityQueue.push(startPoint)

    # Algorithm
    while time.time() < (startTime + maxRunTime):
        if frontierPriorityQueue.isEmpty():
            runTime = time.time() - startTime
            if heuristicCounter == 0:
                heuristicSumOverHeuristicCounter = 0
            else:
                heuristicSumOverHeuristicCounter = heuristicSum / heuristicCounter
            evaluateStats('Astar', maze, False, node, frontierPriorityQueue, exploredCounter, runTime, isHeuristic,
                          heuristicName, heuristicSumOverHeuristicCounter)
            return False

        # deleting node from frontierPriorityQueue
        node = frontierPriorityQueue.pop()
        frontierHashTable.pop(node.key)

        # appending childs so we simulate a tree
        if node != startPoint:
            node.fatherNode.childNodes.append(node)

        # checking to see if we hit the solution
        if maze.isGoal(node):
            # stop the timer
            runTime = time.time() - startTime
            if heuristicCounter == 0:
                heuristicSumOverHeuristicCounter = 0
            else:
                heuristicSumOverHeuristicCounter = heuristicSum/heuristicCounter
            evaluateStats('Astar', maze, True, node, frontierPriorityQueue, exploredCounter, runTime, isHeuristic,heuristicName,heuristicSumOverHeuristicCounter )
            return True

        #if node.key not in exploredHashTable:
        exploredCounter += 1
        exploredHashTable[node.key] = node
        expandNode(maze, node, frontierPriorityQueue, frontierHashTable, exploredHashTable,heuristic)

    # time's up!
    runTime = time.time() - startTime
    if heuristicCounter == 0:
        heuristicSumOverHeuristicCounter = 0
    else:
        heuristicSumOverHeuristicCounter = heuristicSum / heuristicCounter
    evaluateStats('Astar', maze, False, node, frontierPriorityQueue, exploredCounter, runTime, isHeuristic,heuristicName,heuristicSumOverHeuristicCounter)
    return False


# this functions receives a node and expand it in order to all direction, inserting the new expanded nodes into frontierPriorityQueue aswell.
def expandNode(maze, node, frontierPriorityQueue, frontierHashTable, exploredHashTable,heuristic):

    global heuristicSum
    global heuristicCounter
    global h_time


    # the expansion order is opposite because last element becomes first in the heap, thus it will expand in the right order
    for direction in  ['U', 'LU', 'L', 'LD', 'D', 'RD', 'R', 'RU']:

        x,y = getCoordsFromDirection(direction, node.x, node.y)
        if maze.isValidMove(x,y):
            newNodeCost = maze.getCost(x, y)
            heuristicValue = heuristic(x,y,maze.goalNode)
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

                    # heapdict
                    frontierPriorityQueue.popSpecific(frontierHashTable[newNode.key])
                    frontierPriorityQueue.push(newNode)
                    frontierHashTable[newNode.key] = newNode



