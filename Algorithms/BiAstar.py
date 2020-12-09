import time
from DataStructures.PriorityQueue import PriorityQueue
from Entities.Node import Node
from Heuristics.Heuristics import diagonalHeuristic, movesCountHeuristic
from Utilities import getCoordsFromDirection, evaluateStats


# this was programmed using 'AI modern approach' pseudo code for Bidirectional algorithm.
#                      @@@@ BiAstar algorithm. @@@
#      this algorithm start to search from goal node and start node simultaneously
#       until it reaches an intersection between the two.
#       Note - BiAstar doesnt guarantee to return optimal solution



heuristicCounter = 0
heuristicSum = 0


def BiAstar(maze, startPoint):
    # initialization

    isHeuristic = True
    exploredCounter = 0

    global heuristicSum
    global heuristicCounter
    heuristicCounter = 0
    heuristicSum = 0

    backwardsFrontierPriorityQueue = PriorityQueue()
    backwardsFrontierHashTable = {}
    backwardsExploredHashTable = {}

    frontierPriorityQueue = PriorityQueue()
    frontierHashTable = {}
    exploredHashTable = {}

    turn = False  # True = front turn, false = backwards turn

    maxRuntime = 60 * 60  # seconds

    # calculating heuristic to first node

    startPoint.heuristicCost = movesCountHeuristic(startPoint.x, startPoint.y, maze.goalNode)
    startPoint.pathCostWithHeuristic = startPoint.pathCost + startPoint.heuristicCost

    # creating startpoint of backwards search
    backwardsStartPoint = Node(maze.goalNode.x,maze.goalNode.y,maze.goalNode.cost,None,maze.goalNode.cost,
                               movesCountHeuristic(maze.goalNode.x,maze.goalNode.y,startPoint)+maze.goalNode.cost,0,
                               movesCountHeuristic(maze.goalNode.x,maze.goalNode.y,startPoint))


    # inserting first node at for both searches
    frontierHashTable[startPoint.key] = startPoint
    frontierPriorityQueue.push(startPoint)

    backwardsFrontierHashTable[backwardsStartPoint.key] = backwardsStartPoint
    backwardsFrontierPriorityQueue.push(backwardsStartPoint)

    # Algorithm
    startTime = time.time()
    while time.time() < (startTime + maxRuntime):

        if turn is True: # ============================= FRONT SEARCH TURN

            if frontierPriorityQueue.isEmpty():
                return False

            # deleting node from frontierPriorityQueue
            node = frontierPriorityQueue.pop()
            frontierHashTable.pop(node.key)

            # checking if we hit the solution
            if isIntersecting(node,backwardsFrontierHashTable,backwardsExploredHashTable):
                # stop the timer
                runTime = time.time() - startTime

                # retrieve coliding node from backward search
                if node.key in backwardsFrontierHashTable:
                    backwardsNode = backwardsFrontierHashTable[node.key]
                elif node.key in backwardsExploredHashTable:
                    backwardsNode = backwardsExploredHashTable[node.key]
                else:
                    print("Error")
                    return False

                evaluateStats('BiAstar', maze, True, node, frontierPriorityQueue, exploredCounter, runTime, isHeuristic,
                              'Diagonal', (heuristicSum / heuristicCounter),backwardsNode,backwardsFrontierPriorityQueue)
                return True

            if node.key not in exploredHashTable:
                exploredCounter += 1
            exploredHashTable[node.key] = node
            expandNode(maze, node, frontierPriorityQueue, frontierHashTable, exploredHashTable,turn)

            turn = False

        elif turn is False: # ================================ BACKWARDS SEARCH TURN

            if backwardsFrontierPriorityQueue.isEmpty():
                return False

            # deleting node from frontierPriorityQueue
            node = backwardsFrontierPriorityQueue.pop()
            backwardsFrontierHashTable.pop(node.key)

            # checking if we hit the solution
            if isIntersecting(node,frontierHashTable,exploredHashTable):
                # stop the timer
                runTime = time.time() - startTime

                # retrieve coliding node from front search
                if node.key in frontierHashTable:
                    frontierNode = frontierHashTable[node.key]
                elif node.key in exploredHashTable:
                    frontiernode = exploredHashTable[node.key]
                else:
                    print("Error")
                    return False

                evaluateStats('BiAstar', maze, True, frontierNode, frontierPriorityQueue, exploredCounter, runTime, isHeuristic,
                              'Diagonal', (heuristicSum / heuristicCounter),node,backwardsFrontierPriorityQueue)
                return True

            if node.key not in backwardsExploredHashTable:
                exploredCounter += 1
            backwardsFrontierHashTable[node.key] = node
            expandNode(maze, node,backwardsFrontierPriorityQueue,backwardsFrontierHashTable,backwardsExploredHashTable,turn)

            turn = True


    # time's up!
    runTime = time.time() - startTime
    evaluateStats('BiAstar', maze, False, node, frontierPriorityQueue, exploredCounter, runTime, isHeuristic, isHeuristic,
                  'Diagonal')
    return False


# this functions receives a node and expand it in order to all direction, inserting the new expanded nodes into frontierPriorityQueue aswell.
def expandNode(maze, node, frontierPriorityQueue, frontierHashTable,exploredHashTable,turn):
    global heuristicSum
    global heuristicCounter

    # the expansion order is like so
    for direction in ['RU', 'R', 'RD', 'D', 'LD', 'L', 'LU', 'U']:

        x, y = getCoordsFromDirection(direction, node.x, node.y)
        if maze.isValidMove(x, y):
            newNodeCost = maze.getCost(x, y)

            # setting heuristic according to which search we are currently at.
            if turn is True: #front search
                heuristicValue = movesCountHeuristic(x, y, maze.goalNode)
            elif turn is False: # backwards search
                heuristicValue = movesCountHeuristic(x, y, maze.startNode)

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
                    # updating node
                    node = frontierHashTable[newNode.key]
                    node.fatherNode = newNode.fatherNode
                    node.pathCost = newNode.pathCost
                    node.heuristicCost = newNode.heuristicCost
                    node.depth = newNode.depth
                    node.pathCostWithHeuristic = newNode.pathCostWithHeuristic
                    frontierPriorityQueue.decreaseKey(node, newNode.pathCostWithHeuristic)

                    frontierHashTable[newNode.key] = node

            # node in explored and not in frontier
            elif newNode.key in exploredHashTable and newNode.key not in frontierHashTable:
                if newNode.pathCostWithHeuristic < exploredHashTable[newNode.key].pathCostWithHeuristic or (
                        newNode.pathCostWithHeuristic == exploredHashTable[
                    newNode.key].pathCostWithHeuristic and newNode.heuristicCost < exploredHashTable[
                            newNode.key].heuristicCost):
                    frontierPriorityQueue.push(newNode)
                    frontierHashTable[newNode.key] = newNode
                    # remove from explored????





# checking if a node is reached in the other search.
def isIntersecting(node,frontierHashTable, exploredHashTable):

    if node.key in frontierHashTable or node.key in exploredHashTable:
        return True
    return False