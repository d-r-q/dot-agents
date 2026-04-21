---
name: distilled-skill-creator
description: Interview the user to define or revise a skill without guessing, surface key design options with recommendations, then use the system `$skill-creator` and distill the resulting draft. Use when the user wants a new skill or a rewrite with an explicit interview-first workflow and stronger pressure toward laconic, high-signal instructions.
---

# Distilled Skill Creator

Read the system `$skill-creator`.
Assume it is an installation prerequisite for this wrapper.
Do not run it first.

Read `references/distillation.md` before writing or revising the final `SKILL.md`.
Apply it to that draft as a second-pass compression rule set, not as a replacement for `$skill-creator`.

## Required Order

Follow this order:
- interview the user to remove behavior-changing ambiguity;
- summarize the intended skill and extract unresolved key decisions;
- present concrete options for those decisions with tradeoffs and a recommendation;
- wait for the user's answers or approval;
- only then use `$skill-creator` to produce or update a complete working draft;
- distill that draft with `references/distillation.md`;
- compare the final `SKILL.md` against the pre-distillation draft.

## No-Assumption Rule

Do not infer missing requirements when they can change the resulting skill.
If scope, triggers, examples, output artifacts, file layout, tools, validation, placement, prohibitions, or decision rules are unclear and the choice matters, ask.
Do not convert silence into approval.
If the user wants you to choose, first show the viable options and your recommendation, then proceed only after explicit approval.

## Interview Rule

Start with an interview, not implementation.
Ask only the highest-value questions first and keep each batch small.
Prefer concrete questions that pin down:
- what requests should trigger the skill;
- representative user examples;
- required outputs or edited files;
- required tools, resources, and constraints;
- target location and update scope;
- validation expectations;
- hard prohibitions or non-goals.
Continue until the remaining gaps are either non-material or explicitly captured as decisions for the next step.

## Decision Review

After the interview, summarize the target skill briefly and list the unresolved key decisions.
For each decision:
- give 2-3 viable options;
- state the main tradeoff in one line;
- mark one recommendation when appropriate;
- ask the user to choose or approve.
Do not hide this step inside implementation.
Do not start `$skill-creator` while any unresolved behavior-changing decision remains.

## Composition Rule

Keep the base workflow and validation discipline from `$skill-creator`.
Treat this skill as a composite workflow:
- interview first;
- resolve key decisions with the user;
- produce or update a complete working draft with `$skill-creator`;
- distill that draft with `references/distillation.md`;
- compare the final `SKILL.md` against that draft, not against a hypothetical baseline.
Use the distillation reference only to compress wording and remove redundant material.
Do not copy large parts of `$skill-creator` into the produced skill unless the user explicitly asks for that.

## Compression Boundary

Prefer shorter instructions by default.
Keep any line whose removal would likely cause:
- wrong skill triggering;
- wrong output format;
- wrong tool or resource choice;
- wrong execution order;
- skipped validation;
- unsafe guessing;
- loss of a hard constraint, stop condition, or decision rule.

Remove repetition, motivation, soft preferences, and examples that do not carry unique rules.
Prefer referencing reusable resources over inlining long guidance.
Prefer delta instructions over restating baseline behavior that another skill already defines.

## Frontmatter Rule

Keep `name` and `description` precise.
Do not over-compress the description if that would weaken triggering accuracy.
Preserve concrete "use when" conditions in the description even when the body is highly compressed.

## Wrapper Pattern

When creating a wrapper around another skill:
- identify the base skill and state that it must be read first;
- place wrapper-specific interview and decision steps before the base skill runs when they affect the resulting artifact;
- add only the extra constraints, preferences, or domain deltas introduced by the wrapper;
- keep the wrapper self-contained for its added behavior;
- bundle external prompts or rules into `references/` when they are required at runtime.

## Before Finishing

Check that the final `SKILL.md` is shorter than the draft produced before distillation.
Check that the final skill reflects only user-provided or explicitly approved decisions.
Check that the skill still contains all behavior-changing constraints, decision rules, and validation steps needed to succeed.
If brevity and reliability conflict, keep the smallest wording that still preserves reliable execution.
