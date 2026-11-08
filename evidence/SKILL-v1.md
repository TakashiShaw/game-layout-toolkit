---
name: game-layout-check
description: Review browser games for viewport-filling layout, preserved artwork proportions, integrated menus, and usable responsive controls. Use when a game feels embedded in a website or after responsive UI changes. Report only; do not fix files.
---
# Game layout check
Use a fresh reviewer context, separate from the agent that changed the game.
Read the user's layout requirements and call `inspect_game_layout` for the local game URL and game selector. Review the returned measurements and screenshots. If the tool is unavailable, state that limitation; do not invent measurements.

Check representative phone portrait/landscape, tablet portrait/landscape, laptop, and desktop viewports.
- The game shell fills the viewport without surrounding website chrome or document scrolling.
- Essential artwork keeps its proportions; decorative extensions or intentional letterboxing are acceptable. Do not demand stretching or cropping essential gameplay to maximize scene coverage.
- Instructions, navigation, settings, and status belong inside the game interface.
- Visible controls remain readable, inside the viewport, and usable by touch and mouse. Use 44 CSS pixels as this project's preferred touch-target size, not a claim of universal compliance.
- Inspect menu and gameplay separately. A menu pass cannot establish gameplay quality.

Report a table: viewport/state | PASS/FAIL/UNVERIFIED | issue | measured or visual evidence | suggested fix.
Distinguish measurement from interpretation. Name screenshot/report files and element selectors. State tested browser/viewport coverage and remaining uncertainties. Never claim all devices work from emulation alone.
Do not edit the game, implement suggestions, or claim the user agrees with your judgment.
