import turtle
import tkinter as tk


class Pen(turtle.RawPen):
    __instance = None
    maze = None
    tile_size_px = 0

    def __init__(self, mazeScreen):
        """ Virtually private constructor. """
        if Pen.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Pen.__instance = self
        turtle.RawPen.__init__(self, mazeScreen.cv)
        self.color('')
        self.mazeScreen = mazeScreen
        self.mazeScreen.bgcolor("white")
        self.speed(0)
        self._tracer(False)
        # self.mazeScreen.tracer(0,0)
        self.shape("square")
        self.penup()
        self.wall_color = "#424242"
        self.path_color = "#D32F2F"
        self.light_green = '#DCE775'
        self.dark_green = '#43A047'
        self.num_of_setup_stamps = 0


    @staticmethod
    def getInstance(mazeScreen = None):
        """ Static access method. """
        if Pen.__instance == None:
            Pen(mazeScreen)
        return Pen.__instance

    # setting up the maze
    def maze_setup(self, maze):
        self.clear()
        print(len(self.stampItems))
        self.maze = maze
        self.tile_size_px = 600 / maze.size
        self.shapesize((35 / (1.3 * maze.size + 1)), (35 / (1.3 * maze.size + 1)), 0)
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
        self.goto(self.calculate_node(x, y, False))
        self.color(color)
        self.stamp()
        # update window view
        if update is True:
            # wn = turtle.Screen()
            self.mazeScreen.update()
        # paint number over scanned tiles. slows down. need to put it before if update is True
        # if color != self.wall_color:
        #     # self.paint_number(x, y)
        #     self.color('')

    # paint value number over tile
    def paint_number(self, x, y):
        font_size = 700 / (self.maze.size * 2)
        self.goto(self.calculate_node(x, y, True))
        self.color(self.wall_color)
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
        # turtle.exitonclick()
        # easteregg
        # self.goto(0,0)
        # self.color("black")
        # style = ('Arial', 70)
        # self.write("בומבה על הראש", font=style, align='center')
        # turtle.done()