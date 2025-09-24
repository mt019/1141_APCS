# 線上評測常見輸入輸出技巧（Python）

APCS 與 LeetCode 題目多半採用「從標準輸入讀資料、輸出答案」的模式。以下整理常見的讀取方法與注意事項。

## 1. 基本 `input()`

```python
n = int(input())              # 讀取單一整數
line = input().strip()        # 讀取一行並移除換行
tokens = line.split()         # 預設以空白拆分
numbers = list(map(int, tokens))
```

- `strip()`：移除左右空白（包含換行）。
- `split()`：依空白拆字串。可傳入分隔符，例如 `split(',')`。

## 2. 多行輸入

```python
n = int(input())
data = [int(input()) for _ in range(n)]
```

- 逐行讀取 `n` 筆資料。

## 3. 搭配 `sys.stdin`
當輸入量很大（例如上萬行）時，`input()` 可能偏慢，可改用 `sys.stdin`：

```python
import sys

data = sys.stdin.read().strip().split()  # data 會是一串字串
numbers = list(map(int, data))
```

- `read()` 會一次讀完所有內容。
- 若資料量不大，`input()` 就足夠，程式更好讀。

## 4. 矩陣輸入範例
給定範例輸入：

```text
3 4
1 2 3 4
5 6 7 8
9 10 11 12
```

對應程式：

```python
rows, cols = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(rows)]
```

- `map(int, input().split())`：將每行轉成整數列表。

## 5. 常見輸出技巧

```python
print(answer)                         # 最簡單
print(' '.join(map(str, array)))      # 將陣列以空白分隔輸出
print(*array)                         # Python 的解包輸出
```

若需要固定小數位數：

```python
avg = 12 / 5
print(f"{avg:.2f}")  # → 2.40
```

## 6. 綜合範例：APCS 常見資料格式
題目：第一行 `n`，接著 `n` 行，每行學生姓名與成績。

```python
n = int(input())
records = []
for _ in range(n):
    name, score = input().split()
    records.append((name, int(score)))

records.sort(key=lambda x: x[1], reverse=True)
for name, score in records:
    print(name, score)
```

## 7. 陷阱提醒
- 注意空行：有些題目會在區塊之間插入空行，可先檢查 `line = input().strip()` 是否為空字串。
- 讀檔 vs. 標準輸入：在本地測試時可使用檔案，但提交時記得改回標準輸入。
- 使用 `split()` 前確認題目分隔符（空白、逗號、冒號…）。

## 練習建議
1. 練習讀取 `m x n` 表格並列出每列總和。
2. 練習處理「未知行數」的輸入，可搭配 `sys.stdin` 讀到 EOF。
3. 模仿 APCS 題目：輸入多組測試資料，每組包含多行，確保迴圈控制正確。

## 小結
- 多試幾種輸入樣式，建立肌肉記憶，上考場就不會慌。
- 寫函式包裝輸入處理，可重複使用（例如：`read_ints()`、`read_matrix()`）。
- 若題目資料大，優先檢查輸入輸出是否成為瓶頸。
