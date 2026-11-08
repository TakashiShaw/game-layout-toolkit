# Human playtest and resulting changes

## User observations (verbatim)

> yes it fits the browser very well, nothing seems cu off, the title is on the screen. where is the original for me to comapre it to

After comparison:

> i dont like how in the new one, the how to play box is half in the game and half not, and that the top of the screen isnt game but is website. in the oringal i font like all the extra space at the bottom, although its not a big deal. the original looks better overall just barily. the play now button is also larger which looks better in my opinion. to imrpove the new one, fix what i said. if extra space at the bottom is neded, that is better than using extra space at the top

## Changes made by Codex

- Anchored title art, office art and camera scene to the top.
- Moved How to play beside Start Night 1 inside the title menu; during gameplay it moves beside Pause and Menu at the bottom.
- Enlarged Start Night 1 to a 360px-wide desktop action with 22px text, adapting down for smaller screens.
- Kept spare space below the artwork rather than above it.
- Updated checker instructions so outer-shell coverage alone cannot establish visual integration.

## Actual follow-up checks

`checks.json` records eight viewport sizes, each with title, office and camera states. Visible button centers were reachable; targets were at least 44px in each dimension and inside the viewport. Scene top measured at 0px in office and camera states. Help close/resume, pause/resume, win and retry interactions completed. Screenshots are in this directory. These are Chromium emulation results. The user has not yet judged this latest revision.
