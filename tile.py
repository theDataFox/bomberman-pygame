import config, pygame

class Tile(pygame.sprite.Sprite):
	def __init__(self,type):
		pygame.sprite.Sprite.__init__(self)
		self.c = config.Config()
		self.type = type

		self.bomb = None
		self.powerup = None

		self.setPowerup()
		self.setAttributes()
	
	# RFCT
	def setPowerup(self):
		if self.type == self.c.BOMB_UP:
			self.powerup = self.c.BOMB_UP
			self.type = self.c.BRICK
		elif self.type == self.c.POWER_UP:
			self.powerup = self.c.POWER_UP
			self.type = self.c.BRICK

	def isPowerUp(self):
		return self.type in [self.c.POWER_UP, self.c.BOMB_UP]

	def setAttributes(self):
		if self.type == self.c.GROUND:
			self.passable = True 
			self.destroyable = False
		elif self.type == self.c.BRICK:
			self.passable = False
			self.destroyable = True
		elif self.type == self.c.WALL:
			self.passable = False
			self.destroyable = False
		elif self.type in [self.c.BOMB_UP, self.c.POWER_UP]:
			self.passable = True
			self.destroyable = True

		self.image = pygame.image.load(self.c.IMAGE_PATH + "tiles/" + str(self.type) + ".png").convert()
	
	def destroy(self):
		if self.powerup is None:
			self.type = self.c.GROUND
		else:
			self.type = self.powerup
			self.powerup = None
		self.setAttributes()
	
	# RFCT
	def canBombPass(self):
		if self.type in [self.c.BOMB_UP, self.c.POWER_UP]:
			return False
		return self.passable & (self.bomb == None)

	def canPass(self):
		return self.passable & (self.bomb == None)

	def getBackground(self):
		return self.image

	def getImage(self):
		if self.bomb != None:
			return self.bomb.image
		return self.image

	def __str__(self):
		return str(self.type)
