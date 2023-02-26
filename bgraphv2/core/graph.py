from .vertex import Vertex

from typing import Union


class Graph:
    """Lớp đồ thị (Graph class)
    """

    def __init__(self):
        """Phương thức khởi tạo đồ thị rỗng, mới.
        """
        # Danh sách các đỉnh
        self.vertList = {}

        # Số lượng đỉnh trong đồ thị
        self.numVertices = 0

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

    def __contains__(self, n) -> bool:
        """Phương thức kiểm tra liệu một đỉnh có nằm trong đồ thị hay không.
        Tức là kiểm tra đỉnh đầu vào có nằm trong danh sách các đỉnh của đồ thị hay không?

        Tham số:
            n (Union[int, str]): key của đỉnh cần lấy ra từ đồ thị.

        Trả về:
            bool: Nếu đỉnh có tồn tại trong danh sách các đỉnh, trả về True. Ngược lại, False.
        """
        return n in self.vertList

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

    def getVertices(self) -> list:
        """Phương thức trả về danh sách tất cả các đỉnh trong đồ thị.

        Tham số:
            list: Danh sách tất ca các đỉnh trong đồ thi.
        """
        return self.vertList.keys()

    def __iter__(self):
        """Phương thức duyệt các đối tượng đỉnh trong đồ thị.

        Trả về:
            _type_: Bộ duyệt duyệt các đối tượng đỉnh trong đồ thị.
        """
        return iter(self.vertList.values())
    
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

