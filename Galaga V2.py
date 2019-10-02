import sys
import pygame
from Settings import Settings
from Plane import Plane

def init_game():

	pygame.init()
	game_settings = Settings()
	screen = pygame.display.set_mode(
		(game_settings.screen_width, game_settings.screen_height))
	pygame.display.set_caption("Galaga V2")

	plane = Plane(screen)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

		screen.fill(game_settings.bg_col)
		plane.blitMe()

		pygame.display.flip()

init_game()