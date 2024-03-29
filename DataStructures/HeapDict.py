from heapdict import heapdict
# NOTE - this ia a *min* heap.

class HeapDict(object):

    def  __init__(self):
        self.heap = heapdict()
        self.count = 0

    def push(self, node):
        self.heap[node] = (node.pathCostWithHeuristic,node.heuristicCost)
        self.count += 1

    def popSpecific(self,node):
        self.heap.pop(node)
        self.count -= 1
        return;

    def pop(self):
        (node, priority) = self.heap.popitem()
        self.count -= 1
        return node

    def decreaseKey(self, node,newPathCostWIthHeuristic,newHeuristicCost):
        self.heap[node] = (newPathCostWIthHeuristic,newHeuristicCost)

    def accessSpecific(self,node):
        return self.heap[node]

    def isEmpty(self):
        return len(self.heap) == 0

    def peekFirst(self):
        return self.heap.peekitem()[0]

    def minH(self):
        minNode = None
        for idx in range(0,len(self.heap.heap)):
            if minNode is None:
                minNode = self.heap.heap[idx][1]
            else:
                if self.heap.heap[idx][1].heuristicCost < minNode.heuristicCost:
                    minNode = self.heap.heap[idx][1]

        return minNode
