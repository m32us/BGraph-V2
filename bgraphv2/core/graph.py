from vertex import Vertex

class Graph:
    def __init__(self):
        # List of vertices in the graph
        self.vertList = {}

        # Number of vertices in the graph
        self.numVertices = 0

    def addVertex(self, key):
        """Add vertex to graph

        Args:
            key (_type_): _description_

        Returns:
            _type_: _description_
        """
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, n):
        """Get a vertex from the graph.

        Args:
            n (_type_): _description_

        Returns:
            _type_: _description_
        """
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self, n):
        """Check whether vertex exists in the graph.

        Args:
            n (_type_): _description_

        Returns:
            _type_: _description_
        """
        return n in self.vertList

    def addEdge(self, f, t, weight=0):
        """Add edge to the graph.

        Args:
            f (_type_): indexing of the start vertex.
            t (_type_): indexing of the end vertex.
            weight (int, optional): _description_. Defaults to 0.
        """
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], weight)

    def getVertices(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.vertList.keys()

    def __iter__(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return iter(self.vertList.values())
