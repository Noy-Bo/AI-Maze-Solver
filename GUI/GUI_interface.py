from tkinter import Tk, ttk, filedialog, Label, Entry, Button, Checkbutton, BooleanVar, Canvas, W, E, StringVar
from turtle import TurtleScreen

import Utilities
from Algorithms.Astar import Astar
from Algorithms.Astar_visualized import AstarVisual
from Algorithms.BiAstar import BiAstar
from Algorithms.BiAstar_visualized import BiAstarVisual
from Algorithms.IDAstar import IDAstar
from Algorithms.IDAstar_visualized import IDAstarVisual
from Algorithms.IDS import IDS
from Algorithms.IDS_visualized import IDSVisual
from Algorithms.UCS import UCS
from Algorithms.UCS_visualized import UCSVisual
from GUI.GUI import Pen


class GuiInterface(object):
    def __init__(self):
        self.pen = None
        self.title = "Maze AI Solver"
        self.algorithms = ["Astar", "biAstar", "IDAstar", "IDS", "UCS"]
        self.path = "ENTER PATH"
        self.mazeScreen = None
        self.pen = None
        self.root = None
        self.combo = None
        self.runtimeEntry = None
        self.canvas = None
        self.visualCheckBox = None
        self.textBox = None

    def setupInterface(self):
        # initialize windows
        self.root = Tk()
        self.root.title(self.title)
        self.root.configure(bd=10)

        # add label and choises of algorithms
        Label(self.root, text="Algorithm:").grid(row=0, column=0, sticky=W)
        self.combo = ttk.Combobox(self.root, width=10, values=self.algorithms)
        self.combo.current(4)
        self.combo.grid(row=0, column=1, sticky=W)

        # add label and time limit entry
        Label(self.root, text="Time Limit").grid(row=1, column=0, sticky=W)
        self.runtimeEntry = Entry(self.root, width=13)
        self.runtimeEntry.grid(row=1, column=1, sticky=W)
        self.runtimeEntry.insert(0, "100")

        # add choose file button
        Button(self.root, text="Choose file", width=10, command=lambda: self.browseFile(), cursor="hand2",
                               activebackground="Lavender").grid(row=0, column=2, sticky=W)

        # add check button
        self.visualCheckBox = BooleanVar()
        self.visualCheckBox.set(True)
        Checkbutton(self.root, text="visualize", variable=self.visualCheckBox, cursor="hand2").grid(row=1, column=2, sticky=W)

        # add run button
        self.textBox = StringVar()
        self.textBox.set("Welcome")
        Label(self.root, textvariable=self.textBox).grid(row=2, column=0, sticky=W + E, columnspan=4)
        button_run = Button(self.root, text="Run", width=5, height=3, command=lambda: self.runButton(), cursor="hand2",
                            activebackground="Lavender").grid(row=0, column=3, sticky=W + E, columnspan=1, rowspan=2)

        # create the maze window
        self.canvas = Canvas(self.root, width=630, height=630)
        self.canvas.grid(column=0, row=3, columnspan=4)

        # add the maze window inside main window
        self.mazeScreen = TurtleScreen(self.canvas)
        self.pen = Pen.getInstance(self.mazeScreen)
        self.root.mainloop()

    def runButton(self):
        # self.mazeScreen.clear()
        maxRunTime = int(self.runtimeEntry.get())
        algorithmName, startNode, goalNode, mazeSize, maze = Utilities.readInstance(self.path)
        algorithm, isHeuristic = self.getAlgorithmFromString(self.combo.get(), self.visualCheckBox.get())
        self.textBox.set("solving with " + self.combo.get() + ", please wait...")
        self.mazeScreen.update()
        if isHeuristic is True:
            algorithm(maze, maxRunTime, "minimumMoves")
            #algorithm(maze, maxRunTime, "movesCount")
        else:
            algorithm(maze, maxRunTime)
        self.textBox.set("Finished running. See OutputResult.txt for results")
        self.mazeScreen.update()

    def browseFile(self):
        file = filedialog.askopenfile(parent=self.root, mode='rb', title='Choose a file')
        algorithmName, startNode, goalNode, mazeSize, maze = Utilities.readInstance(file.name)
        for item in self.algorithms:
            if algorithmName.lower() == item.lower():
                self.combo.current(self.algorithms.index(item))
        self.path = file.name


    def getAlgorithmFromString(self, algorithmString, isVisual):

        if algorithmString.lower() == "biastar":
            if isVisual is True:
                return BiAstarVisual, True
            else:
                return BiAstar, True

        elif algorithmString.lower() == "astar":
            if isVisual is True:
                return AstarVisual, True
            else:
                return Astar, True

        elif algorithmString.lower() == "idastar":
            if isVisual is True:
                return IDAstarVisual, True
            else:
                return IDAstar, True

        elif algorithmString.lower() == "ids":
            if isVisual is True:
                return IDSVisual, False
            else:
                return IDS, False

        elif algorithmString.lower() == "ucs":
            if isVisual is True:
                return UCSVisual, False
            else:
                return UCS, False

        else:
            return "ERROR"