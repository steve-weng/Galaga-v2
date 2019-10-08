import pygame
from pygame.sprite import Group
from settings import settings
from ship import Ship
import game_functions as gf

def init_game():

	pygame.init()
	ai_settings = settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Galaga V2")

	ship = Ship(ai_settings, screen)
	bullets = Group()

	while True:
		gf.check_events(ai_settings, screen, ship, bullets)
		ship.update()
		gf.update_bullets(bullets)
		gf.update_screen(ai_settings, screen, ship, bullets)

init_game()