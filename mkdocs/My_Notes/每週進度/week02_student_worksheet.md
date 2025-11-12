# 第二週學習單 Week 2 Student Worksheet

## 課程資訊 Course Info
- **主題 Topic**：演算法效率與排序 Algorithm Efficiency & Sorting
- **課程長度 Duration**：120 分鐘（2 小時）
- **目標 Goal**：把上週閱讀挑選的演算法想法，延伸到時間與空間複雜度概念，為 APCS Python 做暖身 Connect last week's reading choices to time & space complexity as gentle APCS prep
- **你可以準備的工具 Helpful Things**：
  - 上週的排序筆記 Your sorting notes from Week 1
  - 老師自製 1–20 數字小紙片 Teacher-made number slips (1–20)
  - 筆與彩色貼紙 Pen and sticky dots
  - 可計時的裝置 Timer-capable device


## 預備提醒 Prior Knowledge Reminder
## 概念提醒 Quick Ideas
- 我們用「比較、交換、移動」等操作次數，來感受排序演算法要花多少時間。We count comparisons, swaps, or moves to sense how long a sort might take.
- 當輸入筆數變大，操作次數會跟著變；常見的說法有 `O(1)` 幾乎不變、`O(n)` 跟著成長、`O(n^2)` 成長得更快。Bigger inputs mean more steps; common patterns are `O(1)` (almost flat), `O(n)` (grows with n), and `O(n^2)` (grows faster).
- 等會兒我們會觀察自己的資料，猜猜它比較像哪一種成長，再練習用 Big-O 語言描述。We will look at our own data, guess the pattern, and practice naming it with Big-O.

---

你需要記得的數學 only includes：Here are the math bits you'll need:
- 基本加減乘除 Basic addition, subtraction, multiplication, division
- 次方與平方根 Powers and roots，例如 e.g., `2^3 = 8`
- 比較數字大小與簡單四捨五入 Compare numbers and round up/down (ceil/floor)
- 絕對值 Absolute value，例如 e.g., `abs(-7) = 7`


---

## 熱身 Warm-up (10 min)
- **快速回想 Recall**：
  - 我上週在書中挑到的演算法（圈選）The algorithm I bookmarked last week (circle one): 普林 Prim / 氣泡 Bubble / 雞尾酒 Cocktail / 堆 Heap / 直接插入 Insertion
  - 核心步驟 Core steps ________________________________________________
- **排序感覺排序線 Feeling Scale**：可以在「耗時」數線上寫下演算法名稱（或只要心裡想一想也行）You may place your algorithm on the "time taken" line—or just imagine it.
  - `慢 ←＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿→ 快`
- **問題反思 Prompt**：如果資料筆數翻倍，你猜操作次數會變成多少？寫下或口頭說說都可以。If the data doubles, what might happen to the steps? Jot or think aloud.
- **LeetCode 分享 Share**：回想上週課後作業，你觀察到的頁面/題目是什麼？用 2 句話描述。Which LeetCode page or problem did you explore? Summarize in two sentences.

---

## 活動一：演算法檔案庫 Algorithm Profile (about 20 min)
### 小小整理 Quick Pick
- 圈選今天要練的演算法 Pick one: □ 普林 Prim □ 氣泡 Bubble □ 雞尾酒 Cocktail □ 堆 Heap □ 直接插入 Insertion
- 寫一句你記得的關鍵步驟 Write one key step: ______________________________________________
- 想想等會兒要用的資料長度（例如 8、16、32）Plan input sizes: _______________________

> 如果忘了內容，可以翻翻上週筆記或 LeetCode 截圖。Peek at last week's notes if you need a reminder.


---

## 活動二：時間複雜度 Time Complexity (about 30 min)
1. **慢慢數步驟 Counting Steps at Your Pace**：挑一個你上週圈選的演算法，第一次用老師的 1–20 小紙片慢慢模擬，悠閒地記錄幾筆比較與交換次數。

| 輸入長度 Input Size (n) | 比較次數 Comparisons | 交換/移動次數 Swaps/Moves | 推斷關係 Estimated Relationship |
| --- | --- | --- | --- |
|  n =  |    |    |    |
|  n =  |    |    |    |
|  n =  |    |    |    |

2. **Big-O 轉換 Translate to Big-O**：
   - 常數項 Constant term → __________________ (丟棄？Keep or ignore?)
   - 高次項 Leading term → __________________
   - 最終 Big-O → `O(__________)`

3. **個案分析 Case Analysis**：

| 情境 Scenario | 預期時間複雜度 Expected Time Big-O | 理由 Reason |
| --- | --- | --- |
| 最佳 Best Case |    |    |
| 平均 Average Case |    |    |
| 最差 Worst Case |    |    |

- **APCS 小貼心 APCS Friendly Tip（想了解再看）**：Python 題目常以巢狀迴圈測試你對 `O(n^2)` 的判斷，注意迴圈範圍與遞迴深度 Pay attention to nested loops and recursion depth in APCS problems.

---

## 活動三：空間複雜度 Space Complexity (about 20 min)
1. **操作與觀察 Hands-on**：
   - 使用老師自製 1–20 數字小紙片模擬兩種排序：
     - 就地排序 In-place (例：插入排序 Insertion Sort)
     - 額外容器排序 Extra storage (例：合併排序 Merge Sort)

2. **比較表 Comparison Table**：

| 排序法 Algorithm | 額外記憶體 Extra Memory? | 空間複雜度 Space Big-O | 記憶體用途 Purpose |
| --- | --- | --- | --- |
|    | 是 / 否 |    |    |
|    | 是 / 否 |    |    |

3. **思考 Think**：
   - 當記憶體只有原本陣列大小時，你會選擇 __________________________
   - 原因 Reason：_______________________________________________________

- **APCS 小貼心 APCS Friendly Tip（想了解再看）**：題目可能要求你計算陣列以外的暫存變數數量，特別注意 `list.copy()` 或遞迴堆疊 Watch for extra lists (e.g., `list.copy()`) and recursion stack depth.

---

## 活動四：比較實驗 Growth Lab (about 30 min)
1. **想試的話 Try Timing Yourself**：使用 1–20 小紙片抽取 8、16、32 筆資料進行排序並記錄（若想休息，選幾個就好）。

| Input Size | 開始時間 Start | 結束時間 End | 實際耗時 Duration | 比較次數 Comparisons | 交換/移動 Swaps/Moves |
| --- | --- | --- | --- | --- | --- |
| 8 |    |    |    |    |    |
| 16 |    |    |    |    |    |
| 32 |    |    |    |    |    |

2. **圖形化 Plot**：
   - 在座標紙上標出 (Input Size, Comparisons)，或用想像的方式也不錯
   - 觀察點與哪條函數最接近？沒有標準答案，寫下你的感覺就好。`n`, `n log n`, `n^2`, 其他？
   - 寫下理由：___________________________________________________________

3. **推論 Predict**：試著想像輸入為 64 或 128，輕鬆推測時間複雜度與操作次數。

```
當 n = 64 時，我預測操作約 _______ 次，因為 ______________________________
當 n = 128 時，我預測操作約 _______ 次，因為 _____________________________
```

---

## APCS Python 小練習 APCS Python Gentle Practice (about 20 min)
閱讀下列程式碼，試著估計時間與空間複雜度（可以邊猜邊驗證）。Read the snippet and estimate complexities.

```python
# Snippet A
for i in range(n):
    j = i
    while j > 0 and data[j] < data[j - 1]:
        data[j], data[j - 1] = data[j - 1], data[j]
        j -= 1
```

- **時間複雜度 Time Big-O**：`O(__________)`
- **空間複雜度 Space Big-O**：`O(__________)`
- **理由 Reasoning**：____________________________________________________

```python
# Snippet B
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)
```

- **遞迴深度 Recursion Depth**：________________________________________
- **時間複雜度 Time Big-O**：`O(__________)`
- **空間複雜度 Space Big-O**：`O(__________)`
- **備註 Notes**：切片 `arr[:mid]` 會產生新串列，記得計入空間成本 Slicing creates new lists; include in space count.

- **挑戰 Challenge**：若改成就地合併 in-place merge，空間複雜度是否可降至 `O(1)`？
  - 你的想法 Your idea：____________________________________________________

---

## 詞彙加油站 Vocabulary Booster
- **時間複雜度 Time Complexity**：輸入規模成長時，演算法步驟怎麼增加 Growth of steps as input grows
- **空間複雜度 Space Complexity**：演算法運行時需要的額外記憶體 Extra memory needed during execution
- **Big-O 記號 Big-O Notation**：上界估計，忽略常數與低階項 Upper bound, ignoring constants and lower-order terms
- **In-place**：只在原陣列內操作 Operates within the original array
- **Trade-off**：在速度與記憶體之間做取捨 Balancing speed and memory usage

---

## 放鬆時間 Chill Reflection (about 10 min)
1. 今天我最清楚的複雜度概念是 _________________________________
2. 我仍有疑問的地方是 ______________________________________________
3. 如果想多練習，可以記下你想挑戰的題目類型（選填） Optional: jot a type of problem you might explore later _______________________________
4. Complete the sentence → "The time complexity of my algorithm is ______________ because ___________________."

---

## 延伸 Optional Extension
- 如果你有興趣：在 VisuAlgo 或 Python Tutor 上看看新的排序演算法，想記錄時可以使用下表 Observe if you like and jot it here.

| 新演算法 New Algorithm | 觀察來源 Source | 時間複雜度 Time Big-O | 空間複雜度 Space Big-O | 想在哪種情境測試 Scenario |
| --- | --- | --- | --- | --- |
|  .  |    |    |    |   |

- （想寫再寫）：輸入特性改變時，你的演算法選擇會如何調整？ A short bilingual reflection if you feel like it.

You’ve got this—enjoy the journey toward APCS Python!
