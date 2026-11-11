# Member 3: Arrow key controls and score

**Branch:** `controls`  **Issue:** #3
**Videos:** [Part 3: Tile clicks](https://www.youtube.com/watch?v=s4_ApCTvYtg) (watch to understand it, then replace the clicks), score part of [Part 6](https://www.youtube.com/watch?v=l0yGzZCnVVc)
**Your spots in `main.py`:** the "Member 3" function, the arrow key line in EVENTS, and the score drawing in GAME PAGE

This is the part that's different from the tutorial, so it's the most original code. Git commands are in [GIT_STEPS.md](GIT_STEPS.md).

## Step 1: Agree with Member 2 first
- [ ] Tile attributes: `rect`, `alive`, `color`
- [ ] Member 2's helper `get_lowest_tile(tile_group)` returns the lowest alive tile, or `None`
- [ ] While waiting for their code, you can write your function and test it with `print()`

## Step 2: How the arrow keys work
`KEY_TO_COLUMN` is already in `main.py`: ← = 0, ↓ = 1, ↑ = 2, → = 3.

Write `handle_arrow_key(key)`:
- [ ] Get the column for the key from `KEY_TO_COLUMN`
- [ ] Get the lowest alive tile with `get_lowest_tile(tile_group)`
- [ ] Find that tile's column: `tile.rect.x // TILE_WIDTH`
- [ ] **Same column:** set `tile.alive = False`, add 1 to `score`, update `high_score` if needed
- [ ] **Different column:** `game_over = True` (Member 4 adds the buzzer sound)
- [ ] Remember `global score, high_score, game_over` at the top of the function, since it changes those variables

## Step 3: Only when it should work
- [ ] Ignore arrow keys on the home page, during the 3-2-1 countdown, and after game over
- [ ] In EVENTS: `if event.key in KEY_TO_COLUMN: handle_arrow_key(event.key)` (with the checks above)

## Step 4: Score (Part 6)
- [ ] Draw "Score: X" and "High: Y" at the top during the game
- [ ] Score resets to 0 when replaying (Member 1's `reset_game`), high score stays

## Tell Member 4
After a correct hit, Member 4 needs to play a note and show a "+1". Leave a comment like `# Member 4: play note and +1 here` in the right spot so they can add one line.

## Done when
- [ ] Right arrow on the right column = point, wrong key = game over
- [ ] Holding or mashing keys before the game starts does nothing
- [ ] Score and high score show at the top
