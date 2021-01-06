import time
from DataStructures.HeapDict import HeapDict
from Entities.Node import Node
from Utilities import getCoordsFromDirection, evaluateStats


# this was programmed using 'AI modern approach' pseudo code for UCS algorithm.




def UCS (maze,maxRunTime):

    # initialization
    isHeuristic = False
    exploredCounter = 0

    frontierPriorityQueue = HeapDict()
    frontierHashTable = {}
    exploredHashTable = {}

    startPoint = maze.startNode
    startPoint.childNodes = []
    startPoint.fatherNode = None
    # inserting first node
    frontierPriorityQueue.push(startPoint)
    frontierHashTable[startPoint.key] = startPoint

    # Algorithm
    startTime = time.time()
    while  time.time() < (startTime + maxRunTime) :
        if frontierPriorityQueue.isEmpty():
            runTime = time.time() - startTime
            evaluateStats('UCS', maze, False, node, frontierPriorityQueue, exploredCounter, runTime, isHeuristic)
            return False

        # deleting node from frontierPriorityQueue
        node = frontierPriorityQueue.pop()
        frontierHashTable.pop(node.key)

        # appending childs so we simulate a tree
        if node != startPoint:
            node.fatherNode.childNodes.append(node)

        if maze.isGoal(node):

            # stop the timer
            runTime = time.time() - startTime
            evaluateStats('UCS', maze, True, node, frontierPriorityQueue, exploredCounter, runTime, isHeuristic)
            return True

        exploredHashTable[node.key] = node
        exploredCounter += 1
        expandNode(maze,node,frontierPriorityQueue,frontierHashTable,exploredHashTable)

    # time's up!
    runTime = time.time() - startTime
    evaluateStats('UCS', maze, False, node, frontierPriorityQueue, exploredCounter, runTime,isHeuristic)
    return False


# this functions receives a node and expand it in order to all direction, inserting the new expanded nodes into frontierPriorityQueue aswell.
def expandNode(maze, node, frontierPriorityQueue, frontierHashTable, exploredHashTable):

    # the expansion order is opposite because last element becomes first in the heap, thus it will expand in the right order
    for direction in ['U', 'LU', 'L', 'LD', 'D', 'RD', 'R', 'RU']:

        x,y = getCoordsFromDirection(direction, node.x, node.y)

        if maze.isValidMove(x,y):
            nodeCost = maze.getCost(x,y)
            newNode = Node(x,y,nodeCost,node,node.pathCost + nodeCost,node.pathCost + nodeCost,node.depth+1)

            # new node
            if newNode.key not in exploredHashTable and newNode.key not in frontierHashTable:
                frontierPriorityQueue.push(newNode)
                frontierHashTable[newNode.key] = newNode



