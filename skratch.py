from heapdict import heapdict

from Entities.Node import Node
from Heuristics.Heuristics import movesCountHeuristic

hd = heapdict()

node1 = Node(1, 2, 3, None, 4, 10, None, 5)
node2 = Node(1, 3, 4, None, 6, 20, None, 5)
node3 = Node(51, 123, 34, None, 76, 30, None, 35)

hd[node2] = node2.pathCostWithHeuristic
hd[node1] = node1.pathCostWithHeuristic
hd[node3] = node3.pathCostWithHeuristic

#hd[node1] = None
(obj, priority) = hd.popitem()
pass

h1 = movesCountHeuristic
h1(node1.x,node1.y,node3)