


# APCS 輔導陪伴課程

## 專案簡介
本專案紀錄 APCS 輔導陪伴課程的設計與執行。目標是協助學生逐步建立演算法思維、程式設計基礎，以及應付 APCS 考試的能力。

## 課程理念
- 語言是工具，演算法思維才是核心。
- 以「帶著問題學習」為導向。
- 漸進式：中文教材起步 → 雙語材料過渡 → 英文原文強化。
- 遊戲化活動與實作並行，增加參與感。

## 教學步驟
1. **課堂**：以圖書館探索、排序演算法體驗為主，強調動手模擬與思考。
2. **課間任務**：安排小作業，培養自主探索與練習習慣。
3. **銜接 APCS**：逐步引導從演算法思維過渡到 Python 語法，再對應 APCS 歷屆試題。

## 資源連結
- [APCS 題型介紹](https://apcs.csie.ntnu.edu.tw/index.php/questionstypes/websites/)
- [APCS 歷屆試題](https://apcs.csie.ntnu.edu.tw/index.php/questionstypes/previousexam/)
- [Python 101 HackMD](https://hackmd.io/@arthurzllu/python101)

## 待辦事項
- [ ] 設計排序演算法教案（卡片操作、比較表）
- [ ] 準備課間小任務清單
- [ ] 匯總 APCS 歷屆題與當前課程內容的對應表


## Mkdocs

- docker compose up
- http://127.0.0.1:11421

## Jupyter

- 服務埠：`127.0.0.1:11414`
- 一鍵：`bash scripts/jupyter_url.sh`
- 直接啟動：`docker compose up -d jupyter && echo "http://127.0.0.1:11422/lab"`

---