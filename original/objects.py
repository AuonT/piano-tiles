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

import pygame
import random

SCREEN = WIDTH, HEIGHT = 288, 512
TILE_WIDTH = WIDTH // 4  #AT: the screen gets split into 4 columns so each tile is a quarter of the screen wide
TILE_HEIGHT = 130  #AT: how tall each tile is in pixels, 130 makes them long enough that you can see them coming

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (30, 144, 255)
BLUE2 = (2, 239, 239)
PURPLE = (191, 64, 191)

class Tile(pygame.sprite.Sprite):  #AT: creates the tile object, its a sprite so it can go in a group and use kill() to delete itself
	def __init__(self, x, y, win):  #AT: runs whenever a new tile is made, x and y are where it starts and win is the window it gets drawn on
		super(Tile, self).__init__()  #AT: runs the pygame sprite setup first so the tile actually works in a group

		self.win = win  #AT: saves the window so the tile can draw itself later in update
		self.x, self.y = x, y  #AT: saves the starting spot but its never used again since rect already has the position
		self.color = BLACK  #AT: every tile starts black, its saved in a variable so it can turn red if you miss it
		self.alive = True  #AT: alive means the tile hasnt been hit yet, when you click it this becomes False

		self.surface = pygame.Surface((TILE_WIDTH, TILE_HEIGHT), pygame.SRCALPHA)  #AT: makes a blank canvas the size of a tile, SRCALPHA lets it be see through so hit tiles can fade out
		self.rect = self.surface.get_rect()  #AT: rect stores the position and size of the tile, moving the tile is just changing rect.y
		self.rect.x = x  #AT: puts the tile in the column it was given
		self.rect.y = y  #AT: puts the tile at the height it was given (usually above the screen so it slides in)

		self.center = TILE_WIDTH//2, TILE_HEIGHT//2 + 15  #AT: finds the middle of the tile (a bit lower down) for where the circle goes
		self.line_start = self.center[0], self.center[1]-18  #AT: the line starts just above the circle
		self.line_end = self.center[0], 20  #AT: and goes up to 20 pixels from the top of the tile, its just decoration

	def update(self, speed):  #AT: this runs every frame, it moves the tile down by speed and then draws it
		self.rect.y += speed  #AT: moves the tile down the screen by speed pixels every frame
		if self.rect.y >= HEIGHT:  #AT: checks if the tile has gone past the bottom of the screen
			self.kill()  #AT: if its off the screen it deletes itself so old tiles dont pile up and slow the game down

		if self.alive:  #AT: if the tile hasnt been hit yet draw the normal tile
			pygame.draw.rect(self.surface, self.color, (0,0, TILE_WIDTH, TILE_HEIGHT))  #AT: fills the tile with its colour (black normally, red if you missed it)
			pygame.draw.rect(self.surface, PURPLE, (0,0, TILE_WIDTH, TILE_HEIGHT), 4)  #AT: purple border 4 pixels thick around the edge
			pygame.draw.rect(self.surface, BLUE2, (0,0, TILE_WIDTH, TILE_HEIGHT), 2)  #AT: thinner light blue border on top of the purple one so it kinda glows
			pygame.draw.line(self.surface, BLUE, self.line_start, self.line_end, 3)  #AT: draws the blue line going up from the circle
			pygame.draw.circle(self.surface, BLUE, self.center, 15, 3)  #AT: draws the blue circle, 15 is the radius and 3 is how thick the outline is
		else:  #AT: otherwise the tile was already hit
			pygame.draw.rect(self.surface, (0,0,0, 90), (0,0, TILE_WIDTH, TILE_HEIGHT))  #AT: draws a see through black box so you can tell its been hit, the 90 is how see through it is
			
		self.win.blit(self.surface, self.rect)  #AT: stamps the tile canvas onto the game window at the tiles position, without this you wouldnt see it

class Text(pygame.sprite.Sprite):
	def __init__(self, text, font, pos, win):
		super(Text, self).__init__()
		self.win = win

		self.x,self.y = pos
		self.initial = self.y
		self.image = font.render(text, True, (255, 255, 255))

	def update(self, speed):
		self.y += speed
		if self.y - self.initial >= 100:
			self.kill()

		self.win.blit(self.image, (self.x, self.y))

class Counter(pygame.sprite.Sprite):
	def __init__(self, win, font):
		super(Counter, self).__init__()

		self.win = win
		self.font = font
		self.index = 1
		self.count = 3

	def update(self):
		if self.index % 30 == 0:
			self.count -= 1

		self.index += 1

		if self.count > 0:
			self.image = self.font.render(f'{self.count}', True, (255, 255, 255))
			self.win.blit(self.image, (WIDTH//2-16, HEIGHT//2-25))

class Square(pygame.sprite.Sprite):
	def __init__(self, win):
		super(Square, self).__init__()

		self.win = win
		self.color = (255, 255, 255)
		self.speed = 3
		self.angle = 0

		self.side = random.randint(15, 40)
		x = random.randint(self.side, WIDTH-self.side)
		y = 0

		self.surface = pygame.Surface((self.side, self.side), pygame.SRCALPHA)
		self.rect = self.surface.get_rect(center=(x, y))

	def update(self):
		center = self.rect.center
		self.angle = (self.angle + self.speed) % 360
		image = pygame.transform.rotate(self.surface , self.angle)
		self.rect = image.get_rect()
		self.rect.center = center

		self.rect.y += 1.5

		if self.rect.top >= HEIGHT:
			self.kill()

		pygame.draw.rect(self.surface, self.color, (0,0, self.side, self.side), 4)
		pygame.draw.rect(self.surface, (30, 144, 255, 128), (2,2, self.side-4, self.side-4), 2)
		self.win.blit(image, self.rect)

class Button(pygame.sprite.Sprite):
	def __init__(self, img, scale, x, y):
		super(Button, self).__init__()
		
		self.scale = scale
		self.image = pygame.transform.scale(img, self.scale)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

		self.clicked = False

	def update_image(self, img):
		self.image = pygame.transform.scale(img, self.scale)

	def draw(self, win):
		action = False
		pos = pygame.mouse.get_pos()
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] and not self.clicked:
				action = True
				self.clicked = True

			if not pygame.mouse.get_pressed()[0]:
				self.clicked = False

		win.blit(self.image, self.rect)
		return action
