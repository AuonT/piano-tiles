# Piano Tiles 🎹

CHE 120 group project: a Piano Tiles game in Python with **pygame**, played with the **arrow keys** instead of the mouse.

We're following pyGuru's [Piano Tiles Clone with pygame](https://www.youtube.com/playlist?list=PLHlrXTRZkTLDIT7mEYUcwzOXHFR47EIpN) playlist (6 parts). His version uses mouse clicks; ours swaps every click for a key press.

## Team

| Name | Initials | GitHub | Part |
|---|---|---|---|
| Darius Malich | DM | [dmalich6-byte](https://github.com/dmalich6-byte) | Window and screens |
| Auon Tippu | AT | [AuonT](https://github.com/AuonT) | Tiles |
| Gurmanpal Banwait | GB | [gurmy-b](https://github.com/gurmy-b) | Arrow keys and score |
| Harmanpal Banwait | HB | [hbanwait120](https://github.com/hbanwait120) | Sound and effects |

## Controls

| Key | Action |
|---|---|
| ← | Hit a tile in column 1 |
| ↓ | Hit a tile in column 2 |
| ↑ | Hit a tile in column 3 |
| → | Hit a tile in column 4 |
| SPACE | Start the game (replaces his Start button) |
| R | Replay after game over (replaces his Replay button) |
| M | Sound on/off (replaces his Sound button) |
| ESC / Q | Quit |

## Getting started

1. Install Python 3.10+ and then pygame-ce: `pip install pygame-ce` (works on Python 3.10 to 3.15; the code still says `import pygame`)
2. Clone the repo: `git clone https://github.com/AuonT/piano-tiles.git`
3. Run the game: `python main.py`

## File structure

| File / folder | What goes in it |
|---|---|
| `main.py` | Everything: settings, classes (`Tile`, `Text`, `Counter`, `Square`), functions and the game loop, in one labelled section per person |
| `notes.json` | Lists of piano notes for each song |
| `Assets/` | Images (background, piano, title, red overlay) |
| `Sounds/` | Piano note `.ogg` files, buzzer, background music |
| `Fonts/` | Fonts for score and titles |

The images, sounds, fonts and `notes.json` come from the tutorial's [source code folder](https://github.com/pyGuru123/Python-Games/tree/master/Piano%20Tiles).

## Who codes what (4-person split)

Each member watches their videos, writes that part, and changes anything mouse-based to the arrow keys.

### Darius Malich (DM): Window and screens (Part 1 + Part 5)
- Part 1: game window, background image, game loop, FPS, quit with ESC/Q
- Part 5: home page (piano image, title, "Press SPACE to start") and game over screen ("Game over", score, "R to replay, M for sound, Q to quit")
- Use key presses instead of the Start / Replay / Close / Sound buttons
- Keep `main.py` organized with clear sections so the others can add their parts; help fix merge conflicts

### Auon Tippu (AT): Tiles (Part 2)
- `Tile` class in `main.py`: drawing, moving down, removing itself off-screen, greyed out when hit (`alive = False`)
- Spawning a new tile in a random column right above the last one so there are no gaps
- Speed that increases with the score (`get_speed(score)`)
- Game over when an unhit tile reaches the bottom (tile turns red)
- Write a helper `get_lowest_tile(tile_group)` that returns the lowest tile still alive (Gurmanpal needs this)

### Gurmanpal Banwait (GB): Arrow key controls and scoring (Part 3 + score part of Part 6)
- This is the part that's different from the tutorial. Watch Part 3 to see how he checks clicks, then replace it:
  - On `KEYDOWN`, map `K_LEFT, K_DOWN, K_UP, K_RIGHT` to columns 0, 1, 2, 3
  - Find the column of the lowest alive tile: `tile.rect.x // TILE_WIDTH`
  - Right column: mark the tile as hit, +1 score. Wrong column: buzzer and game over
  - Ignore arrow keys before the 3-2-1 countdown finishes and after game over
- Score and high score shown at the top while playing, and reset on replay

### Harmanpal Banwait (HB): Sound and effects (Part 4 + animations of Part 6)
- Part 4: `notes.json`, piano note sounds in `Sounds/`, playing the next note on every correct hit, buzzer on game over, background music, M key toggles sound
- Part 6: `Text` class ("+1" floating up), `Counter` class (3-2-1 countdown), `Square` class (falling background squares), flashing red overlay on game over

## Order to build it in

1. Darius pushes the window and game loop (Part 1) first, plus the `Assets/`, `Sounds/` and `Fonts/` folders from the tutorial's source code
2. Auon, Gurmanpal and Harmanpal add their parts in their own labelled sections of `main.py`
3. Everyone pulls and pushes small changes often; Darius helps fix conflicts
4. Everyone tests together, fixes bugs, and adds polish

## How we use Git

We all work on `main.py` on the `main` branch and push straight to GitHub. Full steps are in [docs/GIT_STEPS.md](docs/GIT_STEPS.md).

- `git pull` before you start coding, every time
- Only edit your own labelled sections of `main.py`
- Commit and push small changes often, and `git pull` right before every `git push`
- Run `python main.py` before every push so nobody pulls broken code
- Never use `git push --force`
- Say "pushing now" in the group chat
- Credit the tutorial in your report, since our code is based on it
