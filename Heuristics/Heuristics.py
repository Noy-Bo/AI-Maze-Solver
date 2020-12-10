

# should be optimal for our config, this hueristic calculate the shortest path to goal considering diagonal moves are allowed.
def diagonalHeuristic(x,y,goalNode):

    maxDistance = max(abs(x - goalNode.x),abs(y - goalNode.y))
    minDistance = min(abs(x - goalNode.x),abs(y - goalNode.y))

    diagonalMoveCost = 0.9999
    regularMoveCost = 0.9999

    h = diagonalMoveCost*minDistance + regularMoveCost*(maxDistance-minDistance)

    return h

def movesCountHeuristic(x,y,goalNode):

    dx = abs(x - goalNode.x)
    dy = abs(y - goalNode.y)
    return ((dx + dy) - min(dx, dy))
