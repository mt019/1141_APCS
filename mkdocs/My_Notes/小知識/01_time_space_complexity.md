# 時間與空間複雜度入門

初學程式時，我們常問「這段程式快不快？會不會吃光記憶體？」時間複雜度（time complexity）與空間複雜度（space complexity）是回答這些問題的工具。本筆記以 LeetCode 與 APCS 常見的排序、搜尋例子為背景，帶你一步步建立直覺。

## 為什麼需要複雜度分析？
- **比較方法**：當有兩段程式都能解題，複雜度可以幫助挑出在大量輸入下更有效率的版本。
- **預估效能**：APCS 或 LeetCode 評測時，題目會設定時間／記憶體限制。理解複雜度能預先判斷程式是否會超時（TLE）或超出記憶體限制（MLE）。
- **建立習慣**：養成在寫程式時思考「這段迴圈跑幾次？」、「我新增的資料結構會佔多少記憶體？」的習慣。

## 兩個核心觀念：輸入規模與主導項
- **輸入規模（`n`）**：通常指資料的數量，例：陣列長度、圖的節點數、字串長度。
- **主導項**：當 `n` 變很大時，最大的那個項目決定總開銷。像 `3n^2 + 5n + 8`，`n^2` 就是主導項，因此複雜度會寫成 `O(n^2)`。

## 常見時間複雜度速查

| Big-O | 範例演算法 | 直覺比喻 |
| --- | --- | --- |
| `O(1)` | 以索引存取串列元素 | 一次就拿到答案 |
| `O(log n)` | 二分搜尋、平衡樹查找 | 每次砍掉一半範圍 |
| `O(n)` | 線性搜尋、計算總和 | 從頭到尾走一遍 |
| `O(n log n)` | 合併排序、堆排序 | 走一遍但每步多了 `log n` 處理 |
| `O(n^2)` | 氣泡排序、雙層巢狀迴圈 | 為每個元素做一次完整掃描 |
| `O(2^n)` | 子集合枚舉、某些遞迴 | 每多一個元素，工作量翻倍 |
| `O(n!)` | 全排列、暴力旅行推銷員 | 小範圍 OK，大一點就爆炸 |

### 小練習：判斷複雜度

```python
def linear_search(nums, target):
    for value in nums:  # 會跑 n 次
        if value == target:
            return True
    return False
```

- 迴圈最多檢查每個元素一次 → `O(n)`。
- 除了迴圈外沒有額外資料結構 → 空間複雜度 `O(1)`。

```python
def pairs(nums):
    result = []
    for i in range(len(nums)):  # n 次
        for j in range(i + 1, len(nums)):  # 最多約 n(n-1)/2 次
            result.append((nums[i], nums[j]))
    return result
```

- 雙層迴圈 → 約 `n * n / 2` 次 → `O(n^2)`。
- `result` 會儲存所有配對 → 空間複雜度 `O(n^2)`。

## 案例：分析排序演算法
1. **氣泡排序（Bubble Sort）**  
   - 兩層迴圈，每層最多跑到 `n` → `O(n^2)`。  
   - 只在陣列裡交換 → 空間 `O(1)`。  
   - 已排序的陣列只要一輪就結束 → 最佳情況 `O(n)`。
2. **堆排序（Heap Sort）**  
   - 建堆 `O(n)`，取出最小值 `n` 次，每次 `O(log n)` → 總和 `O(n log n)`。  
   - 若使用 Python `heapq`（複製一份），需要額外 `O(n)` 空間；若就地堆化則 `O(1)`。
3. **Timsort（Python `sorted` 使用）**  
   - 平均 `O(n log n)`，對幾乎排好的資料最優可到 `O(n)`。  
   - 空間 `O(n)`，因為需要併合暫存區。

## 什麼是空間複雜度？
時間複雜度計算「跑多久」，空間複雜度則量測「用多少記憶體」。即使時間複雜度一樣，空間需求也可能差很多。

```python
def square_numbers_in_place(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] * nums[i]
    return nums
```

- 直接改寫原本的陣列 → 額外空間 `O(1)`。

```python
def square_numbers_new_list(nums):
    result = []
    for value in nums:
        result.append(value * value)
    return result
```

- 新增一個 `result`，大小與輸入相同 → 空間 `O(n)`。  
- 儘管兩者時間複雜度都是 `O(n)`，但空間開銷不同。

## 如何實際估算？
1. **數迴圈**：有幾層巢狀？每層迴圈的範圍大概是多少？
2. **觀察遞迴**：遞迴深度通常就是時間與空間的乘數。像二分搜尋遞迴深度是 `log n`。
3. **列出資料結構**：是否建立新的陣列、字典、堆、佇列？
4. **忽略常數、低次項**：`2n + 5` 與 `n` 在 Big-O 裡都寫成 `O(n)`。

## 複習與延伸練習
- 判斷以下程式的時間與空間複雜度：

```python
def prefix_sums(nums):
    result = [0]
    total = 0
    for value in nums:
        total += value
        result.append(total)
    return result
```

- 回答：時間 `O(n)`，空間 `O(n)`（`result` 長度約 `n + 1`）。
- 嘗試分析其他 LeetCode Easy 題，例如 Two Sum、Valid Anagram，觀察字典或排序如何影響複雜度。

## 小結
- **時間複雜度** 告訴你程式跑多久，**空間複雜度** 告訴你程式會佔多少記憶體。
- Big-O 著重「趨勢」，忽略常數與低次項。
- 寫程式時養成「輸入變大會怎樣？」的提問習慣，會讓你在 APCS 與 LeetCode 解題時更快抓到重點。
- 如果對某個演算法不熟悉，試著手動跑一次流程並記錄迴圈／遞迴次數，就能逐步建立複雜度直覺。
