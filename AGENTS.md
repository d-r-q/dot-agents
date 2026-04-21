# General agents instructions

- Read machine-specific instructions at ~/.codex/AGENTS.local.md
- If the user message is a question (ends with ? or is clearly interrogative), answer it only.
  Do not create, modify, or stage any files in this case.
- Chat answers must be at least 2x shorter than your natural default.

Output template:
- Normal message: `<Role>: <body>`
- Message starting with ```, `<tag>` block or list item:
  `<Role>:`
  `<body>`

## Working with git

- Immediately stage all newly created files in `src` directories with `git add <path>`.
- Before sending the final response, run git status --short and verify that all **newly created** files are staged.

## Executing commands

- MUST: every `exec_command` call must set `shell: "bash"`.
- SHOULD NOT: wrap cmd with `bash -lc`;
  pass plain command in cmd (avoid nested shells).
- MUST: command text must be bash-compatible; do not use zsh syntax/features.
- If tool output shows `Command: /usr/bin/zsh -lc`, treat it as violation and immediately rerun with `shell: "bash"`.
- In run Gradle commands use set environment variable `GRADLE_USER_HOME=./.gradle-user-home`
