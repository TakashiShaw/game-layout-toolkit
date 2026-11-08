# Game Layout Toolkit

[Demonstration](DEMONSTRATION.md) · [Iteration](ITERATION.md) · [Evidence notes](PUBLIC_EVIDENCE.md)

I was tired of constantly fixing web app games so they looked like games instead of games inside a website. This happened with my interactive portfolio and FNAF remake. In my October 29 HW7 chat, I wrote, “i dont like how little the game takes up on the website. please make it larger on the website” and later, “can you ger rid of the white outline outside of the game.” The [full messages](evidence/source-quotes.md) show the repeated instructions behind this toolkit.

My `game-layout-check` skill reviews the UI without changing files. It should run when a game looks embedded in a website or after layout changes. It checks borders, unused space, artwork proportions, readable controls, and whether titles and instructions stay inside the game. I clarified that necessary extra space should go below the artwork, not above it. The report gives PASS/FAIL/UNVERIFIED, evidence, and suggested fixes. A separate development agent makes changes.

The MCP tool, `inspect_game_layout`, supplies actual browser screenshots and measurements. It checks six phone/tablet/desktop window sizes, including game coverage, scrolling, and control sizes. The skill gives instructions; the tool gives it browser evidence. Both were used in fresh Codex CLI sessions on macOS with Python 3.14 and Chromium. These were simulated screen sizes, not every physical device.

To install, run this from the repository folder:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m playwright install chromium
```

Copy `skills/game-layout-check/` into `~/.codex/skills/game-layout-check/`, then open a new Codex session. Register the server using your own absolute paths:

```sh
codex mcp add game-layout -- /ABSOLUTE/PATH/TO/.venv/bin/python /ABSOLUTE/PATH/TO/server.py
```

Serve your game, replacing its folder path:

```sh
python3 -m http.server 8138 --bind 127.0.0.1 --directory /ABSOLUTE/PATH/TO/GAME
```

Ask a fresh session to use `$game-layout-check` on `http://127.0.0.1:8138/`, giving the game selector and buttons needed to reach gameplay. For FNAF these are `#game` and `#start`. More configuration details are in [SETUP.md](SETUP.md).

I supplied the idea, preferences, playtest feedback, and rough writing. Codex helped build and test the toolkit, revise the game, and edit these documents with technical details. The skill used bundled skill-creator guidance; no downloaded third-party skill was copied. Technical sources were the [MCP SDK](https://github.com/modelcontextprotocol/python-sdk), [Playwright](https://playwright.dev/python/docs/library), [skill docs](https://learn.chatgpt.com/docs/build-skills), and [Codex command docs](https://learn.chatgpt.com/docs/developer-commands?surface=cli).
