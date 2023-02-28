# Thiết kế lớp trừu tượng Whatever first search

## Tổng quan

Whatever first search là một thuật toán tổng quát để thể hiện ba loại thuật toán chính trong bài toán duyệt đồ thị. Thuật toán duyệt đồ thị tổng quát lưu trữ một tập hợp lực lượng các cạnh trong một cấu trúc dữ liệu tổng quát gọi là "bag". Một tính chất quan trọng của một "bag" là ta có thể đưa một phần tử vào trong đó và sau đó lấy phần tử bên trong ra.

```
\begin{algorithm}
\caption{Thuật toán Whatever first search}
\label{pseudoPSO}
\begin{algorithmic}[1]
\State Khởi tạo các biến đánh dấu
\State Đặt phần tử $s$ vào một empty bag.
\While{bag không rỗng}
    \State Lấy một đỉnh $v$ từ trong bag.
    \If{$v$ chưa được đánh dấu}
        \State Đánh dấu $v$
        \For{each edge $vw$}
            \State Đặt $w$ vào bag
        \EndFor
    \EndIf
\EndWhile
\end{algorithmic}
\end{algorithm}
```

Bằng cách thay đổi cấu trúc dữ liệu bag, ta có thể cài đặt được các thuật toán sau:
- Nếu bag là cấu trúc dữ liệu ngăn xếp (stack), ta cài đặt được thuật toán Depth First Search.
- Nếu bag là cấu trúc dữ liệu hàng đợi (queue), ta cài đặt được thuật toán Breadth First Search.
- Nếu bag là cấu trúc dữ liệu hàm đợi ưu tiên (priority queue), ta cài đặt được thuật toán Djisktra.

## Cài đặt

Cài đặt lớp WhateverFirstSearch là một lớp trừu tượng

```py
class WhateverFirstSearch(ABC):
    def __init__(self, start, G):
        self.start = start
        self.G = G
    @abstractclassmethod
    def search(self):
        raise NotImplementedError
```

## Phân tích

Nếu gọi $m = |V|$, $n = |E|$, và $t$ lần lượt là số lượng đỉnh, số lượng cạnh, và thời gian thêm/ xóa phần tử trong bag.
- Việc khởi tạo các biến đánh dấu tốn chi phí $O(m)$ do có bấy nhiêu đỉnh thì tạo mảng rộng bấy nhiêu.
- Vòng for ở trong cùng thực thi chính xác một lần cho mỗi những đỉnh đã được đánh dấu, do đó nó sẽ chạy nhiều nhất $m$ lần, $O(m)$
- Mỗi cạnh $uv$ được đặt vào bag chính xác hai lần: một lần với cạnh $u, v$, một lần với $v, u$. Do đó, lệnh put trong vòng for chạy nhiều nhất $2n$ lần.
- Việc lấy một phần tử ra khỏi bag tốn nhiều nhất $2n + 1$ lần (+1 là pha lấy cuối cùng để biết nó rỗng)

Tùy vào cấu trúc lưu trữ của đồ thị mà thuật toán có độ phức tạp khác nhau:
- Cấu trúc danh sách kề: $O(m +tn)$
- Cấu trúc ma trận kề: $O(m^2 +tn)$