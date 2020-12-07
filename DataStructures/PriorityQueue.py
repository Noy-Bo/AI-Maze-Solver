import heapq


# NOTE - this ia a *min* heap.
from heapdict import heapdict


class PriorityQueue(object):

    def  __init__(self):
        self.heap = heapdict()
        self.count = 0

    def push(self, node):

        self.heap[node] = node.pathCostWithHeuristic
        self.count += 1

    def pop(self):
        (node, priority) = self.heap.popitem()
        self.count -= 1
        return node



    def decreaseKey(self, node,newPathCostWIthHeuristic):

        self.heap[node] = newPathCostWIthHeuristic
        # i=0
        # for node in self.heap:
        #     if node[1].x == x and node[1].y == y:
        #         self.heap.pop(i)
        #         break
        #     i+=1
        # for i in range(0,len(self.heap)-1):
        #     if self.heap[i][1].x == x and self.heap[i][1].y == y:
        #         self.heap.pop(i)

    def isEmpty(self):
        return len(self.heap) == 0
