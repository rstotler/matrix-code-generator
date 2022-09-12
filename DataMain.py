import pygame, Column, Utility
from pygame import *

class Load:

	def __init__(self, WINDOW):
	
		self.surfaceBackground = None
		self.columnList = None
		
		self.loadData(WINDOW)
		
	def loadData(self, WINDOW):
	
		# Background Surface #
		self.surfaceBackground = pygame.Surface(Utility.WINDOW_SIZE)
	
		# Column Data #
		self.columnList = []
		for columnNum in range(Utility.WINDOW_SIZE[0] / Utility.COLUMN_WIDTH):
			column = Column.Load(columnNum, self.surfaceBackground)
			self.columnList.append(column)
	
	def update(self, WINDOW, FPS):

		self.getInput()
		
		for column in self.columnList:
			column.update(self.surfaceBackground)
			
		if Utility.DISPLAY_CHECK:
			self.displayScreen(WINDOW, FPS)
			Utility.DISPLAY_CHECK = False
	
	def displayScreen(self, WINDOW, FPS):
		
		WINDOW.fill([0, 0, 0])
		WINDOW.blit(self.surfaceBackground, [0, 0])
		#Utility.write(FPS, [0, 0], Utility.COLOR_DICT["r"], Utility.FONT_DEFAULT, WINDOW)
		
	def getInput(self):

		for event in pygame.event.get():
		
			if event.type == QUIT:
				raise SystemExit
		
			elif event.type == KEYDOWN and event.key == pygame.K_ESCAPE:
				raise SystemExit
				