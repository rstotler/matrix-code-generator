import pygame, random, Utility
from pygame import *

class Load:

	def __init__(self, COLUMN_NUM, BACKGROUND_SURFACE):
	
		self.columnNum = COLUMN_NUM
		self.surface = None
		self.surfaceBlack = None
		self.charString = ""
		self.trailIndex = random.randrange(-100, -25)
		self.trailEndIndex = random.randrange(50, 75)
		self.trailTick = 0
		self.trailTickMax = 4
		self.trailSize = random.randrange(12, 25)
		self.trailLightSize = random.randrange(5, 10)
		
		self.loadVariables(BACKGROUND_SURFACE)
		
	def loadVariables(self, BACKGROUND_SURFACE):
	
		# Load Surface #
		self.surface = pygame.Surface([Utility.COLUMN_WIDTH, Utility.WINDOW_SIZE[1]])
		self.surfaceBlack = pygame.Surface([Utility.COLUMN_WIDTH, Utility.FONT_SIZE])
		self.surfaceBlack.fill([0, 0, 0])
	
		# Generate Random Character List #
		for charNum in range(Utility.WINDOW_SIZE[1] / Utility.FONT_SIZE):
			randomChar = random.choice(Utility.ALPHABET)
			self.charString = self.charString + randomChar
			
		# Draw Column Surface To Background Surface #
		surfaceLoc = [3 + (self.columnNum * self.surface.get_width()), 6]
		BACKGROUND_SURFACE.blit(self.surface, surfaceLoc)
	
	def update(self, BACKGROUND_SURFACE):
	
		self.trailTick += 1
		if self.trailTick >= self.trailTickMax:
			self.trailIndex += 1
			self.trailTick = 0
			self.updateSurface(BACKGROUND_SURFACE)
			Utility.DISPLAY_CHECK = True
			
			if self.trailIndex - self.trailSize >= self.trailEndIndex:
				self.trailIndex = 0
			
	def updateSurface(self, BACKGROUND_SURFACE):
	
		if self.trailIndex >= 0 and self.trailIndex - self.trailSize < len(self.charString):
		
			if self.trailIndex >= self.trailSize:
				surfaceBlackY = Utility.FONT_SIZE * (self.trailIndex - self.trailSize)
				self.surface.blit(self.surfaceBlack, [0, surfaceBlackY])
			
			for cNum in range(self.trailLightSize + 1):
				charNum = self.trailIndex - cNum
				if charNum >= 0 and charNum < len(self.charString):
					targetChar = self.charString[charNum]
					if cNum == 0 : targetColor = Utility.COLOR_DICT["w"]
					elif cNum == self.trailLightSize : targetColor = Utility.COLOR_DICT["dg"]
					else : targetColor = Utility.COLOR_DICT["g"]
					yLoc = Utility.FONT_SIZE * charNum
					Utility.write(targetChar, [1, yLoc], targetColor, Utility.FONT_MATRIX, self.surface)
					
			surfaceLoc = [3 + (self.columnNum * self.surface.get_width()), 6]
			BACKGROUND_SURFACE.blit(self.surface, surfaceLoc)
				