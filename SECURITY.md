# SECURITY.md — 安全政策（簡版）

## 回報安全問題
若你發現任何可能的安全漏洞（例如：金鑰洩漏、權限繞過、注入風險），請不要直接開公開 Issue。
建議以私下方式回報給維護者（例如 email / 私訊）。

## 基本原則
- 不要在 repo 中提交任何 secrets（API keys/tokens/password/cookies）。
- 使用 `.env` + `.env.example` 管理環境變數。
- 優先啟用 GitHub 的 Secret scanning / Dependabot（若適用）。

（依團隊實際聯絡方式補上）
