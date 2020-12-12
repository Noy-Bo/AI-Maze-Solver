# this heuristic calculate how many moves is it to goal and tries to prefer diagonal moves.
def diagonalHeuristic(x,y,goalNode):

    maxDistance = max(abs(x - goalNode.x),abs(y - goalNode.y))
    minDistance = min(abs(x - goalNode.x),abs(y - goalNode.y))

    diagonalMoveCost = 0.58 #   ~(2 - sqrt(2))
    regularMoveCost = 1

    h = diagonalMoveCost*minDistance + regularMoveCost*(maxDistance-minDistance)

    return h


# should be optimal for our config, this hueristic calculate the minimum moves to reach the goal node.
def movesCountHeuristic(x, y, goalNode):

    dx = abs(x - goalNode.x)
    dy = abs(y - goalNode.y)
    return ((dx + dy) - min(dx, dy))


# string to function
def chooseHeuristic(heuristicName):
    if heuristicName == 'movesCount':
        h = movesCountHeuristic
        return h
    elif heuristicName == 'diagonal':
        h = diagonalHeuristic
        return h
    else:
        return "ERROR"
