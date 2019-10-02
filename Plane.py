import pygame

class Plane():

	def __init__(self, screen):
		self.screen = screen

		self.image = pygame.image.load("Images/Galaga_white.png")
		self.rect = self.image.get_rect()

		# centre the plane at the bottom centre of the screen
		self.screen_rect = screen.get_rect()
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

	def blitMe(self):
		self.screen.blit(self.image, self.rect)