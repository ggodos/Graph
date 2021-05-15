
from functools import partial


class GraphCtrl:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self._connectButtons()


    def _connectButtons(self):
        self.view.buttons["Input File"].clicked.connect(partial(self.chooseInputFile))
        self.view.buttons["⭯"].clicked.connect(partial(self.updateGraph))
        self.view.buttons["Coloring"].clicked.connect(partial(self.coloringGraph))
        self.view.buttons["Min Path"].clicked.connect(partial(self.minPathGraph))


    def chooseInputFile(self):
        filepath = self.view.getPathFile()
        if filepath:
            self.model.graph.initGraphFile(filepath)
            self.updateGraph()


    def updateGraph(self):
        try:
            self.model.graph.readGraph()
        except Exception as ex:
            self.view.showError(ex)
            return

        adj, dir, w = self.model.graph.adj, self.model.graph.directed, self.model.graph.weighted

        self.view.figure.clf()
        self.model["drawDefault"](adj, dir, w)
        self.view.canvas.draw()


    def coloringGraph(self):
        q, colors = self.model.graph.coloring()

        adj, dir, w = self.model.graph.adj, self.model.graph.directed, self.model.graph.weighted

        self.view.figure.clf()
        self.model.functions["drawColoring"](adj, dir, w, colors)
        self.view.canvas.draw()


    def minPathGraph(self):
        start, goal = self.view.TextMinPathStart.text(), self.view.TextMinPathGoal.text()

        try:
            lenght, path = self.model.graph.minPathFind(start, goal)
        except Exception as ex:
            self.view.showError(ex)
            return

        adj, dir, w = self.model.graph.adj, self.model.graph.directed, self.model.graph.weighted

        self.view.figure.clf()
        self.model.functions["drawMinPath"](adj, dir, w, path)
        self.view.canvas.draw()

