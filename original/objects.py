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
# AT: Same tile size as main.py. objects.py is a separate file, so the Tile class
#     needs its own copy of these numbers.
TILE_WIDTH = WIDTH // 4
TILE_HEIGHT = 130

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (30, 144, 255)
BLUE2 = (2, 239, 239)
PURPLE = (191, 64, 191)

# AT: Tile is one black piano tile. It's built on pygame's Sprite so it can be put
#     in a Group (tile_group in main.py) and remove itself with kill().
class Tile(pygame.sprite.Sprite):
	# AT: Runs once when a tile is created. x and y are where it starts
	#     (x picks the column), and win is the game window it draws on.
	def __init__(self, x, y, win):
		# AT: Run Sprite's own setup first, otherwise the tile can't join a sprite Group.
		super(Tile, self).__init__()

		self.win = win
		# AT: Saves the starting position. It's never used again: rect below is what
		#     actually tracks where the tile is.
		self.x, self.y = x, y
		self.color = BLACK
		# AT: alive = True means 'not hit yet'. It becomes False when the player hits the
		#     tile, which makes it fade and stops it counting as a miss at the bottom.
		self.alive = True

		# AT: A blank, tile-sized canvas to draw the tile on. SRCALPHA allows
		#     see-through colours, needed for the faded look of a hit tile.
		self.surface = pygame.Surface((TILE_WIDTH, TILE_HEIGHT), pygame.SRCALPHA)
		# AT: rect stores the tile's position and size. Moving the tile just means
		#     changing rect.y; main.py also uses rect for clicks and the bottom check.
		self.rect = self.surface.get_rect()
		self.rect.x = x
		self.rect.y = y

		# AT: Points for the blue circle and line drawn in the middle of the tile.
		#     Only decoration, they don't affect the gameplay.
		self.center = TILE_WIDTH//2, TILE_HEIGHT//2 + 15
		self.line_start = self.center[0], self.center[1]-18
		self.line_end = self.center[0], 20

	# AT: Called every frame from main.py with the current speed.
	def update(self, speed):
		# AT: Move the tile down. In pygame a bigger y is lower on the screen.
		self.rect.y += speed
		# AT: Once the tile has gone off the bottom, delete it so thousands of
		#     invisible tiles don't pile up below the screen and slow the game down.
		if self.rect.y >= HEIGHT:
			self.kill()

		# AT: Not hit yet: draw it black with a purple and a cyan border, plus the blue
		#     line and circle in the middle.
		if self.alive:
			pygame.draw.rect(self.surface, self.color, (0,0, TILE_WIDTH, TILE_HEIGHT))
			pygame.draw.rect(self.surface, PURPLE, (0,0, TILE_WIDTH, TILE_HEIGHT), 4)
			pygame.draw.rect(self.surface, BLUE2, (0,0, TILE_WIDTH, TILE_HEIGHT), 2)
			pygame.draw.line(self.surface, BLUE, self.line_start, self.line_end, 3)
			pygame.draw.circle(self.surface, BLUE, self.center, 15, 3)
		# AT: Already hit: cover it with see-through black (alpha 90) so it looks faded.
		#     Note: the canvas isn't cleared first, so this layer stacks up every frame and the
		#     tile gets darker. In our version we clear it with surface.fill((0, 0, 0, 0)) first.
		else:
			pygame.draw.rect(self.surface, (0,0,0, 90), (0,0, TILE_WIDTH, TILE_HEIGHT))
			
		# AT: Stamp the tile's canvas onto the game window at the tile's position.
		#     Nothing is visible until this line runs.
		self.win.blit(self.surface, self.rect)

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
