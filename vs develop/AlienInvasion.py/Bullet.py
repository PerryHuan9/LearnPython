import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """description of class"""
    def __init__(self,settings,screen,ship,image):
        super(Bullet,self).__init__()
        self.screen=screen
        self.image=pygame.image.load(image)
        #self.rect=pygame.Rect(0,0,settings.bullet_width,settings.bullet_height)
        self.rect=self.image.get_rect()
        self.rect.centerx=ship.rect.centerx
        self.rect.top=ship.rect.top
        self.y=float(self.rect.y)
        self.x=float(self.rect.x)
        self.color=settings.bullet_color
        self.speed_factor=settings.bullet_speed_factor
    
    def update(self):
        self.y-=self.speed_factor
        self.rect.y=self.y
        

    def draw_bullet(self):
        #pygame.draw.rect(self.screen,self.color,self.rect)
        self.screen.blit(self.image,self.rect)































