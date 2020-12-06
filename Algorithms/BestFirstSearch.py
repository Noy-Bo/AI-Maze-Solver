from DataStructures.PriorityQueue import PriorityQueue
from Entities.Node import Node
from Heuristics.Heuristics import movesCountHeuristic
from Utilities import evaluateStats, getCoordsFromDirection


def RBFS(maze,node):

    # if problem.GOAL-TEST(node.STATE) then return SOLUTION(node)
    if maze.isGoal(node):
        #evaluateStats('Astar', maze, True, node, frontierPriorityQueue, exploredCounter, runTime, isHeuristic,
        #              'Diagonal', (heuristicSum / heuristicCounter))
        return True

    # successors ←[]
    frontierPriorityQueue = PriorityQueue()
    frontierHashTable = {}
    exploredHashTable = {}

    # for each action in problem.ACTIONS(node.STATE) do add CHILD-NODE(problem, node, action)into successors
    expandNode(maze, node, frontierPriorityQueue, frontierHashTable, exploredHashTable)

    # if successors is empty then return failure, ∞
    if frontierPriorityQueue.isEmpty() == True:
        return False

    # for each s in successors do /* update f with value from previous search, if any */ s.f ←max(s.g + s.h, node.f))







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

            # incase we already seen this node but with higher pathcost \\ incase we seen this node with same pathcost but higher heuristic value
            elif newNode.key in frontierHashTable and (newNode.pathCostWithHeuristic < frontierHashTable[newNode.key].pathCostWithHeuristic \
                    or newNode.pathCostWithHeuristic == frontierHashTable[newNode.key].pathCostWithHeuristic and newNode.heuristicCost < frontierHashTable[newNode.key].heuristicCost):
                frontierHashTable[newNode.key] = newNode