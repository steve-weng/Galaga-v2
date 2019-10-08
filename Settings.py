# this module stores all settings for Galaga V2

class settings():
	
	def __init__(self):

		# background screen
		self.screen_width = 800
		self.screen_height = 600
		self.bg_color = (200, 200, 200)

		# ship settings
		self.ship_speed_factor = 1.5

		# bullets
		self.bullet_speed_factor = 1.2
		self.bullet_width = 1
		self.bullet_height = 12
		self.bullet_color = 60, 60, 60
		self.bullets_allowed = 10
