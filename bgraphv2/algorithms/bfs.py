from .whateverfirstsearch import WhateverFirstSearch

class BFS(WhateverFirstSearch):
    def __init__(self, start, G) -> None:
        super().__init__(start, G)

    def search(self):
        queue = []     # Initialize a queue
        visited = []   # List for visited nodes.

        queue.append(self.start)
        visited.append(self.start)
        current_node_id = self.start

        while len(queue) > 0:

            current_node_id = queue.pop(0)
            print(current_node_id)

            for neighbor in self.G.getVertex(str(current_node_id)).getConnections():

                id_node_neighbor = neighbor.id

                if id_node_neighbor not in visited:
                    queue.append(id_node_neighbor)
                    visited.append(id_node_neighbor)

