# Piano Tiles - CHE 120 group project
# Based on pyGuru's "Piano Tiles Clone with pygame" tutorial, played with the arrow keys.
#
# HOW TO USE THIS FILE
# - Each member only adds code inside their own labelled section.
# - Put big chunks of code in functions/classes (or in objects.py) and just CALL them here.
#   Fewer changed lines in main.py = fewer merge conflicts.
# - Don't rename the shared variables below without telling the group.

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
# tile_group = pygame.sprite.Group()     # Member 2
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
# def get_speed(score): ...
# def get_lowest_tile(tile_group): ...   returns the lowest tile that is still alive


# --- Member 3: arrow keys and score ---
# def handle_arrow_key(key): ...   right column = +1 score, wrong column = game over


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
            # Member 3: arrow keys -> if event.key in KEY_TO_COLUMN: handle_arrow_key(event.key)

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
        # Member 4: update "+1" text pop-ups
        # Member 3: draw score and high score at the top

        # column lines
        for i in range(4):
            pygame.draw.line(win, WHITE, (TILE_WIDTH * i, 0), (TILE_WIDTH * i, HEIGHT), 1)

        # Member 2: speed = int(get_speed(score) * (FPS / 1000))

        if game_over:
            speed = 0
            # Member 4: flashing red overlay
            # Member 1: draw_game_over()

    # ---------- UPDATE SCREEN ----------
    pygame.draw.rect(win, BLUE, (0, 0, WIDTH, HEIGHT), 2)
    clock.tick(FPS)
    pygame.display.update()

pygame.quit()
