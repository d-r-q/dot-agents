---
name: choose-model
description: Choose an OpenAI model and reasoning_effort from GPT-5.4-Mini, GPT-5.2, GPT-5.3-Codex, GPT-5.4, and GPT-5.5 for a described task. Use when the user asks which model or reasoning level to use, or when configuring a subagent/delegated task where model and reasoning_effort can be selected.
---

# Choose Model

Ask one concise question if missing context can change the model or reasoning effort.
Otherwise choose directly.

Use priority profile: `balanced` by default, `speed` for fastest sufficient, `cost` for cheapest sufficient, `quality` for strongest suitable.
For `spawn_agent`, set `model` when different from inherited default and set `reasoning_effort` when non-default.
Use tool ids when configuring tools: `gpt-5.4-mini`, `gpt-5.2`, `gpt-5.3-codex`, `gpt-5.4`, `gpt-5.5`.

Return only:
- `model`
- `reasoning_effort`
- `why`: one or two sentences

## Models

- `GPT-5.4-Mini`: simple bounded tasks, low-risk edits, summaries, formatting, checks; best for speed/cost.
- `GPT-5.2`: broad professional or long-running non-specialized agent work.
- `GPT-5.3-Codex`: coding-heavy implementation, debugging, refactoring, tests, review, codebase navigation.
- `GPT-5.4`: stronger everyday coding/technical work when Mini is too weak and 5.5 is unnecessary.
- `GPT-5.5`: hardest ambiguous or high-impact architecture, research, multi-system debugging, and long reasoning.

Tie-break with the smallest model that satisfies the quality bar.
Prefer `GPT-5.3-Codex` when code is the main artifact.
Prefer `GPT-5.5` when ambiguity and failure cost are both high.

## Reasoning

- `low`: trivial, mechanical, lookup-style.
- `medium`: normal implementation, review, planning, professional work.
- `high`: complex debugging, architecture, multi-file changes, subtle correctness risk.
- `xhigh`: very hard, ambiguous, high-impact, deeply coupled work.

Defaults: `GPT-5.5` uses `xhigh`; all others use `medium`.
For `speed`, reduce one level when safe.
For `cost`, use the lowest likely sufficient effort.
For `quality`, raise one level for non-trivial tasks.
