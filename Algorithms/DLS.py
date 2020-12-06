import time

import fibheap

from DataStructures.PriorityQueue import PriorityQueue
from Entities.Node import Node
from Utilities import getCoordsFromDirection, getDirectionFromCoords, evaluateStats


# this was programmed using 'AI modern approach' pseudo code for UCS algorithm.

#                   DataStructures:
# frontierHashTable - Hashtable, inorder to be able to 'find' in o(1)
# explored - Hashtable to check if a node has already been visited; using python built-in dict with override hashFunction. (3.x python ver)
# fibonacci heap - to check for the next node with least cost.




def UCS (maze,startPoint):

    # initialization
    isHeuristic = False
    frontierCounter = 0
    exploredCounter = 0

    frontierPriorityQueue = PriorityQueue()
    frontierHashTable = {}
    exploredHashTable = {}

    maxRuntime = 60 # seconds

    # inserting first node
    frontierPriorityQueue.push(startPoint)
    frontierHashTable[startPoint.key] = startPoint

    # Algorithm
    startTime = time.time()
    while  time.time() < (startTime + maxRuntime) :
        if frontierPriorityQueue.isEmpty():
            return False

        # deleting node from frontierPriorityQueue
        node = frontierPriorityQueue.pop()
        frontierHashTable.pop(node.key)

        if maze.isGoal(node):

            # stop the timer
            runTime = time.time() - startTime
            evaluateStats('IDS', maze, True, node, frontierPriorityQueue, exploredCounter, runTime, isHeuristic)
            return True

        exploredHashTable[node.key] = node
        exploredCounter += 1
        expandNode(maze,node,frontierPriorityQueue,frontierHashTable,exploredHashTable)

    # time's up!
    runTime = time.time() - startTime
    evaluateStats('IDS', maze, False, node, frontierPriorityQueue, exploredCounter, runTime,isHeuristic)
    return False


# this functions receives a node and expand it in order to all direction, inserting the new expanded nodes into frontierPriorityQueue aswell.
def expandNode(maze, node, frontierPriorityQueue, frontierHashTable, exploredHashTable):

    # the expansion order is like so
    for direction in ['RU','R','RD','D','LD','L','RU','U']:

        x,y = getCoordsFromDirection(direction, node.x, node.y)

        if maze.isValidMove(x,y):
            nodeCost = maze.getCost(x,y)
            newNode = Node(x,y,nodeCost,node,node.pathCost + nodeCost,node.pathCost + nodeCost,node.depth+1)

            # new node
            if newNode.key not in exploredHashTable and newNode.key not in frontierHashTable:
                frontierPriorityQueue.push(newNode)
                frontierHashTable[newNode.key] = newNode

            # incase we already seen this node but with higher path cost.
            elif newNode.key in frontierHashTable and newNode.pathCost < frontierHashTable[newNode.key].pathCost:
                frontierHashTable[newNode.key] = newNode


