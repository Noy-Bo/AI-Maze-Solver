class Node(object):
    def __init__(self, x, y, cost, fatherNode = None, pathCost = None, pathCostWithHeuristic = None, depth=None, heuristicCost = None):
        self.cost = cost
        self.x = int(x)
        self.y = int(y)
        self.pathCost = pathCost
        self.fatherNode = fatherNode
        self.key = "node coords: " + str(self.x) + "," + str(self.y) + "  node cost: " + str(self.cost)
        self.pathCostWithHeuristic = pathCostWithHeuristic # NOTE this is the keyValue that PQ is sorted by
        self.depth = depth
        self.heuristicCost = heuristicCost
        self.childNodes = []
        self.directionScore = 0




    def __hash__(self):
        return hash((self.x,self.y))

        # object to string
    def __repr__(self):
        return "node coords: " + str(self.x) + "," + str(self.y) + "  node cost: " + str(self.cost) + " path cost: " + str(self.pathCost)

    def __lt__(self, other):
        if self.pathCostWithHeuristic > other.pathCostWithHeuristic:
            return other
        elif self.pathCostWithHeuristic == other.pathCostWithHeuristic:
            if self.heuristicCost is not None:
                if self.heuristicCost > other.heuristicCost:
                    return other


        return self

    def __le__(self,other):
        if self.pathCostWithHeuristic < other.pathCostWithHeuristic:
            return self
        elif self.pathCostWithHeuristic == other.pathCostWithHeuristic:
            if self.heuristicCost < other.heuristicCost:
                return self
        return other