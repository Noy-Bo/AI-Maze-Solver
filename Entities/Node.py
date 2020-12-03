class Node(object):
    def __init__(self, x, y, cost, fatherNode = None, pathCost = None, pathCostWithHeuristic = None, depth=None):
        self.cost = cost
        self.x = x
        self.y = y
        self.pathCost = pathCost
        self.fatherNode = fatherNode
        self.key = "node coords: " + str(self.x) + "," + str(self.y) + "  node cost: " + str(self.cost)
        self.pathCostWithHeuristic = pathCostWithHeuristic # NOTE this is the keyValue that PQ is sorted by
        self.depth = depth


    def __hash__(self):
        return hash((self.x,self.y))

        # object to string
    def __repr__(self):
        return "node coords: " + str(self.x) + "," + str(self.y) + "  node cost: " + str(self.cost) + " path cost: " + str(self.pathCost)

    def __lt__(self, other):
        if self.pathCost < other.pathCost:
            return self
        return other

    def __le__(self,other):
        if self.pathCost <= other.pathCost:
            return self
        return other