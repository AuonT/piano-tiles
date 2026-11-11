# Member 2: Tiles

**Branch:** `tiles`  **Issue:** #2
**Video:** [Part 2: Creating tiles](https://www.youtube.com/watch?v=LHqiU4hc5_0)
**Your files:** `objects.py` (`Tile` class), plus the "Member 2" spots in `main.py` (GROUPS, functions, GAME PAGE)

Git commands are in [GIT_STEPS.md](GIT_STEPS.md).

## Step 1: Agree with Member 3 first
Before coding, message Member 3 and agree on:
- [ ] The `Tile` attribute names: `rect` (position), `alive` (True until hit), `color`
- [ ] The helper `get_lowest_tile(tile_group)`: returns the lowest tile that's still alive, or `None` if there isn't one

## Step 2: Tile class (Part 2)
- [ ] Create `objects.py` with the same `WIDTH`, `HEIGHT`, `TILE_WIDTH`, `TILE_HEIGHT` numbers as `main.py`
- [ ] `Tile` class: draws itself, moves down by `speed` in `update(speed)`, removes itself (`self.kill()`) when it goes off the bottom
- [ ] When `alive` is False (hit), draw it see-through grey

## Step 3: Tiles in the game (Part 2)
- [ ] In GROUPS: uncomment `tile_group`
- [ ] When the game starts, add the first tile in a random column above the screen
- [ ] In GAME PAGE: update every tile, and spawn a new tile in a random column right above the last one so there are no gaps
- [ ] `get_speed(score)`: `200 + 5 * score`, so it speeds up as the score goes up
- [ ] If a tile that's still alive reaches the bottom: make it red and set `game_over = True`

## Step 4: The helper for Member 3
- [ ] Write `get_lowest_tile(tile_group)`. Hint: loop through the tiles, skip ones that aren't alive, keep the one with the biggest `rect.y`

## Different from the tutorial
His tiles are hit by clicking (`collidepoint`). Don't write any click code. Member 3 handles hitting with the arrow keys using your `get_lowest_tile`.

## Done when
- [ ] Tiles fall in random columns with no gaps, get faster, and the game ends when one reaches the bottom
- [ ] `get_lowest_tile` works (test by printing its column: `tile.rect.x // TILE_WIDTH`)
