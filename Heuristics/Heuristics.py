# this heuristic calculate how many moves is it to goal and tries to prefer diagonal moves.
from Heuristics.MinimumMoves import HeuristicEvauluationSearch
evalMovesMatrix = None
evalMovesMatrixBackwards = None
minVal = None

def updateMinVal(val):
    global minVal
    minVal = val

# def diagonalHeuristic(x,y,goalNode):
#
#     maxDistance = max(abs(x - goalNode.x),abs(y - goalNode.y))
#     minDistance = min(abs(x - goalNode.x),abs(y - goalNode.y))
#
#     diagonalMoveCost = 1 #   ~(2 - sqrt(2))
#     regularMoveCost = 1
#
#     h = diagonalMoveCost*minDistance + regularMoveCost*(maxDistance-minDistance)
#
#     return h

# should be optimal for our config, this hueristic calculate the minimum moves to reach the goal node.
def movesCountHeuristic(x, y, goalNode):

    dx = abs(x - goalNode.x)
    dy = abs(y - goalNode.y)
    h = ((dx + dy) - min(dx, dy))
    return h

def minimumMovesBi(x,y,goal):
    global evalMovesMatrixBackwards
    return evalMovesMatrixBackwards[x][y] * minVal

def minimumMoves(x,y,goal):
    global evalMovesMatrix
    global minVal
    return evalMovesMatrix[x][y] * minVal

def calculateMinimumMovesMatrix(maze,goalNode):
    global evalMovesMatrix
    global minVal
    evalMovesMatrix,val = HeuristicEvauluationSearch(maze,goalNode)
    minVal = val

def calculateMinimumMovesMatrixBi(maze,goalNode):
    global evalMovesMatrixBackwards
    evalMovesMatrixBackwards,v = HeuristicEvauluationSearch(maze,goalNode)



# string to function
def chooseHeuristic(heuristicName):
    if heuristicName == 'movesCount':
        h = movesCountHeuristic
        return h
    # elif heuristicName == 'diagonal':
    #     h = diagonalHeuristic
    #     return h
    elif heuristicName == 'minimumMoves':
        h = minimumMoves
        return h
    else:
        return "ERROR"
