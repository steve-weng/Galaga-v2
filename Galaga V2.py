import sys
import pygame
from Settings import Settings

def init_game():

	pygame.init()
	game_settimgs = Settings()
	window = pygame.display.set_mode(
		(game_settings.screen_width, game_settings.screen_height))
	pygame.display.set_caption("Galaga V2")

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

		window.fill(game_settings.bg_col)
		pygame.display.flip()

init_game()