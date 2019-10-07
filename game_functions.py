import sys
import pygame

# responds to keypresses and mouse events
def check_events():
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

# updates game screen
def update_screen(ai_settings, screen, plane):

	screen.fill(ai_settings.bg_color)
	plane.blitme()
	pygame.display.flip()