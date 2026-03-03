# COMMIT_CONVENTION.md — Commit 與分支命名規範

本文件用於團隊統一版本紀錄風格，並作為 PR Review 的檢核依據。

---

## 1) 分支命名
- `feature/<short-desc>`：新功能
- `fix/<short-desc>`：修 bug
- `chore/<short-desc>`：雜務（依賴更新、設定調整）
- `refactor/<short-desc>`：重構（不改功能）

建議 `<short-desc>`：
- 全小寫、用 `-` 分隔（kebab-case）
- 例：`feature/add-login`, `fix/null-pointer`, `chore/bump-deps`

---

## 2) Commit Message（Conventional Commits）
格式：`<type>(<scope>): <subject>`

### type
- `feat`：新增功能
- `fix`：修 bug
- `docs`：文件
- `test`：測試
- `refactor`：重構（不改功能）
- `perf`：效能改善
- `chore`：雜務（依賴、設定、格式化）
- `ci`：CI/CD
- `build`：建置系統/打包

### scope
- 建議用模組/資料夾名（例如 `api`, `ui`, `db`, `pipeline`, `infra`）
- 若 scope 不明確可省略：`fix: ...`

### subject
- 英文動詞開頭（Add/Improve/Fix/Refactor）
- 50 字內
- 不要句號
- 盡量描述「結果」而非「過程」

### 範例
- `feat(api): add txn validation endpoint`
- `fix(ui): handle empty state in dashboard`
- `refactor(db): extract query builder`
- `chore(deps): bump dependencies`

---

## 3) 一次 commit 只做一件事（原則）
✅ 好：  
- 「修掉一個 bug」或「新增一個 endpoint」或「補一組測試」

❌ 不好：  
- 同時「改功能 + 大重構 + 依賴更新 + 格式化全 repo」

---

## 4) PR 合併策略建議
- 預設：**Squash merge**（讓 main 歷史乾淨，適合 feature 分支多次 commit 的情況）
- 若你們重視完整歷史：Merge commit 也可，但請一致。

（依團隊習慣修改）
