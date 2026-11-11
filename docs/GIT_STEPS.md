# Git steps for everyone

Your **workspace** is your own branch. You code there, and nothing you do can break anyone else's work until your Pull Request is merged.

| Member | Branch | Guide |
|---|---|---|
| 1 | `screens` | [MEMBER1_screens.md](MEMBER1_screens.md) |
| 2 | `tiles` | [MEMBER2_tiles.md](MEMBER2_tiles.md) |
| 3 | `controls` | [MEMBER3_controls.md](MEMBER3_controls.md) |
| 4 | `sound` | [MEMBER4_sound.md](MEMBER4_sound.md) |

## First time only

```bash
git clone https://github.com/AuonT/piano-tiles.git
cd piano-tiles
pip install pygame
git checkout tiles        # use YOUR branch name
python main.py            # a black window with a blue border = working
```

You need to be added as a collaborator on the repo before you can push. Send Auon your GitHub username.

## Every time you sit down to code

```bash
git checkout main
git pull                  # get everyone's latest merged work
git checkout tiles        # YOUR branch
git merge main            # bring that latest work into your branch
```

## Saving your work

```bash
git add .
git commit -m "Add Tile class with move and draw"   # say what you did
git push
```

Commit small and often (every time something works), not one giant commit at the end.

## When your part works: Pull Request

1. Run `python main.py` and check the game still runs.
2. Push your branch (`git push`).
3. On GitHub, click **Compare & pull request**, set **base: main** and **compare: your branch**.
4. Write what you added and link your issue (for example "Closes #2").
5. Ask one other member to review, then merge.

Merge **one Pull Request at a time**. After each merge, everyone runs the "every time you sit down" steps above.

## If you get a merge conflict

Git shows something like this in the file:

```
<<<<<<< HEAD
your code
=======
someone else's code
>>>>>>> main
```

Keep the lines you need from **both** sides, delete the `<<<<<<<`, `=======`, `>>>>>>>` lines, save, then:

```bash
git add .
git commit -m "Fix merge conflict"
git push
```

VS Code shows **Accept Current / Accept Incoming / Accept Both** buttons above conflicts, which makes this easier. If you're stuck, ask the group before deleting anything.

## Rules

- Never commit directly to `main`.
- Only edit **your** labelled sections in `main.py`.
- Don't rename shared variables (`score`, `speed`, `game_over`, `TILE_WIDTH`...) without telling the group.
- Run the game before every push.
