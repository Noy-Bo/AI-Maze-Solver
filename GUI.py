import turtle


class Pen(turtle.Turtle):
    def __init__(self, maze):
        turtle.Turtle.__init__(self)
        self.color('')
        wn = turtle.Screen()
        wn.setup(620, 620)
        wn.bgcolor("white")
        wn.title("Maze")
        wn.tracer(0, 0)
        # turtle.tracer(0, 0)
        self.maze = maze
        self.tile_size_px = 600 / maze.size
        self.shape("square")
        self.shapesize((28 / (maze.size + 1)), (28 / (maze.size + 1)), 0.5)
        self.penup()
        self.speed(0)
        self.wall_color = "#424242"
        self.path_color = "#D32F2F"
        self.light_green = '#DCE775'
        self.dark_green = '#43A047'
        self.num_of_setup_stamps = 0

    # setting up the maze
    def maze_setup(self):
        for y in range(0, self.maze.size):
            for x in range(0, self.maze.size):
                # check if value is a wall (-1)
                if self.maze.getCost(x, y) == -1:
                    # paint walls
                    self.paint_tile(x, y, self.wall_color, False)
                else:
                    self.paint_number(x, y)
        self.color("blue")
        self.goto(self.calculate_node(self.maze.startNode.x, self.maze.startNode.y, False))
        self.stamp()
        self.color("red")
        self.goto(self.calculate_node(self.maze.goalNode.x, self.maze.goalNode.y, False))
        self.stamp()
        self.num_of_setup_stamps = len(self.stampItems)

    # calculate node location in px
    def calculate_node(self, x, y, is_number):
        screen_x = -305 + (x * self.tile_size_px) + (self.tile_size_px / 2)
        screen_y = 305 - (y * self.tile_size_px) - (self.tile_size_px / 2)
        if is_number is True:
            screen_y -= (self.tile_size_px / 2)
        return screen_x, screen_y

    # paint the tile with color
    def paint_tile(self, x, y, color, update):
        if (self.maze.goalNode.x == x and self.maze.goalNode.y == y) or (
                self.maze.startNode.x == x and self.maze.startNode.y == y):
            return
        self.color(color)
        self.goto(self.calculate_node(x, y, False))
        self.stamp()
        # update window view
        if update is True:
            wn = turtle.Screen()
            wn.update()
        # paint number over scanned tiles. slows down. need to put it before if update is True
        # if color != self.wall_color:
        #     # self.paint_number(x, y)
        #     self.color('')

    # paint value number over tile
    def paint_number(self, x, y):
        font_size = 700 / (self.maze.size * 2)
        self.color(self.wall_color)
        self.goto(self.calculate_node(x, y, True))
        style = ('Arial', int(font_size))
        self.write(self.maze.getCost(x, y), font=style, align='center')

    # paint optimal path. bi_node used for bi_star algorithm
    def paint_path(self, node, bi_node = None):
        path = []
        while node.key != self.maze.startNode.key:
            path.append(node)
            node = node.fatherNode
        # reverse the list for ordered painting
        # path.reverse()
        # only if using biastar algorithm
        if bi_node != None:
            while bi_node.key != self.maze.goalNode.key:
                path.append(bi_node)
                bi_node = bi_node.fatherNode
        for node in path:
            self.paint_tile(node.x, node.y, self.path_color, True)
        # easteregg
        # self.goto(0,0)
        # self.color("black")
        # style = ('Arial', 70)
        # self.write("בומבה על הראש", font=style, align='center')
        # turtle.done()