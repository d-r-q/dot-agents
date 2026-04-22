---
name: finding-codex-session
description: Find Codex session `.jsonl` files under `~/.codex/sessions/` and `~/.cache/JetBrains/IntelliJIdea*/aia/codex/sessions/` by text fragment, session id, date, or date range. Use when the user wants only matching session file paths.
---

# Finding Codex Session

Search only these roots and skip missing ones:
- `~/.codex/sessions/`
- `~/.cache/JetBrains/IntelliJIdea*/aia/codex/sessions/`

Ask only for missing search criteria. Accept any combination of:
- text fragment;
- session id;
- date `YYYY-MM-DD`;
- month `YYYY-MM`;
- date range `from` / `to` in `YYYY-MM-DD`.

Search only `.jsonl` session files. Prefer the narrowest filter first:
- session id: use exact fixed-string match; match the filename first; if needed, search file content for the id;
- date or month: restrict by dated path segments before content search;
- text: use fixed-string search with `rg -l -F`.

For date ranges, treat `from` and `to` as inclusive bounds.
Allow either bound to be omitted.
Intersect all provided filters.
Do not guess missing criteria.
Do not summarize file contents.

Return only absolute matching paths, one per line, sorted. If nothing matches, reply `No matching session files.`
