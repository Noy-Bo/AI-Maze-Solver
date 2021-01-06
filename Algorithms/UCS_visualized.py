import time
from DataStructures.HeapDict import HeapDict
from Entities.Node import Node
from GUI.GUI import Pen
from Utilities import getCoordsFromDirection, getDirectionFromCoords, evaluateStats


# this was programmed using 'AI modern approach' pseudo code for UCS algorithm.

#                   DataStructures:
# frontierHashTable - Hashtable, inorder to be able to 'find' in o(1)
# explored - Hashtable to check if a node has already been visited; using python built-in dict with override hashFunction. (3.x python ver)
# fibonacci heap - to check for the next node with least cost.

pen = None

def UCSVisual (maze,maxRunTime):

    global pen
    pen = Pen.getInstance()
    pen.maze_setup(maze)
    visual_counter = 1
    visual_turns = 2

    # initialization
    isHeuristic = False
    frontierCounter = 0
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
            # mark - print path to goal
            pen.paint_path(node)
            return True

        exploredHashTable[node.key] = node
        exploredCounter += 1
        expandNode(maze,node,frontierPriorityQueue,frontierHashTable,exploredHashTable)

        # visualize painting green expanded nodes + painting rate increase when algorithm has higher run time
        visual_counter += 1
        if visual_counter > visual_turns:
            pen.paint_tile(node.x, node.y, pen.dark_green, True)
            visual_turns *= 1.045
            if visual_turns > 110:
                visual_turns = 110
            visual_counter = 0
        else:
            pen.paint_tile(node.x, node.y, pen.dark_green, False)

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
                # painting frontier node in yellow
                pen.paint_tile(newNode.x, newNode.y, pen.light_green, False)

            # # incase we already seen this node but with higher path cost.
            # elif newNode.key in frontierHashTable and newNode.pathCost < frontierHashTable[newNode.key].pathCost:
            #     #frontierHashTable[newNode.key] = newNode
            #     frontierPriorityQueue.removeSpecific(newNode.x,newNode.y)  # this is o(n), need to think of a better way to do it
            #     frontierPriorityQueue.push(newNode)
            #     frontierHashTable[newNode.key] = newNode


