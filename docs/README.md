# CÀI ĐẶT THUẬT TOÁN TÌM KIẾM TRÊN ĐỒ THỊ

Môn học: Phương pháp toán cho TNTT

Thành viên:
- Nguyễn Thị Thu Hằng - 22C15027
- Lê Nhựt Nam - 22C11067

## Nội dung đồ án

Thiết kế xây dựng thuật toán tìm kiếm trên đồ thị BFS, DFS

## Các lớp trong thư viện

Thư viện cài đặt kiểu dữ liệu trừu tượng cho đồ thị bằng cách sử dụng danh sách kề. Như vậy, kiểu dữ liệu trừu tượng Graph sẽ có hai lớp
- Graph – chứa danh sách các đỉnh, và
- Vertex - cho mỗi đỉnh trong đồ thị.

### Graph – chứa danh sách các đỉnh

```py
class Graph:
    def __init__(self):
        """Phương thức khởi tạo đồ thị rỗng, mới."""
        # Danh sách các đỉnh
        self.vertList = {}
        # Số lượng đỉnh trong đồ thị
        self.numVertices = 0
```

Một số phương thức của lớp Graph

1/ Phương thức thêm đỉnh addVertex.

```py
def addVertex(self, key: Union[int, str]) -> Vertex:
    """Phương thức thêm đỉnh có `key` vào đồ thị

    Tham số:
        key (Union[int, str]): key của đỉnh cần thêm vào đồ thị.

    Trả về:
        Vertex: đối tượng thuộc lớp Vertex thể hiện đỉnh vừa thêm vào đồ thị.
    """
    self.numVertices = self.numVertices + 1
    newVertex = Vertex(key)
    self.vertList[key] = newVertex
    return newVertex
```

2/ Phương thức lấy một đinh getVertex.

```py
def getVertex(self, n: Union[int, str]) -> Union[Vertex, None]:
    """Phương thức lấy một đỉnh có khóa hay nhãn là `n` ra từ danh sách các đỉnh của đồ thị.

    Tham số:
        n (Union[int, str]): key của đỉnh cần lấy ra từ đồ thị.

    Trả về:
        Union[Vertex, None]: Trả về đối tượng thuộc lớp Vertex thể hiện đỉnh cần lấy ra từ đồ thị.
        Nếu đỉnh không tồn tại, trả về None.
    """
    if n in self.vertList:
        return self.vertList[n]
    else:
        return None
```

3/ Phương thức thêm một cạnh addEdge.

```py
def addEdge(self, f: Union[int, str], t: Union[int, str], weight: int = 0):
        """Phương thức thêm cạnh, có hướng vào đồ thị nối hai đỉnh `f` và `t`.
        Tham số:
            f (Union[int, str]): Khóa của đỉnh bắt đầu.
            t (Union[int, str]): Khóa của đỉnh kết thúc.
            weight (int, optional): Trọng số của cạnh nối hai đỉnh. Mặc định là 0.
        """
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], weight)
```

4/ Phương thức lấy tất cả các đỉnh getVertices.

```py
def getVertices(self) -> list:
        """Phương thức trả về danh sách tất cả các đỉnh trong đồ thị.

        Tham số:
            list: Danh sách tất ca các đỉnh trong đồ thi.
        """
        return self.vertList.keys()
```

5/ Phương thức iter duyệt qua các đối tượng đỉnh trong đồ thị.

```py
def __iter__(self):
        """Phương thức duyệt các đối tượng đỉnh trong đồ thị.

        Trả về:
            SupportsNextT@iter: Bộ duyệt duyệt các đối tượng đỉnh trong đồ thị.
        """
        return iter(self.vertList.values())
```

6/ Phương thức xây dựng đồ thị bằng cách nhập tay

```py
@classmethod
def build_graph_from_file(cls, filename, delimiter = " "):
    """ Phương thức xây dựng đồ thị từ danh sách kề

    Tham số:
        filename: file chưa danh sách kề

    Trả về:
        Đồ thị
    """
    g = cls()
    edge_list = dict()
    for line in open(filename,'U'):
        L = line.strip().split(delimiter)
        if (L[0] not in g.getVertices()):
                g.addVertex(L[0])
        for i in range(1, len(L)):
            if (L[i] not in g.getVertices()):
                g.addVertex(L[i])
            g.addEdge(L[0], L[i])
    return g
```

7/ Phương thức xây dựng đồ thị từ tập tin

```py
@classmethod
    def build_graph_from_edge_list(cls, d):
        """ Phương thức xây dựng đồ thị từ danh sách kề

        Tham số:
            d: danh sách kề

        Trả về:
            Đồ thị
        """
        g = cls()
        for v1, v2_list in d.items():
            if (v1 not in g.getVertices()):
                    g.addVertex(v1)
            for v2 in v2_list:
                if (v2 not in g.getVertices()):
                    g.addVertex(v2)
                g.addEdge(v1, v2)

        return g
```

## Vertex - cho mỗi đỉnh trong đồ thị.

```py
class Vertex:
    def __init__(self, key: Union[int, str]):
        """Phương thức khởi tạo.
        Chỉ thiết lập id, gồm một string là key được truyền cho và một từ điển connectTo
        Tham số:
            key (Union[int, str]): Khóa hay nhãn của đỉnh được truyền cho.
        """
        # Khóa hay nhãn
        self.id = key
        # Từ điển connectTo
        self.connectedTo = {}
```

1/ Phương thức addNeighbor để thêm một cung vào đồ thị.

```py
def addNeighbor(self, nbr: Union[int, str], weight: int = 0):
        """Phương thức thêm một cung vào đồ thị.

        Tham số:
            nbr (Union[int, str]): Khóa hay nhãn của lân cận đầu vào.
            weight (int, optional): Trọng số của cung sau khi khởi tạo. Mặc định là 0.
        """
        self.connectedTo[nbr] = weight
```

2/ Phương thức getConnections để lấy tất cả các đỉnh trong danh sách kề.

```py
def getConnections(self) -> dict:
        """Phương thức trả về tất cả các đỉnh trong danh sách kề, biểu diễn bởi biến connectedTo.

        Trả về:
            dict: Từ điển connectedTo chứa dữ liệu tất cả các đỉnh trong danh sách kề.
        """
        return self.connectedTo.keys()
```

3/ Phương thức getWeight trả về trọng số của cạnh được truyền theo tham số.

```py
def getWeight(self, nbr) -> int:
        """Phương thức lấy trọng số của cạnh được truyền theo tham số.

        Tham số:
            nbr (_type_): khóa hay nhãn thể hiện của đỉnh lân cận với đối tượng đỉnh.

        Trả về:
            int: Trọng số của cạnh được truyền theo tham số.
        """
        return self.connectedTo[nbr]
```

## Tài liệu tham khảo

[1] ĐỒ THỊ VÀ THUẬT GIẢI TRÊN ĐỒ THỊ, Nguyễn Đình Thúc