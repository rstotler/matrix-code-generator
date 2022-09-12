import pygame
from pygame import *
pygame.init()

# Utility Functions #
def loadColorDict():

	codeDict = {"lr":[255, 80,  80],  "r":[255, 0,   0],   "dr":[125, 0,   0],   "ddr":[80,  0,   0],
				"lo":[255, 150, 75],  "o":[255, 100, 0],   "do":[150, 75,  0],   "ddo":[80,  40,  0],
				"ly":[255, 255, 80],  "y":[255, 255, 0],   "dy":[125, 125, 0],   "ddy":[80,  80,  0],
				"lg":[80,  255, 80],  "g":[0,   255, 0],   "dg":[0,   125, 0],   "ddg":[0,   60,  0],
				"lc":[80,  255, 255], "c":[0,   255, 255], "dc":[0,   125, 125], "ddc":[0,   80,  80],
				"lb":[80,  80,  255], "b":[0,   0,   255], "db":[0,   0,   125], "ddb":[0,   0,   80],
				"lv":[255, 80,  255], "v":[255, 0,   255], "dv":[125, 0,   125], "ddv":[80,  0,   80],
				"lm":[175, 80,  255], "m":[175, 0,   255], "dm":[75,  0,   125], "ddm":[75,  0,   80],
				"lw":[255, 255, 255], "w":[255, 255, 255], "dw":[200, 200, 200], "ddw":[150, 150, 150],
				"la":[150, 150, 150], "a":[150, 150, 150], "da":[100, 100, 100], "dda":[70,  70,  70],
				"x":[0, 0, 0]}
				
	return codeDict

def write(LABEL, LOCATION, COLOR, FONT, WINDOW):

	text = FONT.render(LABEL, True, COLOR)
	WINDOW.blit(text, LOCATION)
	
# Variables #
WINDOW_SIZE = [800, 600]
ALPHABET = "abcdefghijklmnopqrstuvwxyz"
FONT_SIZE = 24
FONT_DEFAULT = pygame.font.Font("Monofur.ttf", FONT_SIZE)
FONT_MATRIX = pygame.font.Font("Matrix.ttf", FONT_SIZE)
COLOR_DICT = loadColorDict()
COLUMN_WIDTH = FONT_MATRIX.size("x")[0] + 2
DISPLAY_CHECK = True
