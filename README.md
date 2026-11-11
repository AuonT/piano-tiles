# Piano Tiles 🎹

CHE 120 group project: a Piano Tiles game written in Python with **pygame**.

Black tiles fall down 4 columns. Click (or press the matching key) on each black tile before it reaches the bottom. Miss a tile or click a white space and the game is over. The game speeds up as your score goes up.

## Getting started

1. Install Python 3.10+ and then pygame: `pip install pygame`
2. Clone the repo: `git clone https://github.com/AuonT/piano-tiles.git`
3. Run the game: `python main.py`

## Planned file structure

| File | What goes in it | Owner |
|---|---|---|
| `main.py` | Window setup, main game loop, game states (menu / playing / game over) | Member 1 |
| `settings.py` | Shared constants: screen size, 4 columns, colours, FPS, starting speed | Member 1 |
| `tiles.py` | `Tile` class, spawning new rows, moving tiles down, speed-up | Member 2 |
| `input_handler.py` | Mouse clicks + keyboard keys (D F J K), checking hits and misses | Member 3 |
| `score.py` | Score counter (add points, reset on restart) | Member 3 |
| `highscore.py` | Load and save the high score in `highscore.txt` | Member 4 |
| `screens.py` | Start menu, game over screen, drawing the score on screen | Member 4 |
| `sounds/` + `sound.py` | Piano note sounds when a tile is hit, fail sound | Member 4 |

## Who codes what (4-person split)

### Member 1: Game loop and setup
- Create `settings.py` with all shared constants (do this FIRST so everyone uses the same numbers)
- Create `main.py`: open a 400x600 window, run the loop at 60 FPS, handle the quit event
- Draw the 4 column grid lines
- Manage game states: `"menu"`, `"playing"`, `"game_over"`, with clear spots in the loop where each member plugs in their part
- Review the other members' Pull Requests and help fix merge conflicts

### Member 2: Tiles
- Write a `Tile` class (column, y position, height, `was_hit` flag) with `move(speed)` and `draw(screen)`
- Spawn a new row with one black tile in a random column whenever the top row has moved down far enough
- Remove tiles that leave the screen; if an unhit tile reaches the bottom, report a miss (game over)
- Slowly increase the falling speed as the score goes up
- Agree with Member 3 early on the `Tile` attribute names and a function to get the lowest unhit tile in a column
- Hook your tile updating and drawing into `main.py` yourself

### Member 3: Input and scoring
- Turn a mouse click into a column number (x position divided by column width)
- Map keys D F J K to columns 0 to 3
- Check if the click/key hits the lowest unhit tile in that column; correct = +1 point, wrong = game over
- Keep track of the score (add a point per hit, reset on restart)
- Hook your input handling into the event loop in `main.py` yourself

### Member 4: Screens, sound and polish
- Start menu ("Press SPACE to start"), and game over screen showing score + high score and "Press R to restart"
- Draw the live score at the top of the screen while playing
- Play a piano note when a tile is hit and a fail sound on game over (`pygame.mixer`)
- Red flash on a wrong click
- Load and save the high score in `highscore.txt` (`highscore.py`) and show it on the game over screen
- Hook your screens and sounds into `main.py` yourself

## Order to build it in

1. Member 1 pushes `settings.py` and a blank window in `main.py`
2. Members 2, 3 and 4 build their files using the constants from `settings.py`
3. Each member connects their own part into `main.py` through a Pull Request; Member 1 reviews and helps fix conflicts
4. Everyone tests, fixes bugs, and adds polish

## How we use Git

- Never code directly on `main`. Make a branch for your part: `git checkout -b tiles` (or `input`, `screens`, etc.)
- Commit often with clear messages, e.g. `Add Tile class with move and draw`
- Push your branch and open a Pull Request; one other member reviews it before merging
- Run `git pull` on `main` before starting new work so you have everyone's latest code
- Each task is an Issue in the Issues tab; assign yourself to the ones you're working on
