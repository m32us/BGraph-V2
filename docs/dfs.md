# Thuật toán tìm kiếm theo chiều sâu

Khi cấu trúc bag được cài đặt bằng cấu trúc ngăn xếp (stack), ta có một cách duyệt gọi là thuật toán Depth First Search. Cấu trúc hàng đợi được cài đặt với các phương thức push và pop trong độ phức tạp $O(1)$, do đó độ phức tạp thuật toán là $O(m+n)$

## Cài đặt

```py
class DFS(WhateverFirstSearch):
    def __init__(self, start, G):
        super().__init__(start, G)

    def search(self):
        stack = []
        visited = []
        stack.append(self.start)
        current_node_id = self.start
        while len(stack) > 0:
            current_node_id = stack.pop()
            print(current_node_id)
            for neighbor in self.G.getVertex(str(current_node_id)).getConnections():
                id_node_neighbor = neighbor.getId()
                # print(id_node_neighbor)
                if id_node_neighbor not in visited:
                    stack.append(id_node_neighbor)
                    visited.append(id_node_neighbor)
```

## Ví dụ chạy

1/ Với dữ liệu nhập tay

Khởi tạo dữ liệu
```py
graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}
```

Khởi tạo đồ thị
```py
g = Graph()
g = g.build_graph_from_edge_list(graph)
for v in g:
    for w in v.getConnections():
        print("( %s , %s )" % (v.getId(), w.getId()))
#print(g.getVertex(str(5)).getConnections())

print("Following is the Depth-First Search")
dfs = DFS(5, g).search()

# Kết quả: 5 7 8 3 4 2
```

2/ Với dữ liệu nhập từ tập tin
```py
# File: graph.txt
# 5 3 7
# 3 2 4
# 7 8
# 2
# 4 8
# 8
print("Test load graph from file")
g = Graph()
g = g.build_graph_from_file("graph.txt")
for v in g:
    for w in v.getConnections():
        print("( %s , %s )" % (v.getId(), w.getId()))
print("Following is the Depth-First Search")
dfs = DFS(5, g).search()

# Kết quả: 5 7 8 3 4 2
```