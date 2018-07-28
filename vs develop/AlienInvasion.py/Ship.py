import pygame
from Bullet import *

class Ship():
    """description of class"""
    def __init__(self,screen,settings):
        self.screen=screen
        self.image=pygame.image.load('images/ship.png')
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom
        self.moving_right=False
        self.moving_left=False
        self.moving_down=False
        self.moving_up=False
        self.settings=settings
        #用来保存小数,因为self.rect.centerx是整形
        self.centerx=float(self.rect.centerx)
        self.centery=float(self.rect.centery)
        self.is_bullets=False

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image,self.rect)

    def update(self,settings,screen,bullets):
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.centerx+=self.settings.ship_speed_factor
        if self.moving_left and self.rect.left>0:
            self.centerx-=self.settings.ship_speed_factor
        if self.moving_up and self.rect.top>0:
            self.centery-=self.settings.ship_speed_factor
        if self.moving_down and self.rect.bottom<self.screen_rect.bottom:
            self.centery+=self.settings.ship_speed_factor
        self.rect.centerx=self.centerx
        self.rect.centery=self.centery
        #if self.is_bullets:
        #     
   

        



















