import pygame

class Ship():

	def __init__(self, ai_settings, screen):

		self.screen = screen
		self.ai_settings = ai_settings

		self.image = pygame.image.load("Images/Galaga_white.bmp")
		self.rect = self.image.get_rect()

		# centre the ship at the bottom centre of the screen
		self.screen_rect = screen.get_rect()
		self.rect.centerx = self.screen_rect.centerx
		self.rect.centery = self.screen_rect.centery
		self.rect.bottom = self.screen_rect.bottom
		self.centerx = float(self.rect.centerx)
		self.centery = float(self.rect.centery)

		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False

		self.bullets_fired = 0
		self.bullets_hit = 0

	def blitme(self):

		self.screen.blit(self.image, self.rect)

	def update(self):

		# movement of ship
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.centerx += self.ai_settings.ship_speed_factor

		if self.moving_left and self.rect.left > 0:
			self.centerx -= self.ai_settings.ship_speed_factor

		if self.moving_up and self.rect.top > 0:
			self.centery -= self.ai_settings.ship_speed_factor

		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.centery += self.ai_settings.ship_speed_factor

		# update rect object
		self.rect.centerx = self.centerx
		self.rect.centery = self.centery