import pygame, Utility, DataMain
from pygame import *

pygame.init()
window = pygame.display.set_mode(Utility.WINDOW_SIZE, False, 0)
pygame.display.set_caption("PyMatrix by ParticleMan")
clock = pygame.time.Clock()
dataMain = DataMain.Load(window)

while True:

	lastTick = clock.tick(60) / 1000.0
	dataMain.update(window, str(clock.get_fps())[:5])
	pygame.display.flip()
