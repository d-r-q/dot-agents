---
name: notifying-on-completion
description: Use when the user asks to be notified on completion, for example "напиши как закончишь".
---

# Notifying On Completion

Use when the user asks to be notified on completion, for example: `напиши как закончишь`.

After the work is done and after the final chat message, send one notification:

```bash
notify-send -u critical -- "$TASK_TITLE" "Done!"
```
