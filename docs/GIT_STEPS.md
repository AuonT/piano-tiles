# Git steps for everyone

We all work on the `main` branch and push straight to GitHub. Everyone edits `main.py`, but **only inside their own labelled section**, so Git can combine everyone's changes on its own.

| Who | Part | Guide |
|---|---|---|
| Darius Malich (DM) | Window and screens | [MEMBER1_screens.md](MEMBER1_screens.md) |
| Auon Tippu (AT) | Tiles | [MEMBER2_tiles.md](MEMBER2_tiles.md) |
| Gurmanpal Banwait (GB) | Arrow keys and score | [MEMBER3_controls.md](MEMBER3_controls.md) |
| Harmanpal Banwait (HB) | Sound and effects | [MEMBER4_sound.md](MEMBER4_sound.md) |

## First time only

```bash
git clone https://github.com/AuonT/piano-tiles.git
cd piano-tiles
pip install pygame-ce
git checkout main
python main.py            # a black window with a blue border = working
```

Use **pygame-ce** (not `pygame`). It works on Python 3.10 to 3.15, and you still write `import pygame` in the code.

You need to be added as a collaborator on the repo before you can push. Send Auon your GitHub username.

## Every time you sit down to code

```bash
git pull                  # get everyone's latest work FIRST
```

## Every time one thing works

```bash
python main.py            # check the game still runs
git add .
git commit -m "Tiles fall and spawn"     # say what you did
git pull                  # get anything pushed while you were coding
python main.py            # check it still runs with their code
git push
```

Push small and often, not one giant push at the end. Post "pushing now" in the group chat.

## If your push is "rejected"

Someone pushed before you. Nothing is broken:

```bash
git pull
python main.py
git push
```

## If you get a merge conflict

Git shows something like this in the file:

```
<<<<<<< HEAD
your code
=======
someone else's code
>>>>>>> 1a2b3c4
```

Usually you want to keep **both** sides. Delete only the `<<<<<<<`, `=======`, `>>>>>>>` lines, save, run the game, then:

```bash
git add .
git commit -m "Fix merge conflict"
git push
```

VS Code shows **Accept Current / Accept Incoming / Accept Both** buttons above conflicts. **Accept Both** is usually right. If you're unsure, ask the person whose code it is before deleting anything.

## Rules

- `git pull` before you start, and right before every push.
- Only edit **your** labelled sections in `main.py`.
- Don't rename shared variables (`score`, `speed`, `game_over`, `TILE_WIDTH`...) without telling the group.
- Run the game before every push. Never push code that crashes.
- **Never** use `git push --force`. It deletes other people's work.
- Don't use `git add .` if there are files in the folder that aren't part of the game (like random images). Use `git add main.py` instead.
# Git steps for everyone

We all work on the `main` branch and push straight to GitHub. Everyone edits `main.py`, but **only inside their own labelled section**, so Git can combine everyone's changes on its own.

| Member | Part | Guide |
|---|---|---|
| 1 | Window and screens | [MEMBER1_screens.md](MEMBER1_screens.md) |
| 2 | Tiles | [MEMBER2_tiles.md](MEMBER2_tiles.md) |
| 3 | Arrow keys and score | [MEMBER3_controls.md](MEMBER3_controls.md) |
| 4 | Sound and effects | [MEMBER4_sound.md](MEMBER4_sound.md) |

## First time only

```bash
git clone https://github.com/AuonT/piano-tiles.git
cd piano-tiles
pip install pygame-ce
git checkout main
python main.py            # a black window with a blue border = working
```

Use **pygame-ce** (not `pygame`). It works on Python 3.10 to 3.15, and you still write `import pygame` in the code.

You need to be added as a collaborator on the repo before you can push. Send Auon your GitHub username.

## Every time you sit down to code

```bash
git pull                  # get everyone's latest work FIRST
```

## Every time one thing works

```bash
python main.py            # check the game still runs
git add .
git commit -m "Tiles fall and spawn"     # say what you did
git pull                  # get anything pushed while you were coding
python main.py            # check it still runs with their code
git push
```

Push small and often, not one giant push at the end. Post "pushing now" in the group chat.

## If your push is "rejected"

Someone pushed before you. Nothing is broken:

```bash
git pull
python main.py
git push
```

## If you get a merge conflict

Git shows something like this in the file:

```
<<<<<<< HEAD
your code
=======
someone else's code
>>>>>>> 1a2b3c4
```

Usually you want to keep **both** sides. Delete only the `<<<<<<<`, `=======`, `>>>>>>>` lines, save, run the game, then:

```bash
git add .
git commit -m "Fix merge conflict"
git push
```

VS Code shows **Accept Current / Accept Incoming / Accept Both** buttons above conflicts. **Accept Both** is usually right. If you're unsure, ask the person whose code it is before deleting anything.

## Rules

- `git pull` before you start, and right before every push.
- Only edit **your** labelled sections in `main.py`.
- Don't rename shared variables (`score`, `speed`, `game_over`, `TILE_WIDTH`...) without telling the group.
- Run the game before every push. Never push code that crashes.
- **Never** use `git push --force`. It deletes other people's work.
- Don't use `git add .` if there are files in the folder that aren't part of the game (like random images). Use `git add main.py` instead.
