import time
from DataStructures.PriorityQueue import PriorityQueue
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

    frontierPriorityQueue = PriorityQueue()
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
            evaluateStats('Astar', maze, True, node, frontierPriorityQueue, exploredCounter, runTime, isHeuristic,'Diagonal', (heuristicSum/heuristicCounter))
            return True

        if node.key not in exploredHashTable:
            exploredCounter += 1
        exploredHashTable[node.key] = node
        expandNode(maze, node, frontierPriorityQueue, frontierHashTable, exploredHashTable)

    # time's up!
    runTime = time.time() - startTime
    evaluateStats('Astar', maze, False, node, frontierPriorityQueue, exploredCounter, runTime, isHeuristic,isHeuristic,'Diagonal')
    return False


# this functions receives a node and expand it in order to all direction, inserting the new expanded nodes into frontierPriorityQueue aswell.
def expandNode(maze, node, frontierPriorityQueue, frontierHashTable, exploredHashTable):

    global heuristicSum
    global heuristicCounter

    # the expansion order is like so
    for direction in ['RU','R','RD','D','LD','L','RU','U']:

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
                if newNode.pathCostWithHeuristic < frontierHashTable[newNode.key].pathCostWithHeuristic or (newNode.pathCostWithHeuristic == frontierHashTable[newNode.key].pathCostWithHeuristic and newNode.heuristicCost < frontierHashTable[newNode.key].heuristicCost):

                    #updating node
                    node = frontierHashTable[newNode.key]
                    node.fatherNode = newNode.fatherNode
                    node.pathCost = newNode.pathCost
                    node.heuristicCost = newNode.heuristicCost
                    node.depth = newNode.depth
                    node.pathCostWithHeuristic = newNode.pathCostWithHeuristic
                    frontierPriorityQueue.decreaseKey(node,newNode.pathCostWithHeuristic)

                    frontierHashTable[newNode.key] = node

            # node in explored and not in frontier
            elif newNode.key in exploredHashTable and newNode.key not in frontierHashTable:
                if newNode.pathCostWithHeuristic < exploredHashTable[newNode.key].pathCostWithHeuristic or ( newNode.pathCostWithHeuristic == exploredHashTable[newNode.key].pathCostWithHeuristic and newNode.heuristicCost < exploredHashTable[newNode.key].heuristicCost):
                    frontierPriorityQueue.push(newNode)
                    frontierHashTable[newNode.key] = newNode
                    #remove from explored????
