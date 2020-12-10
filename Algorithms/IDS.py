import time

from DataStructures.HeapDict import HeapDict
from Entities.Node import Node
from Utilities import getCoordsFromDirection, evaluateStats

# this  algorithm was programmed using 'AI modern approach' pseudo code for IDS algorithm.
#            @@@@ Iterative deepening search algorithm. @@@@
#      this algorithm is searching path to goal by looking at
#      increasing depth paths. the implementation is basically Best-First-Search
#      Note - the solution is not guaranteed to be optimal

currentDepthLimit = -1
globalExploredCounter = 0

def IDS (maze,startPoint):
    # initialization
    global currentDepthLimit
    global globalExploredCounter
    cutOffs = []
    isHeuristic = False
    currentDepthLimit = -1
    maxRuntime = 60  * 3  # seconds
    startTime = time.time()
    while time.time() < (startTime + maxRuntime):

        currentDepthLimit += 1
        exploredCounter = 0

        frontierPriorityQueue = HeapDict()
        frontierHashTable = {}
        exploredHashTable = {}



        # calculating heuristic to first node
        startPoint.heuristicCost = -startPoint.depth
        startPoint.pathCostWithHeuristic = startPoint.heuristicCost

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

            # this case indicates a cut-off, this algorithm generates a cutoff when the depth limit is reached
            if node.depth == currentDepthLimit:
                cutOffs.append(node)

            # adding 1 to expanded nodes count
            globalExploredCounter += 1

            # checking to see if we hit the solution
            if maze.isGoal(node):
                # stop the timer
                runTime = time.time() - startTime
                node.depth = currentDepthLimit
                evaluateStats('IDS', maze, True, node, cutOffs, globalExploredCounter, runTime, isHeuristic)
                return True

            if node.key not in exploredHashTable:
                exploredCounter += 1
            exploredHashTable[node.key] = node
            expandNode(maze, node, frontierPriorityQueue, frontierHashTable, exploredHashTable, currentDepthLimit)



    # time's up!
    runTime = time.time() - startTime
    node.depth = currentDepthLimit
    evaluateStats('IDS', maze, False, node, cutOffs, globalExploredCounter, runTime, isHeuristic)
    return False


# this functions receives a node and expand it in order to all direction, inserting the new expanded nodes into frontierPriorityQueue aswell.
def expandNode(maze, node, frontierPriorityQueue, frontierHashTable, exploredHashTable,depthLimit):

    global heuristicSum
    global heuristicCounter

    if (node.depth < depthLimit):

        # the expansion order is opposite because last element becomes first in the heap, thus it will expand in the right order
        for direction in ['U', 'LU', 'L', 'LD', 'D', 'RD', 'R', 'RU']:

            x,y = getCoordsFromDirection(direction, node.x, node.y)
            if maze.isValidMove(x,y):
                newNodeCost = maze.getCost(x, y)
                heuristicValue = -(node.depth+1)
                newNode = Node(x,y,newNodeCost,node,node.pathCost + newNodeCost,heuristicValue,node.depth+1,heuristicValue)


                # new node
                if newNode.key not in exploredHashTable and newNode.key not in frontierHashTable:
                    frontierPriorityQueue.push(newNode)
                    frontierHashTable[newNode.key] = newNode

                # node is in frontier
                elif newNode.key in frontierHashTable:
                    if newNode.depth < frontierHashTable[newNode.key].depth or (newNode.pathCostWithHeuristic == frontierHashTable[newNode.key].pathCostWithHeuristic and newNode.heuristicCost < frontierHashTable[newNode.key].heuristicCost):
                        # #updating node
                        # node = frontierHashTable[newNode.key]
                        # node.fatherNode = newNode.fatherNode
                        # node.pathCost = newNode.pathCost
                        # node.heuristicCost = newNode.heuristicCost
                        # node.depth = newNode.depth
                        # node.pathCostWithHeuristic = newNode.pathCostWithHeuristic
                        # frontierPriorityQueue.decreaseKey(node,newNode.pathCostWithHeuristic)


                        frontierPriorityQueue.popSpecific(frontierHashTable[newNode.key])
                        frontierPriorityQueue.push(newNode)
                        frontierHashTable[newNode.key] = newNode

                # node in explored and not in frontier
                elif newNode.key in exploredHashTable and newNode.key not in frontierHashTable:
                    if newNode.depth < exploredHashTable[newNode.key].depth or ( newNode.depth == exploredHashTable[newNode.key].depth and newNode.heuristicCost < exploredHashTable[newNode.key].heuristicCost):
                        frontierPriorityQueue.push(newNode)
                        frontierHashTable[newNode.key] = newNode

