import sys
import pygame

def run_game():
	pygame.init()
	screen=pygame.display.set_mode((700,500))
	pygame.display.set_caption('Alien Invasion')
	bgColor=(230,200,0)
	screen.fill(bgColor)
	while True:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				sys.exit()

	

		pygame.display.flip()
		
	
run_game()
		
