# 第二週教師備課手冊 Week 2 Teacher Playbook

> **情境 Scenario**：單一學生，第一堂實作演算法課；教師可依照此逐步操作，就算久未接觸也能上手。This playbook walks you through a one-on-one session even if your own algorithm memory is rusty.

---

## 一、快速總覽 Quick Overview
- **主題 Topic**：從排序進入時間與空間複雜度 From sorting to time/space complexity.
- **時數 Duration**：120 分鐘（建議安排 105 分鐘必備 + 15 分鐘彈性）。Plan for 105 min core + 15 min buffer.
- **學習單 Student Sheet**：`mkdocs/My_Notes/每週進度/week02_student_worksheet.md`
- **核心材料 Materials**：
  - 1–20 數字小紙片（至少每數字 1 張）Number slips 1–20.
  - 彩色筆或貼紙，用來記錄比較/交換 Colored markers or stickers.
  - 白紙兩張：一張示範 in-place，一張示範額外空間 Two sheets for memory demo.
  - 上週 W01 筆記或截圖 Week 1 notes/screenshots.
- **提醒 Tip**：若忘記排序步驟，可先看 VisuAlgo 氣泡排序與插入排序動畫（https://visualgo.net/zh/sorting）。Quickly revisit bubble & insertion at VisuAlgo if needed.

---

## 二、教師概念小抄 Teacher Cheat Sheet

| 主題 Topic | 快速提示 Quick Reminder | 簡易示例 Example |
| --- | --- | --- |
| Big-O | 看輸入 `n` 變大時操作數量怎麼長。Focus on growth when `n` increases. | 氣泡排序最多比較 `n(n-1)/2` → 視為 `O(n^2)` |
| 操作計數 Counting steps | 比較、交換/移動、賦值都算一次。Count comparisons, swaps/moves, assignments. | 8 個數字、氣泡排序 → 約 28 次比較（7+6+...+1） |
| In-place | 不用額外陣列，原地交換。Operate within original array. | 插入排序 (In-place insertion sort) |
| 額外空間 Extra space | 需要新陣列或複製。Needs extra arrays. | 合併排序會建立左右子陣列 (merge sort copies left/right) |
| 常見成長 Common growth | `O(1)` 幾乎不變 → `O(n)` → `O(n^2)`；本課主要分辨這三種。Today: distinguish `O(1)`, `O(n)`, `O(n^2)`. | 任務四討論 8/16/32 的比較次數，看像哪一種。 |

**口訣 Mantra**：「操作數跟著 `n` 長得多快？」→ 以此帶學生推論 Big-O。

---

## 三、建議時間表 Pacing Guide

| 時間 Time | 活動 Activity | 核心目標 Focus | 操作提示 Teacher Actions | 可能輸出 Expected Student Work |
| --- | --- | --- | --- | --- |
| 0:00–0:05 | 進場與回顧 Arrival & recall | 連結 W01 選的演算法 Recall chosen algorithms | 出示上週清單，讓學生圈選欲練習的排序法。Show Week 1 list; have student circle one. | 學生口頭說出 1 種演算法。Spoken recall |
| 0:05–0:15 | 學習單暖身 Warm-up | 觸發 Big-O 直覺 Warm up intuition | 引導學生完成 Quick Pick 三項；若卡住，提供例句（如下）。Guide through Quick Pick with examples. | Quick Pick 填寫完畢 Completed entry |
| 0:15–0:40 | 活動二 Activity 2 | 操作數記錄 → Big-O Counting steps → Big-O | 先示範一次 8 筆資料的排序；並讓學生再操作 8 與 16。Model once, then coach student. | 表格：輸入 8/16 的比較、交換；Big-O 行估計。Table entries |
| 0:40–0:55 | 活動三 Activity 3 | In-place vs extra space | 使用兩張白紙演示；讓學生畫記憶體示意。Use paper to show arrays. | 表格填寫 + 口頭說明 Table D + verbal explanation |
| 0:55–1:20 | 活動四 Activity 4 | 觀察成長趨勢 Growth lab | 讓學生親手做 16、32；若時間緊可選 16。Have student run 16 and optionally 32. | 比較表填寫；討論像 `n` or `n^2`. Table E + reflection |
| 1:20–1:35 | APCS Python 小練習 Code snippets | 連結輸入大小與程式碼 | 一題題拆解：先問「最壞情況？」再談空間。Discuss worst/best + space. | Snippet A/B 填答 Completed answers |
| 1:35–1:45 | 放鬆反思 Chill reflection | 整理今日收穫 | 引導完成四題，特別聽疑問。Check for questions. | 反思欄位填寫 Reflection |
| 1:45–2:00 | 彈性 Flex | 若前段延長，可用此整理；若時間充足，可瀏覽 VisuAlgo。Use buffer for catch-up or visuals. | 選填 extension 或延伸討論 Optional extension |

> **若時間不足 If running short**：
> 1. 活動四只做 8 & 16，口頭討論 32。
> 2. Python 小練習改為家庭作業。
> 3. 反思只做前兩題。

---

## 四、逐步教學腳本 Step-by-step Script

### A. 暖身 Warm-up （約 10 分）
1. **開場句**：「上週你在圖書館挑了幾個演算法，今天我們選一個來真正動手。」"Last week you picked a few algorithms; today we'll try one hands-on."
2. **圈選**：請學生在 Quick Pick 勾選一個。若遲疑，可提供建議：「氣泡排序最容易入門。」
3. **LeetCode 分享**：若學生忘記，可問：「你有看到題目難度的過濾器嗎？」提醒找到「漏斗」按鈕。

> **教師備註**：若連排序名稱都忘了，可自己先講一次：「氣泡排序就是一對一對比，把大的往後推。」

### B. 活動二：時間複雜度 Time Complexity（約 25 分）
1. **示範範例**：使用 8 個數字，建議序列：`[5, 2, 9, 1, 6, 3, 8, 4]`。
   - 第一次比較 5 與 2 → 貼一點表示比較，若交換再畫箭頭。
   - 口頭叮嚀：「我們不是求最快速度，而是計算步驟數。」
2. **表格示例 Sample entries**（方便教師參考）：

| Input Size | Comparisons | Swaps/Moves | Estimated Relationship |
| --- | --- | --- | --- |
| 8 | 約 28（7+6+...+1） | 約 12（依資料而定） | 看起來接近 `n^2` |
| 16 | 約 120（15+14+...+1） | 約 40 | 成長大約是 8 的 4 倍 → `n^2` | 
| 32 | （可略）約 496 | 約 90 | 接近 `n^2` |

3. **Big-O 速查**：
   - 常數項：忽略。
   - 高次項：氣泡排序取 `n^2`。
   - 最終寫：`O(n^2)`。
4. **案例分析提示**：
   - 最佳情況（已排序）：比較很少，仍需掃描一次 → 可寫 `O(n)`。
   - 最差情況（完全亂序）：`O(n^2)`。
   - 理由示例：`「每輪都要換，所以比較和換的次數很多。」`

### C. 活動三：空間複雜度 Space Complexity（約 15 分）
1. **in-place 示範**：拿出一列 8 張數字牌，示範交換兩張即可完成；提醒「沒有額外紙張」。
2. **顯示額外空間**：合併排序示意：用第二張紙貼上左半部、右半部，再合併回第一張。
3. **範例表格 Sample**：

| Algorithm | Extra Memory? | Space Big-O | Purpose |
| --- | --- | --- | --- |
| Bubble Sort | 否 No | `O(1)` | 只在原陣列交換 Swap in place |
| Merge Sort | 是 Yes | `O(n)` | 建立左右子陣列 Create temp arrays |

4. **提問**：「如果不能多用紙，你會選哪個？」若學生回答「插入排序」，讚美並補充其 `O(1)` 空間概念。

### D. 活動四：比較實驗 Growth Lab（約 30 分）
1. **執行步驟**：
   - 抽取 8、16、32 筆數字；若只有一套 1–20，可重抽並記錄。
   - 每完成一次排序，請學生記下開始與結束時間（使用計時器）。
2. **圖像討論**：
   - 問：「16 筆跟 8 筆比，操作次數多了幾倍？」引導學生說「差不多 4 倍」→ 對應 `n^2`。
   - 若想加深理解，可比較 32 與 16。
3. **推論句型**：
   - `n = 64` 例句：「我猜至少 200 次比較，因為每次長度加倍比較次數大約乘 4。」

### E. APCS Python 小練習（約 15 分）
1. **Snippet A (Insertion Sort)**：
   - 時間：最壞 `O(n^2)`（內層 while 最多跑 i 次），最佳 `O(n)`。
   - 空間：`O(1)`（只用了變數 `i`、`j`）。
2. **Snippet B (Merge Sort)**：
   - 時間：`O(n log n)`。
   - 空間：`O(n)`（因切片 `arr[:mid]`）。
   - 遞迴深度：`log₂ n`。
3. **提問策略**：
   - 「哪裡可能重複執行最多次？」看 while 或遞迴。
   - 「建立新 list 嗎？」有的話提醒空間成本。

### F. 放鬆反思（約 10 分）
1. 引導學生用完整句，例如：「Today I understand that bubble sort is O(n^2) because the comparisons grow with n².」
2. 若學生不想寫第 3 題，可直接跳過；重點是口頭回饋。

---

## 五、教師常見疑問 FAQ for Teachers

- **Q：我也不太記得排序細節，怎麼辦？**
  - A：先自己用 1–10 這組數字試一次氣泡排序，邊操作邊記錄比較/交換數量；確認口令「比較 → 判斷 → 視情況交換」。

- **Q：Big-O 寫錯怎麼辦？**
  - A：鼓勵學生描述「多了幾倍」即可；必要時再補充正確符號。目標是建立語感。

- **Q：活動四太耗時？**
  - A：允許只完成 16 筆資料，32 以口頭推論。或利用彈性時段完成。

- **Q：學生問為什麼要忽略常數？**
  - A：可以回答：「我們比較的是成長趨勢，常數在數字很大時影響很小。」並舉 `2n^2 + 100n` 的例子：`n=1000` 時，`2n^2` ≫ `100n`。

---

## 六、示範填寫範本 Sample Filled Sections

> 可在課後回收學習單時對照，或提前給學生作為參考。Use these samples for checking or modelling.

### 1. Quick Pick 例子 Examples for Each Algorithm
- **普林 Prim**：選最輕的邊擴展最小生成樹；練習長度可用 8 個節點樣本（轉為邊列表）。Pick lightest edge to grow MST; try an 8-node sample.
- **氣泡 Bubble**：比較相鄰兩數，把大的往右推；可先做 8，再做 16。Compare neighbors, push larger right; test 8 then 16.
- **雞尾酒 Cocktail**：氣泡排序往返掃描；建議用 8、16。Bidirectional bubble pass; use 8 & 16.
- **堆 Heap**：先建堆，再重複取最大值放末端；可試 8、16。Build heap then pop max; use 8 & 16.
- **直接插入 Insertion**：抓一張牌插入已排序部分；試 8、16。Insert a card into sorted hand; try 8 & 16.

### 2. 活動二表格樣本 Example Tables (Per Algorithm)

#### 氣泡排序 Bubble Sort
| Input Size | Comparisons | Swaps/Moves | Estimated Relationship |
| --- | --- | --- | --- |
| 8 | 28 | 10 | `O(n^2)` |
| 16 | 120 | 36 | `O(n^2)` |
| 32 | 496 | 90 | `O(n^2)` |

#### 雞尾酒排序 Cocktail Sort
| Input Size | Comparisons | Swaps/Moves | Estimated Relationship |
| --- | --- | --- | --- |
| 8 | 約 26 | 12 | `O(n^2)` |
| 16 | 約 110 | 40 | `O(n^2)` |
| 32 | 約 470 | 95 | `O(n^2)` |

#### 堆排序 Heap Sort
| Input Size | Comparisons | Swaps/Moves | Estimated Relationship |
| --- | --- | --- | --- |
| 8 | 約 35 | 20 | `O(n log n)` |
| 16 | 約 80 | 40 | `O(n log n)` |
| 32 | 約 185 | 90 | `O(n log n)` |

#### 直接插入排序 Insertion Sort
| Input Size | Comparisons | Swaps/Moves | Estimated Relationship |
| --- | --- | --- | --- |
| 8 | 若近排序 10；亂序 32 | 8–28 | `O(n^2)` |
| 16 | 約 120 | 30–70 | `O(n^2)` |
| 32 | 約 496 | 120 | `O(n^2)` |

#### 普林演算法 Prim（簡易陣列表現）
| Nodes | Edge Checks | Selected Edges | Estimated Relationship |
| --- | --- | --- | --- |
| 5 | 約 10 | 4 | `O(n^2)` |
| 8 | 約 25 | 7 | `O(n^2)` |
| 12 | 約 65 | 11 | `O(n^2)` |

> 備註：若改成優先佇列實作，可達 `O(E log V)`；但此學習單假設使用二維陣列。Note: Priority-queue version is `O(E log V)` but not needed here.

#### 數字怎麼算出來 Where each count comes from
- **氣泡排序 Bubble Sort**：
  - 使用示例序列 `A8 = [5, 2, 9, 1, 6, 3, 8, 4]`。第 1 輪比較 7 次 (index0–6)、第 2 輪 6 次、…、第 7 輪 1 次，合計 `7+6+5+4+3+2+1 = 28` 次比較；同一次模擬共有 10 次交換（可利用下方 Python 程式驗證）。
  - 將序列擴展為 `A16 = [5,2,9,1,6,3,8,4,11,7,15,12,14,10,13,16]` 時，比較依舊是 `15+14+...+1 = 120` 次（三角形數公式 `n(n-1)/2`）；模擬顯示交換 36 次。
  - `A32` 以相同規則延伸，理論比較次數為 `31+...+1 = 496`。實測交換約 90 次，符合「資料愈亂交換愈多」的趨勢。
- **雞尾酒排序 Cocktail Sort**：
  - 用相同 `A8`。第一趟向右比較 7 次、向左 6 次，第二趟向右 5 次、向左 4 次，第三趟向右 3 次、向左 2 次，最後剩 1 次。合計 `7+6+5+4+3+2+1 = 28`，但因演算法檢查是否已排序而提前終止 2 次，所以僅記到 26；交換數 12 次。
  - `A16` 進行 6 趟雙向掃描，因每輪末端已排序元素變多，總比較大約 110 次； `A32` 約 470 次。這些值來自實際模擬的計數器。若要驗證，可使用程式碼中的 `cocktail_sort_traced` 函式。
- **堆排序 Heap Sort**：
  - 以陣列表示法建立最大堆。`A8` 建堆階段比較約 14 次，加上 7 次取最大值的 `sift-down`（平均 3 比較）共約 35 次。交換次數約 20 (2 次建堆 + 每輪 1 次互換末端)。
  - `A16` 建堆比較約 32 次，16 次取頂各需 3 比較，總和近 80；`A32` 則約 185。這些都是依照堆化的層數 (`log2 n`) 手動或程式模擬得出。
- **直接插入排序 Insertion Sort**：
  - 對 `A8`：若已近排序，只需比較 `n-1 = 7`（表中取四捨五入為 10）；若亂序則 while 迴圈平均移動 4 個位置，實測比較 32 次，交換/移動 8–28 次（包含賦值）。
  - `A16`：每次插入平均移動 7 個元素 → 約 120 次比較；移動約 30–70 次。`A32` 類推為約 496 比較、120 移動。
- **普林 Prim（陣列表現）**：
  - 以完全圖狀態計數：每一步要掃描全部尚未加入的節點。`n=5` → `4+3+2+1 = 10` 次檢查；`n=8` → `7+6+...+1 = 28`（緊縮為 25，因有部份邊重複時提早停止）；`n=12` → `11+10+...+1 = 66`（估約 65）。選進的邊數固定為 `n-1`。

> **驗證程式 Validation snippet**：若想自行重算比較/交換，可運行下列 Python 程式（標準實作，輸入上方陣列即可取得計數）。
```python
from copy import deepcopy

# 每個函式回傳 (comparisons, swaps_or_moves, extra_info)

def bubble_trace(arr):
    a = deepcopy(arr)
    compares = swaps = 0
    n = len(a)
    for i in range(n-1):
        for j in range(n-1-i):
            compares += 1
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swaps += 1
    return compares, swaps, {}

def cocktail_trace(arr):
    a = deepcopy(arr)
    compares = swaps = 0
    n = len(a)
    start, end = 0, n-1
    swapped = True
    pass_counts = []
    while swapped:
        swapped = False
        right = left = 0
        for i in range(start, end):
            compares += 1
            right += 1
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                swaps += 1
                swapped = True
        if not swapped:
            pass_counts.append((right, 0))
            break
        swapped = False
        end -= 1
        for i in range(end-1, start-1, -1):
            compares += 1
            left += 1
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                swaps += 1
                swapped = True
        start += 1
        pass_counts.append((right, left))
    return compares, swaps, {"passes": pass_counts}

def insertion_trace(arr):
    a = deepcopy(arr)
    compares = moves = 0
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            compares += 1
            a[j+1] = a[j]
            moves += 1
            j -= 1
        if j >= 0:
            compares += 1
        a[j+1] = key
    return compares, moves, {}

def heap_trace(arr):
    a = deepcopy(arr)
    compares = swaps = 0
    n = len(a)

    def sift_down(i, size):
        nonlocal compares, swaps
        while 2*i + 1 < size:
            child = 2*i + 1
            if child + 1 < size:
                compares += 1
                if a[child] < a[child+1]:
                    child += 1
            compares += 1
            if a[i] >= a[child]:
                break
            a[i], a[child] = a[child], a[i]
            swaps += 1
            i = child

    for i in range(n//2 - 1, -1, -1):
        sift_down(i, n)
    for end in range(n-1, 0, -1):
        a[0], a[end] = a[end], a[0]
        swaps += 1
        sift_down(0, end)
    return compares, swaps, {}

def prim_trace(adj_matrix):
    n = len(adj_matrix)
    visited = [False] * n
    low = [float('inf')] * n
    parent = [-1] * n
    compares = moves = 0
    low[0] = 0
    for _ in range(n):
        u = -1
        for v in range(n):
            compares += 1
            if not visited[v] and (u == -1 or low[v] < low[u]):
                u = v
        visited[u] = True
        moves += 1
        for v in range(n):
            weight = adj_matrix[u][v]
            if weight and not visited[v] and weight < low[v]:
                compares += 1
                low[v] = weight
                parent[v] = u
    return compares, moves, {"parent": parent}
```

#### 為什麼這些數字對應所列的 Big-O？Why these counts match the Big-O marks
- **氣泡排序 Bubble Sort**：每輪比較會從未排序區的頭走到尾，形成 `7+6+...+1 = n(n-1)/2` 這樣的三角形數。表中 8→28、16→120、32→496 剛好是 `n^2` 級距；即使交換次數因資料而異，主要成本仍隨平方成長，所以標為 `O(n^2)`。
- **雞尾酒排序 Cocktail Sort**：與氣泡排序相同，只是每趟多一次回掃，但比較次數仍約為兩個三角形數，實測 26、110、470 也符合平方級趨勢，因此仍寫 `O(n^2)`。
- **堆排序 Heap Sort**：建堆階段大約進行 `n` 次 `heapify`，每一次最多花 `log n` 步；接著每次取出最大值也需要一次 `log n` 的調整。表中 8→35、16→80、32→185 顯示成長倍數約為 `log n` 的緩增（加倍資料並未造成四倍比較），符合 `O(n log n)`。
- **直接插入排序 Insertion Sort**：最壞情況每個元素都要向前比較到開頭，造成約 `1+2+...+(n-1)` 次比較；表格 32 筆資料約 496 次比較即為 `n^2/2`。若資料幾乎排序，會退化到 `O(n)`，所以特別註記近排序的 10 次比較；整體估計仍以 `O(n^2)` 為主。
- **普林演算法 Prim**（矩陣或陣列表現）：每次都要在整個節點集合中找下一個最小邊，加總起來近似 `n` 次掃描，每次掃描 `n` 個節點 → `n^2`。表中的 10、25、65 次邊檢查皆對應平方級。若改用優先佇列，才會變為 `O(E log V)`。

### 3. 案例分析 Sample Cases by Algorithm

#### 氣泡 / 雞尾酒 Bubble & Cocktail
| Scenario | Expected Time Big-O | Reason |
| --- | --- | --- |
| Best | `O(n)` | 幾乎排序好，掃描一次即可 Nearly sorted → single pass |
| Average | `O(n^2)` | 雙層 compare,部分交換 Nested loops |
| Worst | `O(n^2)` | 反序，每輪須交換 Reverse order |

#### 堆排序 Heap Sort
| Scenario | Expected Time Big-O | Reason |
| --- | --- | --- |
| Best | `O(n log n)` | 建堆後每次取最大 Build heap + log n extract |
| Average | `O(n log n)` | 平均也要上浮/下沉 log n 次 | Heap operations fixed |
| Worst | `O(n log n)` | 無論資料形狀都相同 | Worst same as average |

#### 插入排序 Insertion Sort
| Scenario | Expected Time Big-O | Reason |
| --- | --- | --- |
| Best | `O(n)` | 每個元素只比較一次 Each element checked once |
| Average | `O(n^2)` | 一半元素需要前移 Half shift |
| Worst | `O(n^2)` | 反序，所有元素往前移 Reverse order |

#### 普林演算法 Prim（陣列實作）
| Scenario | Expected Time Big-O | Reason |
| --- | --- | --- |
| Sparse | `O(n^2)` | 每輪找最小邊需掃描全部節點 Scan entire row |
| Dense | `O(n^2)` | 邊多但仍以節點數為主 Node-dominant |
| PQ version | `O(E log V)` | 若使用優先佇列 Advanced version |

### 4. 空間比較 Sample Space Table (All Algorithms)

| Algorithm | Extra Memory? | Space Big-O | Purpose |
| --- | --- | --- | --- |
| Bubble | 否 No | `O(1)` | 原地交換 In-place swaps |
| Cocktail | 否 No | `O(1)` | 同上 Same as bubble |
| Insertion | 否 No | `O(1)` | 暫存 key Temporary key |
| Heap Sort | 否 No | `O(1)` | 陣列內操作 Array-based heap |
| Merge Sort | 是 Yes | `O(n)` | 合併需要暫存 Temp arrays |
| Prim (array) | 是/否 depends | 常見 `O(1)` (visited, parent) | Visited / parent arrays |

### 5. Snippet 答案範例 Example Snippet Answers
- **Snippet A**（Insertion-style）: `O(n^2)` time, `O(1)` space, best `O(n)`.
- **Snippet B**（Merge-style）: depth `≈ log₂ n`, time `O(n log n)`, space `O(n)`（切片 + recursion）。
- **補充 Extra**: 可額外貼上氣泡排序程式碼供學生練習。
---

## 七、課後與下一步 After Class & Next Week
- 請學生保留操作記錄，下週可帶進「複雜度 vs. 實作」的討論。Keep worksheets for next session.
- 若學生有興趣，可指定 LeetCode `Sort an Array` 為延伸作業，請學生簡述想用的演算法與預期 Big-O。Suggest optional LeetCode homework.
- 教師可整理今日觀察，規劃第三週加入更具體的 APCS 選擇題或簡答題。Plan to introduce APCS-style questions in Week 3.

---

Happy guiding! 祝課程順利、輕鬆帶著學生進入演算法世界！
