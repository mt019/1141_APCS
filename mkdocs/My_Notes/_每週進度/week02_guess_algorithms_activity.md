# 猜猜演算法挑戰

<!-- - 先觀察下面的 Python 程式碼，暫時忽略函式名稱。 -->
- 寫下你認為每個函式實作的是哪一個經典演算法。
<!-- - 可以把程式碼貼到自己的環境中播放資料、驗證猜想。 -->

```python
from typing import List, Tuple


def algo_1(nums: List[int]) -> List[int]:
    arr = nums[:]
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


def algo_2(nums: List[int]) -> List[int]:
    arr = nums[:]
    start, end = 0, len(arr) - 1
    while start < end:
        swapped = False
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        end -= 1
        for i in range(end, start, -1):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                swapped = True
        start += 1
        if not swapped:
            break
    return arr


def algo_3(nums: List[int]) -> List[int]:
    arr = nums[:]

    def sift_down(root: int, limit: int) -> None:
        while True:
            child = 2 * root + 1
            if child >= limit:
                break
            if child + 1 < limit and arr[child] < arr[child + 1]:
                child += 1
            if arr[root] >= arr[child]:
                break
            arr[root], arr[child] = arr[child], arr[root]
            root = child

    length = len(arr)
    for start in range(length // 2 - 1, -1, -1):
        sift_down(start, length)
    for end in range(length - 1, 0, -1):
        arr[0], arr[end] = arr[end], arr[0]
        sift_down(0, end)
    return arr


def algo_4(nums: List[int]) -> List[int]:
    arr = nums[:]
    for i in range(1, len(arr)):
        current = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > current:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current
    return arr


def algo_5(matrix: List[List[int]], start: int = 0) -> List[Tuple[int, int, int]]:
    n = len(matrix)
    visited = [False] * n
    weight = [float("inf")] * n
    parent = [-1] * n
    weight[start] = 0

    for _ in range(n):
        current = min((w, idx) for idx, w in enumerate(weight) if not visited[idx])[1]
        visited[current] = True
        for neighbor, edge in enumerate(matrix[current]):
            if edge and not visited[neighbor] and edge < weight[neighbor]:
                weight[neighbor] = edge
                parent[neighbor] = current

    tree: List[Tuple[int, int, int]] = []
    for vertex in range(n):
        if parent[vertex] != -1:
            tree.append((parent[vertex], vertex, matrix[parent[vertex]][vertex]))
    return tree


if __name__ == "__main__":
    sample = [29, 10, 14, 37, 14]
    print("algo_1:", algo_1(sample))
    print("algo_2:", algo_2(sample))
    print("algo_3:", algo_3(sample))
    print("algo_4:", algo_4(sample))

    graph = [
        [0, 2, 0, 6, 0],
        [2, 0, 3, 8, 5],
        [0, 3, 0, 0, 7],
        [6, 8, 0, 0, 9],
        [0, 5, 7, 9, 0],
    ]
    print("algo_5:", algo_5(graph))
```

把你覺得的答案寫在旁邊！

<!--
解答與重點：
- algo_1 = Bubble Sort：兩兩比較、把最大值一路往右推；最佳情況 O(n)（資料已經排序、不需要交換），平均/最差 O(n^2)（資料亂序或反序，每輪都要交換）。
- algo_2 = Cocktail Sort：泡泡排序的雙向版，左右來回掃描以加速收斂；最佳情況 O(n)（已排序時第一趟就不交換），平均/最差 O(n^2)（資料亂序或反序仍需完整雙向掃描）。
- algo_3 = Heap Sort：先建最大堆再逐一把堆頂換到尾端，建堆 O(n)，排序階段 O(n log n)；堆排序不論最佳、平均或最差情況都維持 O(n log n)。
- algo_4 = Insertion Sort：將左側視為已排序區，逐個插入新元素；最佳情況 O(n)（資料幾乎或完全排序，只做比較），平均/最差 O(n^2)（資料亂序或反序，插入時需大量搬移）。
- algo_5 = Prim's Algorithm：以鄰接矩陣實作的貪心最小生成樹演算法，每輪選取最小邊擴展樹；這個實作不分情況都是 O(n^2)，因為每輪都要掃描整列權重。
-->
