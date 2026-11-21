# Piano Tiles - CHE 120 group project
# Based on pyGuru's "Piano Tiles Clone with pygame" tutorial, played with the arrow keys.
#
# HOW TO USE THIS FILE
# - Each member only adds code inside their own labelled section.
# - Put big chunks of code in functions/classes (or in objects.py) and just CALL them here.
#   Fewer changed lines in main.py = fewer merge conflicts.
# - Don't rename the shared variables below without telling the group.
#gurm

import random
import pygame

# from objects import Tile, Text, Counter, Square   # uncomment once these classes exist in objects.py

pygame.init()

# =============================================================================
# SETTINGS (Member 1) - shared numbers everyone uses
# =============================================================================
SCREEN = WIDTH, HEIGHT = 288, 512
TILE_WIDTH = WIDTH // 4
TILE_HEIGHT = 130
FPS = 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (75, 75, 75)
BLUE = (30, 144, 255)

# Arrow keys -> column number (0 = far left, 3 = far right)
KEY_TO_COLUMN = {
    pygame.K_LEFT: 0,
    pygame.K_DOWN: 1,
    pygame.K_UP: 2,
    pygame.K_RIGHT: 3,
}

win = pygame.display.set_mode(SCREEN)
pygame.display.set_caption("Piano Tiles")
clock = pygame.time.Clock()

# =============================================================================
# IMAGES & FONTS (Member 1)
# =============================================================================
# Load Assets/ images and Fonts/ here (Part 1 and Part 5)


# =============================================================================
# SOUNDS & NOTES (Member 4)
# =============================================================================
# Load notes.json, buzzer sound and background music here (Part 4)


# =============================================================================
# GROUPS (Member 2 + Member 4)
# =============================================================================
tile_group = pygame.sprite.Group()     # Member 2
# text_group = pygame.sprite.Group()     # Member 4 ("+1" pop-ups)
# square_group = pygame.sprite.Group()   # Member 4 (background squares)


# =============================================================================
# SHARED GAME VARIABLES - everyone reads these, don't rename them
# =============================================================================
score = 0
high_score = 0
speed = 0

home_page = True
game_page = False
game_over = False
sound_on = True


# =============================================================================
# FUNCTIONS
# =============================================================================

# --- Member 2: tiles ---
class Tile(pygame.sprite.Sprite): #creates an object called tile that is a sprite and everything below is a function that is part of the tile class
    def __init__(self, x, y, win): # __init__ runs whenever a new tile is created x and y are the coordinates of the tile and win is the window that the tile will be drawn on
        super().__init__() #this runs the pygame setup first so that the tile can be drawn on the window
        self.win = win #saves the window that the tile will be drawn on
        self.color = BLACK #sets the color of the tile to black
        self.alive = True #sets the tile to be alive aka not hit yet

        self.surface = pygame.Surface((TILE_WIDTH, TILE_HEIGHT), pygame.SRCALPHA) #makes a blank rectangle that is the size of the tile
        self.rect = self.surface.get_rect() #rect stores the position of the tile, later moving the tile will self.recy.y
        self.rect.x = x #sets the x position of the tile to the x that was passed in
        self.rect.y = y #sets the y position of the tile to the y that was passed in

    def update(self, speed): #defines the speed of the tile and moves it down the screen
        self.rect.y += speed #it moves the tiles down by speed pixels every frame
        if self.rect.top >= HEIGHT: #checks to see if the tile has moved off the bottom of the screen.
            self.kill() #if its off the screen it kills itself.

        self.surface.fill((0, 0, 0, 0)) #clears the tile canvas before redrawing it
        if self.alive:
            pygame.draw.rect(self.surface, self.color, (0, 0, TILE_WIDTH, TILE_HEIGHT), border_radius=10) #draws the tile on the canvas with rounding the corners
            pygame.draw.rect(self.surface, BLUE, (0, 0, TILE_WIDTH, TILE_HEIGHT), 3, border_radius=8) #draws the blue outline of the tile on the canvas with rounding the corners
        else:
            pygame.draw.rect(self.surface, GRAY, (0, 0, TILE_WIDTH, TILE_HEIGHT), border_radius=8) #a hit tile becomes gray and the blue outline is removed

        self.win.blit(self.surface, self.rect) #blit stamps the tile canvas onto the window at the position of the tile

def get_speed(score): #returns the speed of the tiles based on the score
        return min(200 + 5 * score, 600) #means start at 200 and increase by 5 for every score but max out at 600

def add_new_tile(): #adds a new tile to the game
    if len(tile_group) == 0: #if there are no tiles on the screen, the new tile will be placed just above the screen
        y = -TILE_HEIGHT #if there are no tiles on the screen, the new tile will be placed just above the screen
        last_column = -1 #last column is set to -1 so that the first tile can be placed in any column
    else:
        last = tile_group.sprites()[-1] #gets the last tile that was added to the game
        y = last.rect.top - TILE_HEIGHT #the new tile will be placed just above the last tile
        last_column = last.rect.x // TILE_WIDTH #gets the column of the last tile that was added to the game

    column = random.randint(0, 3) #randomly chooses a column for the new tile to be placed in
    while column == last_column:
        column = random.randint(0, 3)

    tile_group.add(Tile(column * TILE_WIDTH, y, win))
def get_lowest_tile(tile_group): #returns the lowest tile that is still alive
    lowest = None #nothing found yet
    for tile in tile_group: #goes through every tile one at a time.
        if tile.alive: #skips the tiles that we already hit
            if lowest is None or tile.rect.y > lowest.rect.y: #If we haven’t picked one yet, or this tile is lower down than the one we picked
                lowest = tile
    return lowest



# --- Member 3: arrow keys and score ---
# =====================  BLUEPRINT FOR MEMBER 3  =====================
# Fill in each STEP below in order. The hints tell you WHAT to use,
# you write the actual code. Run `python main.py` after every step.
#
# How to test: temporarily set game_page = True (SHARED GAME VARIABLES),
# run the game and press the arrow keys. Set it back to False before pushing.
#
# Things you can use (already written by others):
#   KEY_TO_COLUMN          dictionary: arrow key -> column number 0-3 (SETTINGS, top of file)
#   get_lowest_tile(...)   Member 2's function: gives the tile to hit next, or None
#   tile.alive             True = not hit yet, False = hit (turns grey)
#   tile.rect.x            the tile's x position in pixels
#   TILE_WIDTH             width of one column in pixels (72)
#   score, high_score, game_over   shared variables
# =====================================================================

# STEP A: make a font for the score text (only once, so it goes here, NOT in the loop).
#   Hint: pygame.font.SysFont(None, 32) makes a basic font at size 32.
#   Save it in a variable, for example called score_font.


def handle_arrow_key(key):
    # This runs every time the player presses an arrow key.
    # `key` tells you WHICH arrow was pressed (pygame.K_LEFT, K_DOWN, K_UP or K_RIGHT).

    # STEP 1: You're going to CHANGE score, high_score and game_over in here.
    #   Hint: Python needs one line starting with the word `global` followed by those 3 names.

    # STEP 2: Turn the key into a column number (0, 1, 2 or 3).
    #   Hint: look `key` up in the KEY_TO_COLUMN dictionary, like dictionary[key].
    #   Save it in a variable, for example pressed_column.

    # STEP 3: Get the tile the player is supposed to hit right now.
    #   Hint: Member 2's get_lowest_tile function. It needs tile_group passed in.
    #   Save it in a variable, for example target.

    # STEP 4: If there's no tile to hit (target is None), stop here.
    #   Hint: an `if` with `return` inside it ends the function early.

    # STEP 5: Work out which column the target tile is in.
    #   Hint: divide the tile's x position by TILE_WIDTH using // (whole-number division).
    #   Save it in a variable, for example target_column.

    # STEP 6: Compare pressed_column and target_column with if / else.
    #   If they MATCH (right key):
    #     - mark the target tile as hit   (Hint: its alive attribute)
    #     - add 1 to score                (Hint: += )
    #     - if score is now bigger than high_score, make high_score equal score
    #     - add this comment for Member 4:  # Member 4: play note and +1 here
    #   If they DON'T match (wrong key):
    #     - end the game                  (Hint: game_over)
    #     - add this comment for Member 4:  # Member 4: buzzer here

    pass   # delete this line once you've written your steps above

# When it works:
#   - right arrow on the right column -> tile turns grey, score goes up
#   - wrong arrow -> game ends
#   - pressing keys on the home page or after game over does nothing (see STEP 7 in the loop)


# --- Member 4: sound and effects ---
# def play_note(): ...


# --- Member 1: screens ---
# def draw_home_page(): ...
# def draw_game_over(): ...
# def reset_game(): ...   used when R is pressed


# =============================================================================
# MAIN GAME LOOP (Member 1 owns the structure; others add ONE-LINE calls)
# =============================================================================
running = True
while running:

    # ---------- EVENTS ----------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_ESCAPE, pygame.K_q):
                running = False

            # Member 1: SPACE starts the game from the home page
            # Member 1: R replays after game over
            # Member 4: M toggles sound
            # Member 3, STEP 7: call handle_arrow_key here, but ONLY when ALL of these are true:
            #   - the key is an arrow key        (Hint: event.key in KEY_TO_COLUMN)
            #   - the game page is showing       (Hint: game_page)
            #   - the game is NOT over           (Hint: not game_over)
            #   - later: the 3-2-1 countdown is finished (ask Member 4 what to check)
            # Hint: ONE `if` line with `and` between the conditions, then call the
            # function on the next line and give it event.key

    # ---------- DRAW BACKGROUND ----------
    win.fill(BLACK)   # Member 1: replace with the background image
    # Member 4: update the falling background squares here

    # ---------- HOME PAGE (Member 1) ----------
    if home_page:
        pass  # draw_home_page()

    # ---------- GAME PAGE ----------
    if game_page:
        # Member 4: 3-2-1 countdown
        # Member 2: move tiles, spawn new tiles, check if a tile reached the bottom
        if len(tile_group) == 0:
            add_new_tile() #when the game starts and there are no tiles yet this makes the new one.
        for tile in tile_group: #for every tile that there is it moves it down, the tile class is being used here.
            tile.update(speed)
            if tile.alive and tile.rect.bottom >= HEIGHT and not game_over: #if the tile wasn't hit and hits the bottom turns the tile red and ends the game.
                tile.color = (255, 0, 0)
                game_over = True
        if tile_group.sprites()[-1].rect.top + speed >= 0: #if the new tile is about to slide onto the screen add a new tile right above.
            add_new_tile()
        # Member 4: update "+1" text pop-ups
        # Member 3, STEP 8: draw the score and high score at the top.
        #   1. Turn text into a picture:  your_font.render(text, True, WHITE)
        #      The text should say e.g. "Score: 5". Hint: an f-string like f"Score: {score}"
        #   2. Stamp the picture on the window:  win.blit(picture, (x, y))
        #      Try (10, 10) for the score and (180, 10) for the high score.
        #   Do both for score AND high_score (4 lines total).

        # column lines
        for i in range(4):
            pygame.draw.line(win, WHITE, (TILE_WIDTH * i, 0), (TILE_WIDTH * i, HEIGHT), 1)

        # Member 2: speed = int(get_speed(score) * (FPS / 1000))
        speed = int(get_speed(score) * (FPS / 1000))

        if game_over:
            speed = 0
            # Member 4: flashing red overlay
            # Member 1: draw_game_over()

    # ---------- UPDATE SCREEN ----------
    pygame.draw.rect(win, BLUE, (0, 0, WIDTH, HEIGHT), 2)
    clock.tick(FPS)
    pygame.display.update()

pygame.quit()
