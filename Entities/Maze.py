
class Maze(object):
    def __init__(self, maze,size,goalNode):
        self.maze = maze
        self.size = int(size)
        self.goalNode = goalNode

    # object to string
    def __repr__(self):
        return "graph of size " + str(self.size)

    def getCost(self,x,y):
        return self.maze[x][y]

    def isGoal(self,node):
        return (node.x,node.y) == (self.goalNode.x,self.goalNode.y)

    def isValidMove(self,x,y):
        if x < 0 or y < 0 or y > (self.size - 1) or x > (self.size - 1) or self.getCost(x,y) < 0:
            return False

        return True