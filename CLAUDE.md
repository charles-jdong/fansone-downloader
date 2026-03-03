# CLAUDE.md — 專案協作規範（請先讀再回覆/改碼）

> 你是此 repo 的協作助理。請在回答、生成程式碼、建議修改前，**先遵守本文件規範**。
> 目標：提升一致性、可維護性、安全性；避免不必要的大改與失控變更。

---

## 0) 工作原則（最重要）
1. **最小可行改動**：能用小 patch 解決就不要大重構。
2. **先說明後動手**：除非我說「直接改」，否則先列：
   - 要改哪些檔案
   - 每個檔案要改什麼
   - 風險與回滾方式
3. **小步提交**：每個 commit 只做一件事（利於回溯/Review）。
4. **不確定就給選項**：需求不清時，先給 2–3 個方案與取捨，不要猜。
5. **避免破壞性變更**：牽涉到 public API/DB schema/介面行為變更，必須在 PR 的 Risk 區說清楚。

---

## 1) Repo 結構
- `src/` — 主要程式碼
  - `downloader.py` — 主下載邏輯（yt-dlp 整合）
  - `auth.py` — 認證 / cookie 處理
  - `extractor.py` — 影片串流 URL 擷取
- `tests/` — 測試
- `downloads/` — 下載輸出（已加入 .gitignore）
- `.env.example` — 環境變數範本
- `.github/` — PR/Issue 模板

---

## 2) 分支與 Commit 規範

> 詳細規範請見 [`COMMIT_CONVENTION.md`](COMMIT_CONVENTION.md)。以下為摘要：

- 主分支：`main`
- 分支命名：`feature/`、`fix/`、`chore/`、`refactor/` + kebab-case 描述
- Commit 格式：`<type>(<scope>): <subject>`（Conventional Commits）
  - type: `feat` / `fix` / `docs` / `test` / `refactor` / `perf` / `chore` / `ci` / `build`
  - scope: 模組或資料夾名（可省略）
  - subject: 英文動詞開頭、50 字內、不加句號
- 一次 commit 只做一件事
- PR 合併策略：**Squash merge**

---

## 3) PR 描述規範（請嚴格遵守）

> PR 模板位於 [`.github/pull_request_template.md`](.github/pull_request_template.md)，請依模板填寫。

必須包含：
1. **What**：做了什麼（3–6 點條列）
2. **Why**：為什麼要做（背景/問題）
3. **How to test**：怎麼測（指令 + 手動測項）
4. **Risk & Rollback**：可能風險與回滾方式
5. **Screenshots**（有 UI 變更才需要）

---

## 4) 安全（特別重要）
- **禁止提交**：cookies、session tokens、帳號密碼、私人 URL
- `.env` 中存放 FANSONE_EMAIL / FANSONE_PASSWORD，絕對不能 commit
- `.cookies.json`（auth 快取）已加入 .gitignore
- 下載的影片檔案（.mp4/.ts/.mkv）已加入 .gitignore

---

## 5) 測試與品質
- `python -m venv .venv && source .venv/bin/activate`
- `pip install -r requirements.txt`
- `pytest`（若有）
- `ruff check .`（若有）

---

## 7) 專案專屬資訊
- 技術棧：Python 3.11+、yt-dlp、requests、browser-cookie3、rich
- 安裝指令：`pip install -r requirements.txt`
- Lint 指令：`ruff check .`
- Test 指令：`pytest`
- Run 指令：`python main.py <url>`
- 禁止事項：不得提交真實 cookies 或帳密；下載的影片不得 commit
