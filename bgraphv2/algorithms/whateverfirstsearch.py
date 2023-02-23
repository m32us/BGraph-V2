# whatever first search is a general algorithm to represent the three main graph search algorithms
# Breadth First Search, Depth First Search, Dijekstra Algorithm. By changing the bag data structure the algorithm changes between the three.
# 1. if the bag is a queue --> the algorithm becomes BFS
# 2. if the bag is a stack --> the algorithm becomes DFS
# 3. if the bag is a priority queue --> the algorithm becomes Dijekstra

# WhateverFirstSearch(s):
#     put s into the bag
#         while the bag is not empty
#             take v from the bag
#             if v is unmarked
#                 mark v
#                 for each edge vw
#                     put w into the bag

from abc import ABC, abstractclassmethod


class WhateverFirstSearch(ABC):
    def __init__(self, start, G) -> None:
        self.start = start
        self.G = G

    @abstractclassmethod
    def search(self):
        raise NotImplementedError

