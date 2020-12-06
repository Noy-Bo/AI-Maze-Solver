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
        return node



    def removeSpecific(self, x,y):
        i=0
        for node in self.heap:
            if node[1].x == x and node[1].y == y:
                self.heap.pop(i)
                break
            i+=1
        # for i in range(0,len(self.heap)-1):
        #     if self.heap[i][1].x == x and self.heap[i][1].y == y:
        #         self.heap.pop(i)

    def isEmpty(self):
        return len(self.heap) == 0
