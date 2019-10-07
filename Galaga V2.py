import pygame
from Settings import Settings
from Plane import Plane
import game_functions as gf

def init_game():

	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Galaga V2")

	plane = Plane(screen)

	while True:
		gf.check_events()
		gf.update_screen(ai_settings, screen, plane)

init_game()