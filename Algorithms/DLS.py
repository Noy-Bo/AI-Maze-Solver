currBestPath = None
def DLS(maze,node,limit):

    global currBestPath

    if maze.isGoal(node):
        if currBestPath == None or node.pathCost < currBestPath:
            currBestPath = node.pathCost
            #save solution configuration.
        
    # this is not 100% necessary, development paused for now