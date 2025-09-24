# 穩定排序 vs. 不穩定排序

在第一週的排序練習中，我們接觸了多個演算法。除了速度，另一個重要特性是「穩定性」。本筆記說明什麼是穩定排序、為什麼它重要，以及如何在 Python 驗證。

## 什麼是穩定？
- **穩定排序**：若兩個元素的鍵值相同，排序後它們的相對順序維持不變。
- **不穩定排序**：相同鍵值的元素可能交換位置。

### 小例子


- 原始資料：[(Aaron, 86), (Kevin, 92), (Chloe, 86)]

以成績排序：

- 穩定排序 → [(Aaron, 86), (Chloe, 86), (Kevin, 92)]
- 不穩定排序 → [(Chloe, 86), (Aaron, 86), (Kevin, 92)]


兩種結果都有正確的鍵值順序，但穩定排序保留了原始出現先後。

## 常見演算法穩定性

| 演算法 | 穩定？ | 時間複雜度 | 備註 |
| --- | --- | --- | --- |
| 氣泡排序 | ✅ | `O(n^2)` | 每次只交換相鄰元素 |
| 雞尾酒排序 | ✅ | `O(n^2)` | 同樣只交換相鄰元素 |
| 插入排序 | ✅ | `O(n^2)` | 插入時向右移動元素 |
| 合併排序 | ✅ | `O(n log n)` | 合併時可維持順序 |
| 堆排序 | ❌ | `O(n log n)` | 彈出最大／最小值會破壞原順序 |
| 快速排序 | ❌（原始版） | 平均 `O(n log n)` | Pivot 交換不保證順序 |
| Python `sorted` / `list.sort` | ✅ | `O(n log n)` | Timsort，語言層面保證 |

## 為什麼需要穩定排序？
- **多欄位排序**：先依科目排序，再依姓名排序；只要第二次排序穩定，就不會破壞第一次結果。
- **資料追蹤**：需要保留原始輸入順序（例如：同分同班排名）。
- **除錯與可讀性**：穩定排序更容易預測結果，避免誤判程式錯誤。

## 在 Python 觀察穩定性

```python
students = [
    {"name": "Aaron", "score": 86},
    {"name": "Kevin", "score": 92},
    {"name": "Chloe", "score": 86},
]

print(sorted(students, key=lambda x: x["score"]))
# → [{'name': 'Aaron', 'score': 86}, {'name': 'Chloe', 'score': 86}, {'name': 'Kevin', 'score': 92}]
```

Python 的 `sorted` 是穩定排序。如果想觀察不穩定版本，可以自己寫堆排序：

```python
import heapq

def unstable_heap_sort(items):
    heap = [(-item["score"], idx, item) for idx, item in enumerate(items)]
    heapq.heapify(heap)
    result = []
    while heap:
        _, _, item = heapq.heappop(heap)
        result.append(item)
    return result

unstable = unstable_heap_sort(students)
print(unstable)
```

如果你把 `idx` 從堆元素中移除，`Chloe` 可能會在結果中跑到 `Aaron` 前面。

## 如何讓不穩定排序變穩定？
- **增加索引作為次要鍵值**：如上例，`(-score, idx)` 可以保留原順序。
- **先整理資料再使用穩定排序**：例如先將資料編號，再用 `sorted` 對編號排序。

## 練習建議
1. 以 `list.sort` 搭配 `key` 實作「先班級、再成績」排序，觀察穩定性如何幫忙。
2. 改寫自己的堆排序，加入原始索引以確保穩定。
3. 查找 APCS 題目中是否有需要穩定排序的場景（提示：成績排名、車站排隊）。
