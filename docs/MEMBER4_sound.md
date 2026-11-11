# Member 4: Sound and effects

**Branch:** `sound`  **Issue:** #4
**Videos:** [Part 4: Playing piano](https://www.youtube.com/watch?v=manti3I6hY0), [Part 6: Scores, animations and fall effects](https://www.youtube.com/watch?v=l0yGzZCnVVc)
**Your files:** `Text`, `Counter`, `Square` classes in `objects.py`, plus the SOUNDS section and "Member 4" spots in `main.py`

Git commands are in [GIT_STEPS.md](GIT_STEPS.md). Member 1 adds the `Sounds/` folder and `notes.json` first, so pull before you start.

## Step 1: Sounds (Part 4)
- [ ] In SOUNDS & NOTES: load `notes.json`, the buzzer sound and background music
- [ ] Write `play_note()`: plays the next note of the song each time it's called (loop back to the start at the end)
- [ ] Buzzer plays on game over (both for a missed tile and a wrong key)
- [ ] M key turns sound on and off (`sound_on`); when off, no music or notes

## Step 2: Effects (Part 6)
- [ ] `Counter` class: 3-2-1 countdown before tiles start moving
- [ ] `Text` class: "+1" that floats up from a hit tile
- [ ] `Square` class: falling, spinning squares in the background
- [ ] Flashing red overlay (`Assets/red overlay.png`) on game over

## Step 3: Hook into everyone else's code
- [ ] After a correct hit (Member 3's function): call `play_note()` and add a `Text("+1", ...)`
- [ ] The countdown needs to finish before tiles move and arrow keys work. Tell Members 2 and 3 what to check (for example `time_counter.count <= 0`)

## Different from the tutorial
- He uses a `Thread` to play notes. You don't need it, `pygame.mixer.Sound(...).play()` already plays without freezing the game
- His sound on/off is a mouse button. Ours is the M key

## Shared files
`objects.py` is shared with Member 2. Add your classes **below** their `Tile` class, and don't change their code, to avoid merge conflicts.

## Done when
- [ ] Each correct hit plays the next note and shows "+1"
- [ ] Countdown shows before play, red flash and buzzer on game over
- [ ] M mutes and unmutes
