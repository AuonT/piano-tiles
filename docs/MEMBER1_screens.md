# Member 1: Window and screens

**Branch:** `screens`  **Issue:** #1
**Videos:** [Part 1: Game window](https://www.youtube.com/watch?v=t1GaunoW0Tc), [Part 5: Start and end screens](https://www.youtube.com/watch?v=_VvOedsZl5w)
**Your sections in `main.py`:** SETTINGS, IMAGES & FONTS, "Member 1: screens" functions, HOME PAGE, and the SPACE / R keys

You go first: the others build on top of your setup. Git commands are in [GIT_STEPS.md](GIT_STEPS.md).

## Step 1: Assets (do this first, push it right away)
- [ ] Download the `Assets/`, `Fonts/` and `Sounds/` folders and `notes.json` from the [tutorial source](https://github.com/pyGuru123/Python-Games/tree/master/Piano%20Tiles) (on GitHub: go up to the repo page, **Code → Download ZIP**, then copy the folders out)
- [ ] Put them in the root of our repo, next to `main.py`. Keep the exact folder names (capital A, F, S)
- [ ] Commit, push, open a Pull Request and merge it so everyone has the files

## Step 2: Window (Part 1)
- [ ] Load `Assets/bg.png` in IMAGES & FONTS and draw it instead of `win.fill(BLACK)`
- [ ] Skip his `NOFRAME` / `FULLSCREEN` window code: our normal window is easier to test

## Step 3: Home page (Part 5)
- [ ] Load the piano image, title and fonts
- [ ] Write `draw_home_page()`: piano image, "Piano Tiles" title, and the text **"Press SPACE to start"** (no Start button)
- [ ] In the EVENTS section: if SPACE is pressed on the home page, set `home_page = False` and `game_page = True`

## Step 4: Game over screen (Part 5)
- [ ] Write `draw_game_over()`: "Game over", the score, and **"R to replay  M for sound  Q to quit"**
- [ ] Write `reset_game()`: score back to 0, speed back to 0, `game_over = False`, empty the groups, new countdown
- [ ] In EVENTS: if R is pressed while `game_over` is True, call `reset_game()`

## Different from the tutorial
His `Button` class uses the mouse. We don't need it. Every button becomes a key press.

## Also your job
- Review other members' Pull Requests and help fix merge conflicts in `main.py`
- Keep the labelled sections tidy

## Done when
- [ ] Game opens on a home page with the background, and SPACE starts it
- [ ] Game over screen shows the score, and R restarts cleanly, ESC/Q quits
