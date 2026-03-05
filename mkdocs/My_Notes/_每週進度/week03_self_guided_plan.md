# 第三週自學教案 W03 Self-Guided Plan

> 本週教師請假，請學生善用新 MacBook Air，依照指引完成環境建置與程式實作。建議全程使用 Jupyter Notebook 紀錄操作與心得，方便下週回報進度。

## 課程核心目標
- 在個人電腦完成 Python 與開發環境建置，並記錄設定流程。
- 熟悉 VS Code 與 Jupyter Notebook 的協同使用，能夠建立並執行 `.ipynb` 檔案。
- 撰寫一個具有適當難度的 Python 腳本（CLI 或 Notebook 皆可），並以 Notebook 說明設計思路、測試結果與反思。
- 將成果整理成可分享的檔案或 Git 版本庫，作為下週討論基礎。

## 自主學習流程

### 1. 環境整備（預計 40 分鐘）
- **macOS 基本設定**：
  - 確認系統已更新（` → 系統設定 → 一般 → 軟體更新`）。
  - 開啟「系統設定 → 隱私權與安全性 → 開發者工具」，允許 VS Code 或其他 IDE 後續取得權限。
- **開發工具安裝**：
  1. 開啟 Terminal，安裝 Command Line Tools：`xcode-select --install`。
  2. 安裝 Homebrew（若尚未安裝），並執行 `brew doctor` 檢查狀態。
  3. 使用 Homebrew 安裝 Python 與 Git：`brew install python git`。
  4. 安裝 VS Code（或確保新版已就緒），並加入 Python、Jupyter 相關擴充套件。
- **虛擬環境與套件**：
  - 在個人專案資料夾建立目錄 `apcs_week03`，使用 `python3 -m venv .venv` 建立虛擬環境。
  - 啟動虛擬環境後，安裝必備套件：`pip install --upgrade pip jupyter ipykernel`。
  - 為 Notebook 建立 Kernel：`python -m ipykernel install --user --name apcs-w03`。
- **紀錄**：在 Notebook 的第一個 Markdown Cell 撰寫環境檢查清單，包含版本號與安裝過程心得。

### 2. Notebook 暖身與測試（預計 20 分鐘）
- 在 VS Code 中啟動 `apcs_week03/week03_environment_check.ipynb`，選擇剛建立的 Kernel。
- 建議 Notebook 架構：
  1. **Markdown**：當日目標、硬體／軟體版本。
  2. **Code**：輸入下列測試片段，確認執行無誤：
     ```python
     import platform, sys, math
     print("Hello, APCS!")
     print("macOS:", platform.mac_ver()[0])
     print("Python:", sys.version.split()[0])
     print("浮點測試:", math.sqrt(2) ** 2)
     ```
  3. **Markdown**：簡述常見錯誤（例如 pip 權限、Kernel 找不到）與對應解法。
- 遇到問題時，請截圖或將錯誤訊息貼在 Notebook 中，方便下週追蹤。

### 3. 主題實作任務（預計 60 分鐘）
目標：撰寫具實用性或演算法性質的 Python 腳本，建議使用 Notebook 記錄開發過程。

- **題材建議（擇一或綜合）**：
  - 建立 CLI 工具，讀取使用者輸入的數列並輸出統計資料（最大值、平均、標準差），再以 Notebook 比對多組測試資料。
  - 實作「氣泡排序 + 交換計數」或「插入排序 + 步驟計數」函式，並在 Notebook 中用圖表呈現 `n` 與步驟數關係。
  - 撰寫簡易檔案整理腳本：掃描資料夾，依副檔名分類至新資料夾，於 Notebook 中展示前後結構差異（可使用 `os` 與 `shutil`）。
- **建議流程**：
  1. 在 Notebook 中撰寫需求分析與測試案例。
  2. 於 Code Cell 中開發並逐步驗證函式或主程式。
  3. 透過 `if __name__ == "__main__":` 模式（若為 `.py` 腳本）或專用測試 Cell（若為 Notebook）執行多組測試。
  4. 以 Markdown 總結成果、紀錄尚未解決的問題。
- **進階延伸**：嘗試將 Notebook 匯出為 `.py`（`File → Export Notebook As`），確認腳本在 Terminal 直接執行仍可得到預期結果。

### 4. 成果整理與回報（預計 15 分鐘）
- 建立 `README.md` 或 Notebook 尾端總結段落，包含：
  - 完成項目列表。
  - 遇到的問題與解決方式。
  - 下週希望討論或協助的主題。
- 將 `apcs_week03` 資料夾整理如下：
  - `week03_environment_check.ipynb`
  - 實作腳本或 Notebook（例如 `sorting_lab.ipynb`、`stats_tool.py`）
  - `README.md`（或 Notebook 最後一節）
  - 額外素材（若有）：測試資料、截圖、外部參考連結。
- 建議將資料夾壓縮後上傳至指定雲端，或同步至個人 GitHub（若已設定）。

## 自主練習建議
- 嘗試在 Notebook 中新增簡易圖表（`matplotlib` 或 `seaborn`），視覺化排序步驟或統計結果。
- 練習使用 `pytest` 或 `unittest` 撰寫一至兩個測試案例，確保核心函式可重複驗證。
- 探索 VS Code 「Notebook diff」功能，了解如何比對不同版本的 `.ipynb`。

## 注意事項
- 開發過程請定期儲存並同步至雲端，避免新電腦資料遺失。
- 若遇到網路受限或權限問題，可先記錄錯誤訊息，週四以前寄信給老師或助教尋求協助。
- 完成後務必留存 Notebook 與環境設定紀錄，作為下週實體課程起點。
