# Iteration

My first instructions were to remove white borders, fill the browser, and keep the interface inside the game. The measurements improved, but I still slightly preferred the original. The empty space had moved above the artwork, How to play looked partly outside the game, and Start was smaller than I wanted.

The problem was that the outside container could fill 100% of the browser while the actual game still looked wrong. My instructions had not explained where necessary empty space should go. I clarified that it should be below the artwork, that text and controls should stay fully inside their area, and that I preferred a larger Start button.

The artwork was moved to the top, How to play went under Start in the menu and beside Pause/Menu during gameplay, and Start was enlarged. The checker was updated to inspect the actual scene rather than just container coverage. The [first skill](evidence/SKILL-v1.md) and [current skill](skills/game-layout-check/SKILL.md) show the revision. The checker reports problems; a separate development agent fixes them.

The [rerun](evidence/user-feedback/checks.json) checked eight window sizes without button-size, boundary, or center-hit failures in the title, office, and camera states. All [38 game regression tests](evidence/game-regression.txt) passed. I looked at the result and said I really liked it, unlike my first comparison. My exact [feedback is saved](evidence/user-feedback/PLAYTEST.md).

There was also a toolkit failure: the first MCP response was too large and the reviewer reported cut-off results. The server now returns a shorter summary and saves full measurements separately. The skill also requires opening screenshots. The [second native review](evidence/native-mcp-rerun-review.md) completed and caught small instructions text, which was then fixed and tested. The [older server](evidence/server-v1.py) is preserved. These explanations were edited with Codex from my rough writing and feedback, as disclosed in the README.
