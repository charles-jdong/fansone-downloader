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

## 1) Repo 結構（可依專案調整）
- `src/`：主要程式碼（若有）
- `tests/`：測試（若有）
- `scripts/`：維運/一次性工具
- `docs/`：文件
- `.env.example`：環境變數範本（禁止提交真實 `.env`）
- `.github/`：PR/Issue 模板、CI 等

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
- 若你發現更適合的 scope/type，請提出建議，但不要擅自改整個 repo 的 commit 風格
- PR 合併策略：預設 **Squash merge**

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

## 4) 測試與品質（依專案選用）
請在回答/建議中，優先提醒以下檢查項：

### Node / Next.js
- `npm ci` 或 `pnpm i`
- `npm run lint`
- `npm test`（若有）
- `npm run build`

### Python
- `python -m venv .venv && source .venv/bin/activate`
- `pip install -r requirements.txt`
- `pytest`（若有）
- `ruff check .`（若有）
- `mypy .`（若有）

> 若專案已定義 Makefile / Taskfile / scripts，請以專案既有指令為主。

---

## 5) 安全與機敏資訊（禁止事項）
- **禁止提交**：API keys、tokens、password、cookies、憑證、私人 URL、內網 IP、客戶資料。
- 若偵測到疑似機敏資訊：
  1) 立即提醒我
  2) 建議移到 `.env` / Secret Manager
  3) 補上 `.gitignore` 與 `.env.example`

---

## 6) Claude 輸出格式偏好（務必遵守）
- **要我貼到 GitHub Desktop**：直接輸出：
  - `Commit message`（1 行）
  - `PR 描述`（可整段貼上，含標題/段落）
- **要 review**：輸出：
  - High / Medium / Low 風險清單
  - 具體建議修正（最好能指出檔案/函式）
  - 測試/手動驗證清單

---

## 7) 專案專屬資訊（請依專案填寫）
- 技術棧：
- 安裝指令：
- Lint 指令：
- Test 指令：
- Build/Run 指令：
- 禁止/限制事項（例如：不得更動資料表、不得改 lockfile、需向下相容）：
