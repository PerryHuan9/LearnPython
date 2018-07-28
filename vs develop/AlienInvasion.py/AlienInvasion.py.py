import pygame
from Settings import Settings
from function import *
from pygame.sprite import Group
from Alien import *

def run_game():
    pygame.init()
    settings=Settings()
    screen=pygame.display.set_mode((settings.screenWidth,settings.screenHeight))
    pygame.display.set_caption('Alien Invasion')
    ship=Ship(screen,settings)
    bullets=Group()
    aliens=[]
    
    create_fleet(settings,screen,aliens)
    #print(len(aliens))
    while True:
        check_event(settings,ship,screen,bullets)
        update_screen(screen,ship,settings,bullets,aliens=aliens)
       
       
		
is_forward=True 	
run_game()












































