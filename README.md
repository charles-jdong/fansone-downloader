# Claude + GitHub Template

給 **VS Code Claude 擴充 + GitHub Desktop** 工作流設計的專案範本。
用 GitHub 的「Use this template」建立新 repo，即可套用所有規範與模板。

---

## 包含什麼

| 檔案 / 資料夾 | 用途 |
|---|---|
| `CLAUDE.md` | Claude 協作規範（工作原則、PR/Commit 規範、安全規則、輸出格式） |
| `COMMIT_CONVENTION.md` | 分支命名 + Conventional Commits 詳細規範 |
| `SECURITY.md` | 安全政策（禁止提交 secrets、回報方式） |
| `.github/pull_request_template.md` | PR 描述模板（What/Why/How to test/Risk） |
| `.github/ISSUE_TEMPLATE/bug_report.md` | Bug 回報模板 |
| `.github/ISSUE_TEMPLATE/feature_request.md` | 功能建議模板 |
| `.gitignore` | 常見忽略規則（OS、IDE、Node、Python、.env） |
| `.env.example` | 環境變數範本 |

---

## 使用方式

### 1. 建立新 repo
點擊 **Use this template** → 填入 repo 名稱 → Create repository

### 2. 填寫專案資訊
打開 `CLAUDE.md` 最後一段「專案專屬資訊」，補上你的：
- 技術棧
- 安裝 / Lint / Test / Build 指令
- 禁止/限制事項

### 3. 開始開發
1. 從 `main` 開新分支（`feature/xxx`、`fix/xxx`）
2. 用 VS Code + Claude 開發
3. Commit / Push 用 GitHub Desktop
4. 開 PR（GitHub Desktop 會開瀏覽器），內容依模板填寫

---

## Claude 常用提示詞

### 產 commit message
> 請根據我目前的變更，給我 3 個符合 Conventional Commits 的 commit message 選項（含 scope），並用一句話說明每個選項適用情境。

### 產 PR 描述
> 請用 CLAUDE.md 的 PR 格式，產出可直接貼到 GitHub 的 PR 描述（What/Why/How to test/Risk）。

### 自我 review
> 請 review 我這次改動，列出 High/Medium/Low 風險與具體建議修正，並附上我應該補的測試/手動驗證清單。
