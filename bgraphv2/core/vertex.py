from typing import Union

class Vertex:
    def __init__(self, key: Union[int, str]):
        """Initialization method for Vertex class.

        Args:
            key (_type_): Input key for vertex.
        """
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self, nbr: Union[int, str], weight: int = 0):
        self.connectedTo[nbr] = weight

    def __str__(self) -> str:
        """Representation string of vertex.

        Returns:
            str: string that represents format for vertex.
        """
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self) -> dict:
        """Get the list of neighbor of the vertex.

        Returns:
            dict: connectedTo dictionary that contains neighbor of the vertex.
        """
        return self.connectedTo.keys()

    def getId(self):
        """Get the identity for the vertex.

        Returns:
            Union[int, str]: identity of the vertex.
        """
        return self.id

    def getWeight(self, nbr):
        """Get weight

        Args:
            nbr (_type_): _description_

        Returns:
            int: _description_
        """
        return self.connectedTo[nbr]
