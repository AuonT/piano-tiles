# ORIGINAL CODE, copied unchanged, for the CHE 120 "comment the original code" task.
# Source: "Piano Tiles" by Prajjwal Pathak (pyGuru)
#   Code: https://github.com/pyGuru123/Python-Games/tree/master/Piano%20Tiles
#   Videos: https://www.youtube.com/playlist?list=PLHlrXTRZkTLDIT7mEYUcwzOXHFR47EIpN
#
# Group members (full names and initials):
#   Darius Malich (DM)       GitHub: dmalich6-byte   window and screens
#   Auon Tippu (AT)          GitHub: AuonT           tiles
#   Gurmanpal Banwait (GB)   GitHub: gurmy-b         arrow keys and score
#   Harmanpal Banwait (HB)   GitHub: hbanwait120     sound and effects
#
# Initial every comment you add, e.g.  # AT: this moves the tile down by speed each frame
# =============================================================================

# Piano Tiles

# Author : Prajjwal Pathak (pyguru)
# Date : Thursday, 30 November, 2021

import json
import random
import pygame
from threading import Thread

from objects import Tile, Square, Text, Button, Counter

pygame.init()
SCREEN = WIDTH, HEIGHT = 288, 512
TILE_WIDTH = WIDTH // 4  #AT: same as in objects.py, 4 columns so each tile is a quarter of the screen
TILE_HEIGHT = 130  #AT: height of each tile in pixels

info = pygame.display.Info()
width = info.current_w
height = info.current_h

if width >= height:
	win = pygame.display.set_mode(SCREEN, pygame.NOFRAME)
else:
	win = pygame.display.set_mode(SCREEN, pygame.NOFRAME | pygame.SCALED | pygame.FULLSCREEN)

clock = pygame.time.Clock()
FPS = 30

# COLORS *********************************************************************

WHITE = (255, 255, 255)
GRAY = (75, 75, 75)
BLUE = (30, 144, 255)

# IMAGES *********************************************************************

bg_img = pygame.image.load('Assets/bg.png')
bg_img = pygame.transform.scale(bg_img, (WIDTH, HEIGHT))

piano_img = pygame.image.load('Assets/piano.png')
piano_img = pygame.transform.scale(piano_img, (212, 212))

title_img = pygame.image.load('Assets/title.png')
title_img = pygame.transform.scale(title_img, (200, 50))

start_img = pygame.image.load('Assets/start.png')
start_img = pygame.transform.scale(start_img, (120, 40))
start_rect = start_img.get_rect(center=(WIDTH//2, HEIGHT-80))

overlay = pygame.image.load('Assets/red overlay.png')
overlay = pygame.transform.scale(overlay, (WIDTH, HEIGHT))

# MUSIC **********************************************************************

buzzer_fx = pygame.mixer.Sound('Sounds/piano-buzzer.mp3')

pygame.mixer.music.load('Sounds/piano-bgmusic.mp3')
pygame.mixer.music.set_volume(0.8)
pygame.mixer.music.play(loops=-1)

# FONTS **********************************************************************

score_font = pygame.font.Font('Fonts/Futura condensed.ttf', 32)
title_font = pygame.font.Font('Fonts/Alternity-8w7J.ttf', 30)
gameover_font = pygame.font.Font('Fonts/Alternity-8w7J.ttf', 40)

title_img = title_font.render('Piano Tiles', True, WHITE)

# BUTTONS ********************************************************************

close_img = pygame.image.load('Assets/closeBtn.png')
replay_img = pygame.image.load('Assets/replay.png')
sound_off_img = pygame.image.load("Assets/soundOffBtn.png")
sound_on_img = pygame.image.load("Assets/soundOnBtn.png")

close_btn = Button(close_img, (24, 24), WIDTH // 4 - 18, HEIGHT//2 + 120)
replay_btn = Button(replay_img, (36,36), WIDTH // 2  - 18, HEIGHT//2 + 115)
sound_btn = Button(sound_on_img, (24, 24), WIDTH - WIDTH // 4 - 18, HEIGHT//2 + 120)

# GROUPS & OBJECTS ***********************************************************

tile_group = pygame.sprite.Group()  #AT: holds all the tiles on the screen so they can be updated together and deleted with kill()
square_group = pygame.sprite.Group()
text_group = pygame.sprite.Group()

time_counter = Counter(win, gameover_font)

# FUNCTIONS ******************************************************************

def get_speed(score):  #AT: works out how fast the tiles fall based on the score
	return 200 + 5 * score  #AT: starts at 200 and goes up by 5 every point so the game gets harder the longer you last

def play_notes(notePath):
	pygame.mixer.Sound(notePath).play()

# NOTES **********************************************************************

with open('notes.json') as file:
	notes_dict = json.load(file)

# VARIABLES ******************************************************************

score = 0
high_score = 0
speed = 0

clicked = False
pos = None

home_page = True
game_page = False
game_over = False
sound_on = True

count = 0
overlay_index = 0

running = True
while running:
	pos = None

	count += 1
	if count % 100 == 0:
			square = Square(win)
			square_group.add(square)
			counter = 0

	win.blit(bg_img, (0,0))
	square_group.update()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE or \
				event.key == pygame.K_q:
				running = False

		if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
			pos = event.pos

	if home_page:
		win.blit(piano_img, (WIDTH//8, HEIGHT//8))
		win.blit(start_img, start_rect)
		win.blit(title_img, (WIDTH // 2 - title_img.get_width() / 2 + 10, 300))

		if pos and start_rect.collidepoint(pos):
			home_page = False
			game_page = True

			x = random.randint(0, 3)  #AT: picks a random column from 0 to 3 for the first tile
			t = Tile(x * TILE_WIDTH, -TILE_HEIGHT, win)  #AT: makes the first tile in that column just above the screen so it slides in instead of popping in
			tile_group.add(t)  #AT: adds it to the group so it gets moved and drawn every frame

			pos = None

			notes_list = notes_dict['2']
			note_count = 0
			pygame.mixer.set_num_channels(len(notes_list))

	if game_page:
		time_counter.update()
		if time_counter.count <= 0:
			for tile in tile_group:  #AT: goes through every tile on the screen
				tile.update(speed)  #AT: moves each tile down and draws it (the update method in objects.py)

				if pos:
					if tile.rect.collidepoint(pos):
						if tile.alive:
							tile.alive = False
							score += 1
							if score >= high_score:
								high_score = score
							

							note = notes_list[note_count].strip()
							th = Thread(target=play_notes, args=(f'Sounds/{note}.ogg', ))
							th.start()
							th.join()
							note_count = (note_count + 1) % len(notes_list)

							tpos = tile.rect.centerx - 10, tile.rect.y
							text = Text('+1', score_font, tpos, win)
							text_group.add(text)

						pos = None

				if tile.rect.bottom >= HEIGHT and tile.alive:  #AT: if a tile that wasnt hit reaches the bottom of the screen then the player missed it
					if not game_over:  #AT: only does this once, otherwise it would keep happening every frame after the game ends
						tile.color = (255, 0, 0)  #AT: turns the missed tile red so the player can see which one they missed
						buzzer_fx.play()
						game_over = True

			if pos:
				buzzer_fx.play()
				game_over = True

			if len(tile_group) > 0:  #AT: only checks if there are tiles to look at, otherwise sprites()[-1] would crash
				t = tile_group.sprites()[-1]  #AT: gets the newest tile, its the last one added so its the one at the top
				if t.rect.top + speed >= 0:  #AT: if the newest tile is about to fully come onto the screen its time to make the next one
					x = random.randint(0, 3)  #AT: picks a random column for the next tile
					y = -TILE_HEIGHT - (0 - t.rect.top)  #AT: puts the new tile right on top of the last one so theres no gap between them
					t = Tile(x * TILE_WIDTH, y, win)  #AT: makes the new tile there
					tile_group.add(t)  #AT: adds it to the group with the rest

			text_group.update(speed)
			img1 = score_font.render(f'Score : {score}', True, WHITE)
			win.blit(img1, (70 - img1.get_width() / 2, 10))
			img2 = score_font.render(f'High : {high_score}', True, WHITE)
			win.blit(img2, (200 - img2.get_width() / 2, 10))
			for i in range(4):
				pygame.draw.line(win, WHITE, (TILE_WIDTH * i, 0), (TILE_WIDTH*i, HEIGHT), 1)

			speed = int(get_speed(score) * (FPS / 1000))  #AT: turns the speed into pixels per frame, at 30 fps it starts at 6 pixels every frame

			if game_over:
				speed = 0  #AT: stops the tiles from moving once the game is over

				if overlay_index > 20:
					win.blit(overlay, (0,0))

					img1 = gameover_font.render('Game over', True, WHITE)
					img2 = score_font.render(f'Score : {score}', True, WHITE)
					win.blit(img1, (WIDTH // 2 - img1.get_width() / 2, 180))
					win.blit(img2, (WIDTH // 2 - img2.get_width() / 2, 250))

					if close_btn.draw(win):
						running = False

					if replay_btn.draw(win):
						index = random.randint(1, len(notes_dict))
						notes_list = notes_dict[str(index)]
						note_count = 0
						pygame.mixer.set_num_channels(len(notes_list))

						text_group.empty()
						tile_group.empty()
						score = 0
						speed = 0
						overlay_index = 0
						game_over = False

						time_counter = Counter(win, gameover_font)

						x = random.randint(0, 3)
						t = Tile(x * TILE_WIDTH, -TILE_HEIGHT, win)
						tile_group.add(t)

					if sound_btn.draw(win):
						sound_on = not sound_on
				
						if sound_on:
							sound_btn.update_image(sound_on_img)
							pygame.mixer.music.play(loops=-1)
						else:
							sound_btn.update_image(sound_off_img)
							pygame.mixer.music.stop()
				else:
					overlay_index += 1
					if overlay_index % 3 == 0:
						win.blit(overlay, (0,0))

	pygame.draw.rect(win, BLUE, (0,0, WIDTH, HEIGHT), 2)
	clock.tick(FPS)
	pygame.display.update()

pygame.quit()
