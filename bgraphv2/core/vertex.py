from typing import Union


class Vertex:
    """Lớp đỉnh (Vertex class)
    """

    def __init__(self, key: Union[int, str]):
        """Phương thức khởi tạo.
        Chỉ thiết lập `id`, gồm một `string` là `key` được truyền cho và một từ điển `connectTo`

        Tham số:
            key (Union[int, str]): Khóa hay nhãn của đỉnh được truyền cho.
        """

        # Khóa hay nhãn
        self.id = key

        # Từ điển connectTo
        self.connectedTo = {}

    def addNeighbor(self, nbr: Union[int, str], weight: int = 0):
        """Phương thức thêm một cung vào đồ thị.

        Tham số:
            nbr (Union[int, str]): Khóa hay nhãn của lân cận đầu vào.
            weight (int, optional): Trọng số của cung sau khi khởi tạo. Mặc định là 0.
        """
        self.connectedTo[nbr] = weight

    def __str__(self) -> str:
        """Phương thức chuỗi thể hiện cho lớp đỉnh.

        Trả về:
            str: Một chuỗi (string) thể hiện thông tin cho lớp đỉnh.
        """
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self) -> dict:
        """Phương thức trả về tất cả các đỉnh trong danh sách kề, biểu diễn bởi biến connectedTo.

        Trả về:
            dict: Từ điển connectedTo chứa dữ liệu tất cả các đỉnh trong danh sách kề.
        """
        return self.connectedTo.keys()

    def getId(self):
        """Phương thức lấy ra khóa hay nhãn thể hiện của đối tượng đỉnh.

        Trả về:
            Union[int, str]: khóa hay nhãn thể hiện của đối tượng đỉnh.
        """
        return self.id

    def getWeight(self, nbr) -> int:
        """Phương thức lấy trọng số của cạnh được truyền theo tham số.

        Tham số:
            nbr (_type_): khóa hay nhãn thể hiện của đỉnh lân cận với đối tượng đỉnh.

        Trả về:
            int: Trọng số của cạnh được truyền theo tham số.
        """
        return self.connectedTo[nbr]
