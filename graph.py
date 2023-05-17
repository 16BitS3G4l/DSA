class Vertex:

    def __init__(self, value=0):
        # adjacent vertices 
        self.edges = []

        self.value = value

    def addEdge(self, vertex):
        self.edges.append(vertex)


class Graph:

    def __init__(self):
        self.vertices = []

    def addVertex(self,vertex):
        self.vertices.append(vertex)




