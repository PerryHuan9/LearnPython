import pygame
from pygame.sprite import Sprite
from Bullet import Bullet
from pygame.sprite import Group


class Alien(Sprite):
    """description of class"""
    def __init__(self, **kwargs):
        super().__init__()
        self.screen=kwargs['screen']
        self.settings=kwargs['settings']
        self.image=pygame.image.load(kwargs['image'])
        self.rect=self.image.get_rect()
        self.x=-float(self.rect.width)
        self.y=float(self.rect.height/2)
        self.rect.x=self.x
        self.rect.y=self.y
        self.is_finish_bullet=False
        #斜率K
        self.k=-(self.settings.screenHeight-200)/self.settings.screenWidth
        self.bullet=None
        self.bullet_number=0

        

    def update(self, *args):
        if self.rect.x<=self.settings.screenWidth-100 and self.y==float(self.rect.height/2):
            self.x+=self.settings.alien_x_speed
        else :
            #self.x=(self.y-self.settings.screenHeight+200)/self.k
            self.y+=self.settings.alien_y_speed
            self.x-=self.settings.alien_x_speed
        self.rect.x=self.x
        self.rect.y=self.y

    def new_bullet(self):
        if self.bullet==None:
            self.bullet=Bullet(self.settings,self.screen,self,self.settings.bullet2)
            self.bullet_number+=1;
        else:
            if self.bullet.rect.y<self.settings.screenHeight:
                self.bullet.rect.y+=self.settings.bullet_speed_factor
                self.bullet.draw_bullet()
            else:
                self.bullet=None

    def update_bullet(self):
        if self.bullet.rect.y<self.settings.screenHeight:
            self.bullet.rect.y+=self.settings.bullet_speed_factor
            self.bullet.draw_bullet()
        else:
            self.bullet=None



    def blitme(self):
        """在指定的位置显示外星人"""
        self.screen.blit(self.image,self.rect)

        


















