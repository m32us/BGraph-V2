from .whateverfirstsearch import WhateverFirstSearch

class DFS(WhateverFirstSearch):
    def __init__(self, start, G) -> None:
        super().__init__(start, G)

    def search(self):
        stack = []
        visited = []
        stack.append(self.start)

        current_node_id = self.start

        while len(stack) > 0:

            current_node_id = stack.pop()
            print(current_node_id)

            # for node in self.G.getVertex(current_node_id).getConnections():
            #     print(node.id)

            for neighbor in self.G.getVertex(current_node_id).getConnections():

                id_node_neighbor = neighbor.id

                # print(id_node_neighbor)
                if id_node_neighbor not in visited:
                    print("Visiting neighbor ", id_node_neighbor)
                    stack.append(id_node_neighbor)
                    visited.append(id_node_neighbor)

