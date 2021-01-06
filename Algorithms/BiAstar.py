import copy
import time
from DataStructures.HeapDict import HeapDict
from Entities.Node import Node
from Heuristics.Heuristics import chooseHeuristic, calculateMinimumMovesMatrixBi, calculateMinimumMovesMatrix
from Utilities import getCoordsFromDirection, evaluateStats



# this was programmed using 'AI modern approach' pseudo code for Bidirectional algorithm.
#                      @@@@ BiAstar algorithm. @@@
#      this algorithm start to search from goal node and start node simultaneously
#       until it reaches an intersection between the two and satisfy the optimality condition.



heuristicCounter = 0
heuristicSum = 0
global forwardContinue
global backwardsContinue
global turn

def BiAstar(maze,maxRunTime, heuristicName):


    # Algorithm
    startTime = time.time()

    # preprocessing for heuristic
    if heuristicName == "minimumMoves":
        calculateMinimumMovesMatrix(maze, maze.goalNode)
        calculateMinimumMovesMatrixBi(maze, maze.startNode)

    isHeuristic = True
    exploredCounter = 0
    heuristic = chooseHeuristic(heuristicName)
    global heuristicSum
    global heuristicCounter
    global forwardContinue
    global backwardsContinue
    global turn
    heuristicCounter = 0
    heuristicSum = 0
    startPoint = maze.startNode
    startPoint.childNodes = []
    startPoint.fatherNode = None

    backwardsFrontierPriorityQueue = HeapDict()
    backwardsFrontierHashTable = {}
    backwardsExploredHashTable = {}

    frontierPriorityQueue = HeapDict()
    frontierHashTable = {}
    exploredHashTable = {}

    turn = False  # True = front turn, false = backwards turn

    # calculating heuristic to first node

    startPoint.heuristicCost = heuristic(startPoint.x, startPoint.y, maze.goalNode)
    startPoint.pathCostWithHeuristic = startPoint.pathCost + startPoint.heuristicCost

    # creating startpoint of backwards search
    backwardsStartPoint = Node(maze.goalNode.x,maze.goalNode.y,maze.goalNode.cost,None,maze.goalNode.cost,
                               heuristic(maze.goalNode.x,maze.goalNode.y,startPoint)+maze.goalNode.cost,0,
                               heuristic(maze.goalNode.x,maze.goalNode.y,startPoint))


    # inserting first node at for both searches
    frontierHashTable[startPoint.key] = startPoint
    frontierPriorityQueue.push(startPoint)

    backwardsFrontierHashTable[backwardsStartPoint.key] = backwardsStartPoint
    backwardsFrontierPriorityQueue.push(backwardsStartPoint)

    forwardContinue = True
    backwardsContinue = True
    intersected = False
    optimalPathCost = None

    forwardSolutionNode = None
    backwardsSolutionNode = None

    if backwardsStartPoint.cost == -1 or startPoint.cost == -1:
        runTime = time.time() - startTime
        evaluateStats('BiAstar', maze, False, startPoint, frontierPriorityQueue, exploredCounter, runTime, isHeuristic,
                      heuristicName, 0, backwardsStartPoint, backwardsFrontierPriorityQueue,
                      backwardsStartPoint)
        return False

    # Algorithm
    while time.time() < (startTime + maxRunTime):

        # checking the optimal step to stop.
        if intersected is True and backwardsFrontierPriorityQueue.isEmpty() is False and frontierPriorityQueue.isEmpty() is False and stopCondition(frontierPriorityQueue.peekFirst(), backwardsFrontierPriorityQueue.peekFirst(),optimalPathCost) is True:
            # stop the timer
            runTime = time.time() - startTime
            if heuristicCounter == 0:
                heuristicSumOverHeuristicCounter = 0
            else:
                heuristicSumOverHeuristicCounter = heuristicSum / heuristicCounter
            evaluateStats('BiAstar', maze, True, forwardSolutionNode, frontierPriorityQueue, exploredCounter,
                          runTime, isHeuristic,
                          heuristicName, heuristicSumOverHeuristicCounter, backwardsSolutionNode,
                          backwardsFrontierPriorityQueue, backwardsStartPoint)
            return True


        if (turn is True and forwardContinue is True) or (turn is False and backwardsContinue is False): # ============================= FRONT SEARCH TURN

            if frontierPriorityQueue.isEmpty():
                runTime = time.time() - startTime
                if heuristicCounter == 0:
                    heuristicSumOverHeuristicCounter = 0
                else:
                    heuristicSumOverHeuristicCounter = heuristicSum / heuristicCounter
                evaluateStats('BiAstar', maze, False, startPoint, frontierPriorityQueue, exploredCounter, runTime,
                              isHeuristic,
                              heuristicName,heuristicSumOverHeuristicCounter , backwardsStartPoint, backwardsFrontierPriorityQueue,
                              backwardsStartPoint)
                return False


            # deleting node from frontierPriorityQueue
            node = frontierPriorityQueue.pop()
            frontierHashTable.pop(node.key)

            # appending childs so we simulate a tree
            if node != startPoint:
                node.fatherNode.childNodes.append(node)

            # checking if we hit the solution
            if isIntersecting(node,backwardsFrontierHashTable,backwardsExploredHashTable):

                # optimality condition
                if intersected == True:
                    if node.key in backwardsFrontierHashTable:
                        tmpBackwardsSolutionNode = backwardsFrontierHashTable[node.key]
                    elif node.key in backwardsExploredHashTable:
                        tmpBackwardsSolutionNode = backwardsExploredHashTable[node.key]


                if intersected is False or (node.pathCost + tmpBackwardsSolutionNode.pathCost - node.cost) < (
                            forwardSolutionNode.pathCost + backwardsSolutionNode.pathCost - forwardSolutionNode.cost):
                    intersected = True
                    forwardSolutionNode = copy.copy(node)
                    # retrieve coliding node from backward search
                    if node.key in backwardsFrontierHashTable:
                        backwardsSolutionNode = copy.copy(backwardsFrontierHashTable[node.key])
                    elif node.key in backwardsExploredHashTable:
                        backwardsSolutionNode = copy.copy(backwardsExploredHashTable[node.key])


                    optimalPathCost = forwardSolutionNode.pathCost + backwardsSolutionNode.pathCost - forwardSolutionNode.cost
                    if stopCondition(frontierPriorityQueue.peekFirst(), backwardsFrontierPriorityQueue.peekFirst(),optimalPathCost) is True:
                        # stop the timer
                        runTime = time.time() - startTime
                        if heuristicCounter == 0:
                            heuristicSumOverHeuristicCounter = 0
                        else:
                            heuristicSumOverHeuristicCounter = heuristicSum / heuristicCounter
                        evaluateStats('BiAstar', maze, True, forwardSolutionNode, frontierPriorityQueue, exploredCounter, runTime, isHeuristic,
                                      heuristicName, heuristicSumOverHeuristicCounter,backwardsSolutionNode,backwardsFrontierPriorityQueue,backwardsStartPoint)
                        return True


           # if node.key not in exploredHashTable:
            exploredCounter += 1
            exploredHashTable[node.key] = node
            expandNode(maze, node, frontierPriorityQueue, frontierHashTable, exploredHashTable,turn,heuristic)

            turn = False

        elif (turn is False and backwardsContinue is True) or (turn is True and forwardContinue is False): # ================================ BACKWARDS SEARCH TURN

            if backwardsFrontierPriorityQueue.isEmpty():
                runTime = time.time() - startTime
                if heuristicCounter == 0:
                    heuristicSumOverHeuristicCounter = 0
                else:
                    heuristicSumOverHeuristicCounter = heuristicSum / heuristicCounter
                evaluateStats('BiAstar', maze, False, startPoint, frontierPriorityQueue, exploredCounter, runTime,
                              isHeuristic,
                              heuristicName,heuristicSumOverHeuristicCounter, backwardsStartPoint, backwardsFrontierPriorityQueue,
                              backwardsStartPoint)
                return False

            # deleting node from frontierPriorityQueue
            node = backwardsFrontierPriorityQueue.pop()
            backwardsFrontierHashTable.pop(node.key)

            # appending childs so we simulate a tree
            if node.key != backwardsStartPoint.key:
                node.fatherNode.childNodes.append(node)

            # checking if we hit the solution
            if isIntersecting(node,frontierHashTable,exploredHashTable):

                # optimality condition
                if intersected == True:
                    if node.key in frontierHashTable:
                        tmpForwardSolutionNode = frontierHashTable[node.key]
                    elif node.key in exploredHashTable:
                        tmpForwardSolutionNode = exploredHashTable[node.key]

                if intersected is False or (node.pathCost + tmpForwardSolutionNode.pathCost - node.cost) < (
                        forwardSolutionNode.pathCost + backwardsSolutionNode.pathCost - forwardSolutionNode.cost):
                    intersected = True
                    backwardsSolutionNode = copy.copy(node)
                    # retrieve coliding node from front search
                    if node.key in frontierHashTable:
                        forwardSolutionNode = copy.copy(frontierHashTable[node.key])
                    elif node.key in exploredHashTable:
                        forwardSolutionNode = copy.copy(exploredHashTable[node.key])


                    optimalPathCost = forwardSolutionNode.pathCost + backwardsSolutionNode.pathCost - forwardSolutionNode.cost
                    if stopCondition(frontierPriorityQueue.peekFirst(), backwardsFrontierPriorityQueue.peekFirst(),optimalPathCost) is True:
                        # stop the timer
                        runTime = time.time() - startTime
                        if heuristicCounter == 0:
                            heuristicSumOverHeuristicCounter = 0
                        else:
                            heuristicSumOverHeuristicCounter = heuristicSum / heuristicCounter
                        evaluateStats('BiAstar', maze, True, forwardSolutionNode, frontierPriorityQueue, exploredCounter, runTime, isHeuristic,
                                  heuristicName, heuristicSumOverHeuristicCounter,backwardsSolutionNode,backwardsFrontierPriorityQueue,backwardsStartPoint)
                        return True

            #if node.key not in backwardsExploredHashTable:
            exploredCounter += 1
            backwardsExploredHashTable[node.key] = node
            expandNode(maze, node,backwardsFrontierPriorityQueue,backwardsFrontierHashTable,backwardsExploredHashTable,turn,heuristic)

            turn = True


    # time's up!
    runTime = time.time() - startTime
    if heuristicCounter == 0:
        heuristicSumOverHeuristicCounter = 0
    else:
        heuristicSumOverHeuristicCounter = heuristicSum / heuristicCounter
    evaluateStats('BiAstar', maze, False, node, frontierPriorityQueue, exploredCounter, runTime, isHeuristic,
                              heuristicName, heuristicSumOverHeuristicCounter,node,backwardsFrontierPriorityQueue,backwardsStartPoint)
    return False


# this functions receives a node and expand it in order to all direction, inserting the new expanded nodes into frontierPriorityQueue aswell.
def expandNode(maze, node, frontierPriorityQueue, frontierHashTable,exploredHashTable,turn,heuristic):
    global heuristicSum
    global heuristicCounter

    # the expansion order is opposite because last element becomes first in the heap, thus it will expand in the right order
    for direction in ['U', 'LU', 'L', 'LD', 'D', 'RD', 'R', 'RU']:

        x, y = getCoordsFromDirection(direction, node.x, node.y)
        if maze.isValidMove(x, y):
            newNodeCost = maze.getCost(x, y)

            # setting heuristic according to which search we are currently at.
            if turn is True:  # front search
                heuristicValue = heuristic(x, y, maze.goalNode)
                # heuristicValue = minimumMoves(x,y,maze.goalNode)
            elif turn is False:  # backwards search
                heuristicValue = heuristic(x, y, maze.startNode)
                # heuristicValue = minimumMovesBi(x, y, maze.goalNode)
            newNode = Node(x, y, newNodeCost, node, node.pathCost + newNodeCost,
                           node.pathCost + newNodeCost + heuristicValue, node.depth + 1, heuristicValue)

            heuristicSum += heuristicValue
            heuristicCounter += 1

            # new node, insert it to PQ and Hashtable
            if newNode.key not in exploredHashTable and newNode.key not in frontierHashTable:

                frontierPriorityQueue.push(newNode)
                frontierHashTable[newNode.key] = newNode

            # node is already in frontier
            elif newNode.key in frontierHashTable:
                if newNode.pathCostWithHeuristic < frontierHashTable[newNode.key].pathCostWithHeuristic or (
                        newNode.pathCostWithHeuristic == frontierHashTable[
                    newNode.key].pathCostWithHeuristic and newNode.heuristicCost < frontierHashTable[
                            newNode.key].heuristicCost):

                    frontierPriorityQueue.popSpecific(frontierHashTable[newNode.key])
                    frontierPriorityQueue.push(newNode)
                    frontierHashTable[newNode.key] = newNode

            # node in explored and not in frontier
            elif newNode.key in exploredHashTable and newNode.key not in frontierHashTable:
                if newNode.pathCostWithHeuristic < exploredHashTable[newNode.key].pathCostWithHeuristic or (
                        newNode.pathCostWithHeuristic == exploredHashTable[
                    newNode.key].pathCostWithHeuristic and newNode.heuristicCost < exploredHashTable[
                            newNode.key].heuristicCost):
                    frontierPriorityQueue.push(newNode)
                    frontierHashTable[newNode.key] = newNode






# checking if a node is reached in the other search.
def isIntersecting(node,frontierHashTable, exploredHashTable):

    if node.key in exploredHashTable or node.key in frontierHashTable:
        return True
    return False



def stopCondition(lowestForward,lowestBackwards,optPathCost):
    global forwardContinue
    global backwardsContinue
    global turn
    if forwardContinue is True and optPathCost <= lowestForward.pathCostWithHeuristic:
        forwardContinue = False

    if backwardsContinue is True and optPathCost <= lowestBackwards.pathCostWithHeuristic:
        backwardsContinue = False

    if backwardsContinue is False and forwardContinue is False:
        return True
    return False

