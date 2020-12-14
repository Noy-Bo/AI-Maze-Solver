import time
from Heuristics.Heuristics import  chooseHeuristic
from DataStructures.HeapDict import HeapDict
from Entities.Node import Node
from Utilities import getCoordsFromDirection, evaluateStats

# this  algorithm was programmed using 'AI modern approach' pseudo code for IDS algorithm.
#            @@@@ Iterative deepening search algorithm. @@@@
#      this algorithm is searching path to goal by looking at
#      increasing depth paths. the implementation is basically Best-First-Search
#      Note - the solution is not guaranteed to be optimal

currentFLimit = 0
globalExploredCounter = 0
heuristicCounter = 0
heuristicSum = 0

def IDAstar (maze,maxRunTime,heuristicName):
    # initialization
    global currentFLimit
    global globalExploredCounter
    global heuristicSum
    global heuristicCounter
    heuristic = chooseHeuristic(heuristicName)
    startPoint = maze.startNode
    cutOffs = []
    isHeuristic = True
    currentFLimit = 0
    startTime = time.time()
    while time.time() < (startTime + maxRunTime):

        currentFLimit += 1
        exploredCounter = 0

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
        while True:
            if frontierPriorityQueue.isEmpty():
                break;

            # deleting node from frontierPriorityQueue
            node = frontierPriorityQueue.pop()
            frontierHashTable.pop(node.key)

            # appending childs so we simulate a tree
            if node != startPoint:
                node.fatherNode.childNodes.append(node)

            # this case indicates a cut-off, this algorithm generates a cutoff when the depth limit is reached
            if node.pathCostWithHeuristic >= currentFLimit:
                cutOffs.append(node)

            # adding 1 to expanded nodes count
            globalExploredCounter += 1

            # checking to see if we hit the solution
            if maze.isGoal(node):
                # stop the timer
                runTime = time.time() - startTime
                evaluateStats('IDAstar', maze, True, node, cutOffs, globalExploredCounter, runTime, isHeuristic,heuristicName,(heuristicSum/heuristicCounter))
                return True

            if node.key not in exploredHashTable:
                exploredCounter += 1
            exploredHashTable[node.key] = node
            expandNode(maze, node, frontierPriorityQueue, frontierHashTable, exploredHashTable, currentFLimit,heuristic)



    # time's up!
    runTime = time.time() - startTime
    evaluateStats('IDAstar', maze, False, node, cutOffs, globalExploredCounter, runTime,isHeuristic,heuristicName,(heuristicSum/heuristicCounter))
    return False


# this functions receives a node and expand it in order to all direction, inserting the new expanded nodes into frontierPriorityQueue aswell.
def expandNode(maze, node, frontierPriorityQueue, frontierHashTable, exploredHashTable,FLimit,heuristic):

    global heuristicSum
    global heuristicCounter

    if (node.pathCostWithHeuristic < FLimit):

        # the expansion order is opposite because last element becomes first in the heap, thus it will expand in the right order
        for direction in ['U', 'LU', 'L', 'LD', 'D', 'RD', 'R', 'RU']:

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

                        frontierPriorityQueue.popSpecific(frontierHashTable[newNode.key])
                        frontierPriorityQueue.push(newNode)
                        frontierHashTable[newNode.key] = newNode

                # node in explored and not in frontier
                elif newNode.key in exploredHashTable and newNode.key not in frontierHashTable:
                    if newNode.pathCost < exploredHashTable[newNode.key].pathCost or\
                            (newNode.pathCost == exploredHashTable[newNode.key].pathCost and newNode.pathCostWithHeuristic < exploredHashTable[
                                newNode.key].pathCostWithHeuristic):
                        frontierPriorityQueue.push(newNode)
                        frontierHashTable[newNode.key] = newNode

