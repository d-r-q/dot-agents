# General agents instructions

- Read machine-specific instructions at ~/.codex/AGENTS.local.md
- If the user message is a question (ends with ? or is clearly interrogative), answer it only.
  Do not create, modify, or stage any files in this case.
- If the user request is about code design, answer it only.
  Do not modify code files in this case.
- Chat answers must be at least 2x shorter than your natural default.

Output template:
- Normal message: `<Role>: <body>`
- Message starting with ```, `<tag>` block or list item:
  `<Role>:`
  `<body>`

## Executing commands

- MUST: every `exec_command` call must set `shell: "bash"`.
- SHOULD NOT: wrap cmd with `bash -lc`;
  pass plain command in cmd (avoid nested shells).
- MUST: command text must be bash-compatible; do not use zsh syntax/features.
- If tool output shows `Command: /usr/bin/zsh -lc`, treat it as violation and immediately rerun with `shell: "bash"`.
- In run Gradle commands use set environment variable `GRADLE_USER_HOME=./.gradle-user-home`

## Efficient evidence collection

- Before tool use, identify the decision to make and retrieve only facts that can affect it.
- Prefer narrow, explicit paths and filtered output; do not run broad recursive searches from `.` when a concrete path is known.
- For API, Kubernetes, and logs, return only decision-relevant fields, aggregates, and a few safe samples.
- Reuse verified immutable facts within the task; re-fetch only external state that may have changed.
- If a command returns unexpected, oversized, or schema-incompatible output, stop and issue one narrower contract-aligned request instead of retrying broadly.
