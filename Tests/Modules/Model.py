
from .Graph import Graph
from .Render import drawColoring, drawMinPath, drawDefault


class GraphModel():
    def __init__(self):
        self.graph = Graph()
        self.functions = {
            drawDefault.__name__: drawDefault,
            drawMinPath.__name__: drawMinPath,
            drawColoring.__name__: drawColoring
        }

