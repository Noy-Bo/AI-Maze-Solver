from pqdict import minpq


# NOTE - this ia a *min* heap.


# NOT IN USE



class PriorityQueueDictionary(object):

    def  __init__(self):
        self.pq = minpq()
        self.count = 0

    def push(self, node):
        self.pq[node] = (node.pathCostWithHeuristic,node.heuristicCost)
        self.count += 1

    def pop(self):
        node = self.pq.pop()
        self.count -= 1
        return node

    def replace(self, oldNode,newNode):
        del self.pq[oldNode]
        self.pq[newNode] = (newNode.pathCostWithHeuristic,newNode.heuristicCost)


    def isEmpty(self):
        return self.count == 0
