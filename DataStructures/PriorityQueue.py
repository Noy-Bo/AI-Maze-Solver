import heapq


# NOTE - this ia a *min* heap.
class PriorityQueue(object):

    def  __init__(self):
        self.heap = []
        self.count = 0

    def push(self, node):
        heapq.heappush(self.heap,(node.pathCostWithHeuristic,node))
        self.count += 1

    def pop(self):
        (_,node) = heapq.heappop(self.heap)
        self.count -= 1
        return node

    def isEmpty(self):
        return len(self.heap) == 0