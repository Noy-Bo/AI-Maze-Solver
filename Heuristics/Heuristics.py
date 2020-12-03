

# should be optimal for our config, this hueristic calculate the shortest path to goal considering diagonal moves are allowed.
def diagonalHeuristic(x,y,goalNode):

    maxDistance = max(abs(x - goalNode.x),abs(y - goalNode.y))
    minDistance = min(abs(x - goalNode.x),abs(y - goalNode.y))

    diagonalMoveCost = 1.1414/2
    regularMoveCost = 1

    h = diagonalMoveCost*minDistance + regularMoveCost*(maxDistance-minDistance)

    return h

