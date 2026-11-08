# Demonstration

I tested the toolkit on a copy of my FNAF remake and compared it with the original. The development agent made changes, while separate checker sessions reviewed the results. The [baseline checks](evidence/before-menu-mcp.json) found that the game filled only about 26% of a portrait-phone window, with very small Start text. The [independent checker](evidence/review-before.md) also found UI outside the game and scrolling at some sizes.

After the first revision, a fresh Codex session made this actual MCP call to inspect the cameras:

```json
{"tool":"inspect_game_layout","arguments":{"url":"http://127.0.0.1:8138/?dev=1&manual=1","game_selector":"#game","clicks":["#start","#monitor-toggle"]},"status":"completed"}
```

The outside game container filled all six tested sizes, but the tool response was too large and some results were cut off. After shortening the response and updating the checker, another fresh session inspected the instructions:

```json
{"tool":"inspect_game_layout","arguments":{"url":"http://127.0.0.1:8138/?dev=1&manual=1","game_selector":"#game","clicks":["#help-open"]},"status":"completed"}
```

The [second reviewer](evidence/native-mcp-rerun-review.md) opened screenshots and caught instructions text that was only 8 pixels. This was enlarged, and [follow-up tests](evidence/final-dialog-checks.json) verified scrolling and closing/resuming. Both runs are preserved in the [transcript excerpts](evidence/native-tool-excerpts.md).

At first I thought the new game fit well, but after comparing it with the original, I slightly preferred the original. Empty space had moved around, How to play looked partly outside the game, and Start looked smaller. I agreed with checking borders and layout, but filling the browser alone did not make it look better. I clarified that extra space should go below the artwork and that the buttons should stay inside the game.

The next version put the artwork at the top, moved How to play beside the other game actions, and enlarged Start. I said, “i really like how that looks.” My [feedback](evidence/user-feedback/PLAYTEST.md), [eight-size layout checks](evidence/user-feedback/checks.json), and [38/38 passing game tests](evidence/game-regression.txt) are saved. Those results do not prove every browser or physical device works.
