# Setup and technical reference (AI-authored)

This is supporting material for the student's own README, not a completed student reflection.

## What is included

- `skills/game-layout-check/SKILL.md`: a report-only checker for viewport filling, art proportions, integrated UI and usable controls.
- `server.py`: one local stdio MCP tool, `inspect_game_layout`.
- `call_tool.py`: reproducible MCP protocol client, including tool discovery and saved requests/responses.
- `evidence/`: actual baseline, revised and independent review records. Do not describe an untested device as verified.

The tool creates a fresh Chromium context for each of six sizes: 390×844, 844×390, 768×1024, 1024×768, 1366×768 and 1920×1080. It can click supplied CSS selectors to reach a state. It measures the game shell, document overflow, controls and image fitting, and saves screenshots. Requests and subresources are restricted to loopback HTTP. Run it only against your own disposable local game. No account or API key is required.

## Install on another computer

Python 3.11+ is recommended; this build was tested using Python 3.14 on macOS ARM64.

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m playwright install chromium
```

On Windows use `.venv\Scripts\python.exe` instead. Windows execution has not been verified.

Copy the `game-layout-check` folder into `~/.codex/skills/` for personal reuse, or your project's `.agents/skills/` for project-scoped discovery. Restart/open a new client session after installation.

Register using **your own absolute paths**:

```sh
codex mcp add game-layout -- /ABSOLUTE/PATH/TO/.venv/bin/python /ABSOLUTE/PATH/TO/server.py
codex mcp get game-layout --json
```

Equivalent configuration (replace both placeholders):

```toml
[mcp_servers.game-layout]
command = "/ABSOLUTE/PATH/TO/.venv/bin/python"
args = ["/ABSOLUTE/PATH/TO/server.py"]
```

If you installed browser binaries in a nondefault directory, add `PLAYWRIGHT_BROWSERS_PATH` to the server's environment. `GAME_LAYOUT_OUTPUT` optionally selects an evidence directory; the default is `evidence/` beside the server.

## Use

Serve the game folder locally:

```sh
python3 -m http.server 8138 --bind 127.0.0.1 --directory /ABSOLUTE/PATH/TO/GAME
```

In a new checker session, ask:

> Use $game-layout-check to inspect http://127.0.0.1:8138/. The game shell is #game. Inspect the title and gameplay, using #start to start. Report only, with screenshot evidence. Do not fix files.

Use the actual selectors for other games. A separate development agent can then act on the report.

Protocol smoke test for this FNAF demo:

```sh
.venv/bin/python call_tool.py menu
.venv/bin/python call_tool.py gameplay '#start'
.venv/bin/python call_tool.py cameras '#start' '#monitor-toggle'
```

`call_tool.py` defaults to the FNAF development URL on port 8138; set `GAME_URL` to test another URL. It verifies that exactly one tool is exposed and records the actual MCP request/response. This protocol test is distinct from a native agent invocation, which is recorded separately in `evidence/native-mcp-transcript.jsonl`.

## Sources and AI use

Implementation and technical notes were produced with Codex using the student's stated preferences and actual HW7 messages. The skill follows the bundled skill-creator guidance; the server uses the official MCP Python SDK and Playwright. No third-party downloadable skill was copied.

- https://github.com/modelcontextprotocol/python-sdk
- https://playwright.dev/python/docs/library
- https://learn.chatgpt.com/docs/build-skills
- https://learn.chatgpt.com/docs/developer-commands?surface=cli
- https://www.cs.cmu.edu/~113/hw8.html

The current SDK is pinned to 2.3.0. The assignment's FastMCP import did not work with this SDK; the implementation uses its MCPServer API instead. Full personal reflections and agreement with reviewer judgments must come from the student.
