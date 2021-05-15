
from random import randint
from collections import deque


class Graph:
    adj: dict
    directed: bool
    weighted: bool
    filePath: str
    inputType: str
    algoValues: dict


    def __init__(self):
        self.adj = {}
        self.directed = False
        self.weighted = False
        self.filePath = None
        self.inputType ="Adjacency List"
        self.algoValues = {}

    def getFields(self):
        return self.adj, self.directed, self.weighted, self.algoValues


    def print(self):
        for key, value in self.adj.items():
            print(f"[{key}] -> ", end="")
            print(f"{value}")


    def addVertices(self, *verts):
        for v in verts:
            if v not in self.adj.keys():
                self.adj[v] = {}


    def addEdges(self, start, ends):
        self.addVertices(*range(1, max(start, *ends)+1))
        self.adj[start] = {**self.adj[start], **ends}
        if not self.directed:
            for end in ends.keys():
                if end in self.adj.keys():
                    self.adj[end] = {**self.adj[end], **{start: ends[end]}}
                else:
                    self.adj[end] = {start: ends[end]}


    def convert_matrix_to_list(self, matrix):
        G = {}
        for a in range(len(matrix)):
            if matrix[a].count(0) != len(matrix):
                for b in range(len(matrix)):
                    if matrix[a][b]:
                        if a + 1 not in G:
                            G[a + 1] = {b + 1: matrix[a][b]}
                        else:
                            G[a + 1][b + 1] = matrix[a][b]
            else:
                G[a + 1] = set()
        return G


    def readGraph(self):
        try:
            with open(self.filePath, "r") as fin:
                if self.inputType == "Adjacency List":
                    self.adj = {}
                    while True:
                        temp = [int(i) for i in fin.readline().split()]
                        if temp == []:
                            break
                        if self.weighted:
                            for i in range(0, len(temp), 3):
                                if temp[i] <= 0 or temp[i+1] <= 0:
                                    print("Uncorrect vertice")
                                    self._adj = {}
                                    return "Uncorrect vertice"
                                elif temp[i+2] <= 0:
                                    print("Uncorrect weights")
                                    self._adj = {}
                                    return "Uncorrect weights"
                                self.addEdges(temp[i], {temp[i+1]:temp[i+2]})
                        else:
                            for i in range(0, len(temp), 2):
                                if temp[i] <= 0 or temp[i+1] <= 0:
                                    print("Uncorrect vertice")
                                    self._adj = {}
                                    return "Uncorrect vertice"
                                self.addEdges(temp[i], {temp[i+1]:1})
                    self.addVertices(max(self.adj.keys()))
                elif self.inputType == "Adjacency Matrix":
                    matrix = []
                    while True:
                        if self.weighted:
                            temp = [int(i) for i in fin.readline().split()]
                        else:
                            temp = [1 if int(i) else 0 for i in fin.readline().split()]
                        if temp == []:
                            break
                        matrix.append(temp)
                    self.adj = self.convert_matrix_to_list(matrix)
        except (FileNotFoundError, TypeError):
            raise Exception("Path Error")
        except (IndexError, ValueError):
            self.adj = {}
            print("File not match input type")
            return "File not match input type"

    def minPathFind(self, start, goal):
        graph = self.adj
        if start not in graph or goal not in graph:
            print("Vertices not in graph")
            return "Vertices not in graph"
        queue = deque()
        visited = {start: 0}
        tmpPath = {}
        queue.append(start)
        while queue:
            v = queue.popleft()
            for u in graph[v]:
                if u not in visited or visited[v] + graph[v][u] < visited[u]:
                    visited[u] = visited[v] + graph[v][u]
                    queue.append(u)
                    tmpPath[u] = v
        v = goal
        path = deque()
        path.append(v)
        if v in tmpPath:
            while v != start:
                v = tmpPath[v]
                path.appendleft(v)
            return visited[goal], list(path)
        elif start == goal:
            return 0, [start]
        else:
            print("Minimal path error")
            return "Minimal path error"


    def coloring(self):
        graph = self.adj
        tmp = {x: 0 for x in graph}
        for x in graph:
            if graph[x]:
                tmp[x] = len(graph[x].keys())
            else:
                tmp[x] = 0
        vertList = list(tmp.items())
        vertList.sort(key=lambda i: i[1])
        colored = {x: None for x in graph}
        flag = True
        cl = 0
        smList = []
        for v in vertList:
            v = v[0]
            if colored[v] is None:
                colored[v] = cl
                smList.append(v)
                for j in vertList:
                    j = j[0]
                    if colored[j] is None:
                        for sm in smList:
                            if sm in graph[j] or j in graph[sm] and flag:
                                flag = False
                        if flag:
                            colored[j] = cl
                            smList.append(j)
                        flag = True
                smList = []
                cl += 1
        res = {}
        existColors = {}
        for i in colored:
            if colored[i] in existColors.keys():
                res[i] = existColors[colored[i]]
            else:
                existColors[colored[i]] = (randint(0, 255), randint(0, 255),randint(0, 255))
                res[i] = existColors[colored[i]]
        return cl, res


    def initGraphFile(self, filepath):
        self.filePath = filepath
        