import time
from DataStructures.HeapDict import HeapDict
from Entities.Node import Node
from GUI.GUI import Pen
from Heuristics.Heuristics import chooseHeuristic
from Utilities import getCoordsFromDirection, evaluateStats


# this was programmed using 'AI modern approach' pseudo code for Astar algorithm.
#                      @@@@ Astar algorithm. @@@
#      this algorithm is searching the path from start to goal by evaluating
#      heuristic cost + actual cost. the solution is guaranteed to be optimal


pen = None
heuristicCounter = 0
heuristicSum = 0


def AstarVisual (maze,maxRunTime,heuristicName):
    global pen
    pen = Pen.getInstance()
    pen.maze_setup(maze)
    visual_counter = 1
    visual_turns = 2

    # initialization
    isHeuristic = True
    heuristic = chooseHeuristic(heuristicName)
    exploredCounter = 0

    global heuristicSum
    global heuristicCounter
    heuristicCounter = 0
    heuristicSum = 0

    startPoint = maze.startNode

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
    startTime = time.time()
    while time.time() < (startTime + maxRunTime):
        if frontierPriorityQueue.isEmpty():
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
            evaluateStats('Astar', maze, True, node, frontierPriorityQueue, exploredCounter, runTime, isHeuristic,heuristicName,(heuristicSum/heuristicCounter) )
            # mark - get_path
            pen.paint_path(node)
            return True

        #if node.key not in exploredHashTable:
        exploredCounter += 1
        exploredHashTable[node.key] = node
        expandNode(maze, node, frontierPriorityQueue, frontierHashTable, exploredHashTable,heuristic)
        # mark - expanding node, node.x/node.y - hard yellow
        visual_counter +=1
        if visual_counter > visual_turns:
            pen.paint_tile(node.x, node.y, pen.dark_green, True)
            visual_turns*=1.045
            if visual_turns > 110:
                visual_turns = 110
            visual_counter = 0
        else:
            pen.paint_tile(node.x, node.y, pen.dark_green, False)

    # time's up!
    runTime = time.time() - startTime
    evaluateStats('Astar', maze, False, node, frontierPriorityQueue, exploredCounter, runTime, isHeuristic,heuristicName,(heuristicSum/heuristicCounter))
    return False


# this functions receives a node and expand it in order to all direction, inserting the new expanded nodes into frontierPriorityQueue aswell.
def expandNode(maze, node, frontierPriorityQueue, frontierHashTable, exploredHashTable,heuristic):

    global heuristicSum
    global heuristicCounter

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
                # mark - node is valid, we're only looking at it - yellow
                pen.paint_tile(newNode.x, newNode.y, pen.light_green, False)
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

            # node in explored and not in frontier
            elif newNode.key in exploredHashTable and newNode.key not in frontierHashTable:
                if newNode.pathCost < exploredHashTable[newNode.key].pathCost or\
                        (newNode.pathCost == exploredHashTable[newNode.key].pathCost and newNode.pathCostWithHeuristic < exploredHashTable[
                            newNode.key].pathCostWithHeuristic):
                    frontierPriorityQueue.push(newNode)
                    frontierHashTable[newNode.key] = newNode




