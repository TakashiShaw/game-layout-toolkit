# Native MCP call excerpts — factual AI-prepared index

These are trimmed from actual JSONL logs. The student should explain them in their own demonstration write-up.

## native-mcp-first-attempt.jsonl
```json
{
  "server": "game-layout",
  "tool": "inspect_game_layout",
  "arguments": {
    "url": "http://127.0.0.1:8138/?dev=1&manual=1",
    "game_selector": "#game",
    "clicks": [
      "#start",
      "#monitor-toggle"
    ]
  },
  "status": "failed",
  "error": {
    "message": "MCP tool call requires approval, but approval policy is never"
  }
}
```

## native-mcp-transcript.jsonl
```json
{
  "server": "game-layout",
  "tool": "inspect_game_layout",
  "arguments": {
    "url": "http://127.0.0.1:8138/?dev=1&manual=1",
    "game_selector": "#game",
    "clicks": [
      "#start",
      "#monitor-toggle"
    ]
  },
  "status": "completed",
  "error": null,
  "resultKeys": [
    "content",
    "structured_content"
  ],
  "savedReport": "evidence/44f93e024054/report.json",
  "viewports": [
    {
      "name": "phone-portrait",
      "coverage": 100,
      "error": null
    },
    {
      "name": "phone-landscape",
      "coverage": 100,
      "error": null
    },
    {
      "name": "tablet-portrait",
      "coverage": 100,
      "error": null
    },
    {
      "name": "tablet-landscape",
      "coverage": 100,
      "error": null
    },
    {
      "name": "laptop",
      "coverage": 100,
      "error": null
    },
    {
      "name": "desktop",
      "coverage": 100,
      "error": null
    }
  ]
}
```

## native-mcp-rerun-transcript.jsonl
```json
{
  "server": "game-layout",
  "tool": "inspect_game_layout",
  "arguments": {
    "url": "http://127.0.0.1:8138/?dev=1&manual=1",
    "game_selector": "#game",
    "clicks": [
      "#help-open"
    ]
  },
  "status": "completed",
  "error": null,
  "resultKeys": [
    "content",
    "structured_content"
  ],
  "savedReport": "evidence/54c834a55405/report.json",
  "viewports": [
    {
      "name": "phone-portrait",
      "coverage": 100,
      "error": null
    },
    {
      "name": "phone-landscape",
      "coverage": 100,
      "error": null
    },
    {
      "name": "tablet-portrait",
      "coverage": 100,
      "error": null
    },
    {
      "name": "tablet-landscape",
      "coverage": 100,
      "error": null
    },
    {
      "name": "laptop",
      "coverage": 100,
      "error": null
    },
    {
      "name": "desktop",
      "coverage": 100,
      "error": null
    }
  ]
}
```
