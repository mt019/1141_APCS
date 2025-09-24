# 第二週教學指引 Week 2 Teacher Guide

## 課程總覽 Session Overview
- **主題 Topic**：演算法效率與排序 Algorithm Efficiency & Sorting
- **時數 Duration**：120 分鐘（2 小時）
- **班級規模 Class Size**：1 位學生 One-on-one learner
- **課程目標 Lesson Goal**：
  - 以學生第一週在圖書館所圈選的 5 個演算法為出發，建立時間複雜度與空間複雜度的直覺 Bridge last week's selected algorithms to time & space complexity intuition.
  - 透過實際操作 1–20 數字小紙片，引導學生從操作次數推論 Big-O 整體趨勢 Use hands-on number slips to infer Big-O growth.
  - 串連 APCS Python 考試常見題型，熟悉巢狀迴圈與 recursion 的效率語言 Connect work to APCS Python patterns (nested loops, recursion).

## 事前準備 Pre-class Setup
- 老師自製 1–20 數字小紙片 Teacher-made number slips (1–20 pieces).
- W01 課堂筆記與學生 LeetCode 截圖或文字紀錄 (供回顧用) Week 1 notes and student LeetCode artifacts.
- 白板 / A3 紙 + 彩色筆 Whiteboard or large paper + markers.
- 計時器 Timer app (供示範使用，可開啟手機計時器即可).
- 若需線上資源，可預先開啟 VisuAlgo「排序」動畫頁面 Optional: open VisuAlgo sorting animations.

> **提示 Tip**：一對一情境可走「教練模式」，適時示範後再請學生口頭描述與操作。Adopt a coaching stance—model briefly, then invite the learner to narrate and try.

## 本週學習重點 Learning Focus
1. **語言轉換 Language Bridge**：鼓勵學生以中文思考後練習說出英文關鍵詞 (time complexity, in-place 等) Encourage bilingual articulation.
2. **數據觀察 Data Observation**：使用變動的 `n` 判斷趨勢，讓學生自述「我看到的操作次數長這樣…」Help student craft personal observations.
3. **APCS 對應 APCS Alignment**：強調巢狀迴圈 `O(n^2)`、merge sort `O(n log n)`、insertion sort best-case `O(n)` 等常見概念 Highlight exam-relevant cases.

---

## 課程流程 Lesson Flow (120 min)

| 時段 Time | 活動 Activity | 教師行動 Teacher Moves | 學生輸出 Student Evidence |
| --- | --- | --- | --- |
| 0:00–0:10 | 暖身 Warm-up | 用學生 W01 清單帶學生圈選演算法，請對比 LeetCode 作業；做時間估計提問 Prompt student to circle algorithm from Week 1 list, connect to LeetCode homework, ask doubling question | 口頭敘述 + W02 學習單 warm-up 填答 Spoken recap + warm-up entries |
| 0:10–0:30 | 活動一 Activity 1 | 引導撰寫 Table A，追問「為什麼覺得這個演算法熟悉？」Probe reasons for familiarity; show how to reference notes/screenshots | 完成演算法檔案表 + 個人結論 Completed Table A + takeaway |
| 0:30–1:00 | 活動二 Activity 2 | 示範一次 8 筆資料的手動演算法，計程式；用顏色標記比較 vs 交換 Use color markers to distinguish comparisons vs swaps; coach Big-O translation | 表格記錄 + Big-O 填寫 Table entries + Big-O estimates |
| 1:00–1:20 | 活動三 Activity 3 | 介紹 in-place vs extra space，拿兩張白紙演示「額外緩衝」Show memory diagrams on paper | 填寫空間比較表 & 口頭描述 Table D + verbal explanation |
| 1:20–1:50 | 活動四 Activity 4 | 依序讓學生操作 16、32 筆資料；鼓勵拍照或錄螢幕記錄 Encourage logging via photo/video; discuss growth | 實測資料表 + 口頭圖像描述 Table E + plotted/imagined trend |
| 1:50–2:00 | APCS 小練習 + 反思 APCS practice + reflection | 一起走過 Snippet A/B，討論 `while` 的最差情況、`arr[:]` 的空間；收斂今日收穫 Review code snippets, emphasize worst-case loops and slicing cost; guide exit reflection | 填寫 Snippet 答案 + 反思題 Completed snippet answers + reflection |

---

## 活動細節與引導 Notes by Activity

### 暖身 Warm-up (10 min)
- **教師提問 Teacher Prompts**：
  - 「上週你在 LeetCode 看到哪個介面？有沒有看到排序相關的題目？」Which LeetCode area did you explore?
  - 「如果資料筆數翻倍，你覺得操作次數大概會怎麼變？」How might steps scale when data doubles?
- **觀察指標 Look-fors**：
  - 學生能說出至少 1 個演算法的中文與英文名稱 Student names one algorithm in both languages.
  - 能提到 LeetCode 的一個元素 (難度、語言、題目) Mentions one LeetCode observation.
- **差異化 Differentiation**：若學生記不清，可展示 W01 課堂紀錄或 LeetCode 截圖帶入記憶 Use Week 1 artifacts as memory aids.

### 活動一 Activity 1：演算法檔案庫 (20 min)
- **教師重點 Focus**：讓學生用自己的語言描述演算法核心步驟 Encourage own words explanation.
- **支援 Support**：可用流程圖／關鍵字提示，如「比較」「交換」「選取最小邊」「堆化」 Provide keywords.
- **延伸 Extend**：請學生補一句英文，例如 "Prim's algorithm keeps picking the lightest edge." Add simple English sentence.
- **評量 Evidence**：完成 Table A + 關鍵結論；教師可寫下提示供下週追蹤 Capture notes for follow-up.

### 活動二 Activity 2：時間複雜度 (30 min)
- **示範 Demo**：
  - 以學生選的排序法建立 8 筆資料（例如 3, 10, 1, 6...）。
  - 每比較一次放一顆貼紙，交換一次畫星號 Use stickers or marks for comparisons/swaps.
  - 計時並與學生討論「如果是 16 筆呢？」Discuss scaling.
- **引導問題 Guiding Questions**：
  - 「為什麼我們只寫高次項？」Why keep only leading term?
  - 「最佳/最差案例會是哪種資料排列？」What arrangement leads to best/worst case?
- **常見誤解 Misconception Watch**：
  - 將 `O(n^2)` 誤寫為 `O(2n)`；提醒指數不是係數 Clarify exponents vs coefficients.
- **評量 Evidence**：Table (比較/交換) + Big-O 三欄；教師可標註是否需要複習 Record needs for review.

### 活動三 Activity 3：空間複雜度 (20 min)
- **棄用 vs 保留**：示範 insertion sort 原地交換；再示範 merge sort 需要左右子陣列 Explain in-place vs new arrays.
- **視覺化 Visualization**：
  - 用兩色紙條代表主陣列與額外記憶體 Use two colors to represent arrays.
  - 請學生畫出自己的記憶體示意圖 Have learner sketch memory usage.
- **引導問題 Questions**：
  - 「如果不能多用一塊紙片，你會怎麼做？」What if no extra array allowed?
  - 「遞迴呼叫時，Python 會幫我們用多少空間？」Discuss recursion stack.
- **評量 Evidence**：Table D + 口頭說明；教師可記錄學生對 recursion 的理解度 Note recursion comprehension level.

### 活動四 Activity 4：比較實驗 (30 min)
- **流程 Steps**：
  1. 抽取 8/16/32 筆資料排序，鼓勵學生自己計時 Encourage self-timing.
  2. 帶學生將數據點標在座標紙上，或者使用「想像位置」方法 Plot or imagine positions.
  3. 討論「實測 vs. 推論」差異 Compare observed vs predicted growth.
- **引導問題 Questions**：
  - 「如果點看起來接近 n^2，表示什麼？」What does proximity to n^2 mean?
  - 「哪種資料形狀會讓結果不一樣？」How does data arrangement affect results?
- **備註 Notes**：一對一可適度減少樣本量，如只完成兩組即可，可補充討論 Additional discussion can replace missing trials.

### APCS Python 小練習 (20 min)
- **策略 Strategy**：
  - Snippet A：聚焦 while 可能重複 `i` 次 → `O(n^2)`；空間為 `O(1)` Focus on while loop repeating per i.
  - Snippet B：討論遞迴樹、切片成本 `O(n)`；空間 `O(n)` due to slices & recursion Discuss recursion tree and slicing cost.
- **引導問題 Questions**：
  - 「最佳情況下 Snippet A 會多快？」What is best case for Snippet A?
  - 「如果不作 `arr[:mid]`，空間會如何？」What happens without slicing?
- **評量 Evidence**：完成表格 + 口頭推理 Completed entries + verbal justification.

### 放鬆反思 Chill Reflection (10 min)
- **教師任務 Teacher Move**：
  - 一起檢視四題反思，引導學生用完整句回答（中英皆可） Review reflection questions together.
  - 確認學生能說出至少一個「仍困惑」的點以供下週教學參考 Capture next-step needs.
- **收束 Wrap-up**：
  - 分享下週預告：將把時間/空間複雜度帶入 LeetCode 題目練習 Tease next class focus.

---

## 評量與紀錄 Assessment & Documentation
- **形成性評量工具 Formative Tools**：W02 學習單、教師觀察筆記、學生口頭說明 Worksheet responses, observation notes, verbal explanations.
- **建議紀錄方式 Suggested Logging**：
  - 將關鍵對話或學生句子抄在教師筆記中 Capture key student statements.
  - 若學生同意，可拍下排序操作過程作為證據 Photograph sorting sequence with permission.
- **APCS 對應檢核 APCS Alignment Checklist**：
  - [ ] 學生能說出至少一個 `O(n^2)` 排序演算法 Names an `O(n^2)` algorithm.
  - [ ] 一次說明最佳/平均/最差案例差異 Articulates best/average/worst case.
  - [ ] 能指出 merge sort 需要額外空間 Recognizes merge sort's extra space.
  - [ ] 能從程式碼 snippet 判斷 Big-O Estimates Big-O from code.

---

## 差異化與支援 Differentiation & Support
- **如果學生進度較快 Fast Learner**：
  - 安排額外輸入規模（64、128）或請學生撰寫簡短 Python 程式模擬 Provide larger n or quick Python scripts.
  - 引導討論 Prim 演算法與排序的差異，延伸到圖形結構 Introduce graph algorithm discussion.
- **如果學生需要更多引導 Needs More Support**：
  - 以圖卡或貼紙輔助比較/交換計數 Use visual aids for counting.
  - 先口頭描述 Big-O，再協助寫上符號 Verbal explanation before notation.

---

## 課後追蹤 After-class Follow-up
- 建議學生在 LeetCode 嘗試 `Sort an Array` (Quick Sort/Heap Sort/ Merge Sort) 並記錄執行時間 Encourage trying LeetCode "Sort an Array" with runtime notes.
- 發送簡短訊息提醒下次課前帶回 W02 學習單與任何疑問 Send reminder to bring worksheet and questions next session.
- 教師可整理本課觀察，為第三週設計「複雜度測驗」或「APCS 題目解析」 Prepare observations for Week 3 planning.

---

## 附錄 Appendix
- **參考資源 References**：
  - VisuAlgo Sorting: https://visualgo.net/en/sorting
  - APCS Python 常見題型整理（教師自備或外部連結）APCS Python topic bank (teacher curated)
- **關鍵詞對照 Glossary**：
  - 比較 comparison, 交換 swap, 插入 insertion, 堆 heap, Prim 演算法 Prim's algorithm
  - 時間複雜度 time complexity, 空間複雜度 space complexity, 演算法算法 algorithm, 巢狀迴圈 nested loop, 遞迴 recursion

Happy teaching! 祝教學順利！
