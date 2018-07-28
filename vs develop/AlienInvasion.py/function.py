import sys
import pygame
from Bullet import *
from Alien import *
import random
from Ship import *
from time import sleep


def check_keydown_events(screen,settings,event,ship,bullets):
    """监听按键按下事件"""
    if event.type==pygame.KEYDOWN:
        if event.key==pygame.K_RIGHT:
            ship.moving_right=True
        elif event.key==pygame.K_LEFT:
            ship.moving_left=True
        elif event.key==pygame.K_UP:
            ship.moving_up=True
        elif event.key==pygame.K_DOWN:
            ship.moving_down=True
        elif event.key==pygame.K_SPACE:
            ship.is_bullets=True
            new_bullet=Bullet(settings,screen,ship,settings.bullet1)
            bullets.add(new_bullet)
        elif event.key==pygame.K_q:
            sys.exit()
           
            

def check_keyup_events(screen,settings,event,ship,bullets):
    """监听键盘按键松开事件"""
    if event.type==pygame.KEYUP:
        if event.key==pygame.K_RIGHT:
            ship.moving_right=False
        elif event.key==pygame.K_LEFT:
            ship.moving_left=False
        elif event.key==pygame.K_UP:
            ship.moving_up=False
        elif event.key==pygame.K_DOWN:
            ship.moving_down=False
        elif event.key==pygame.K_SPACE:
            ship.is_bullets=False

 
def check_event(settings,ship,screen,bullets):
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
	        sys.exit()
        check_keydown_events(screen,settings,event,ship,bullets)
        check_keyup_events(screen,settings,event,ship,bullets)
       
         
def update_bullets(bullets):
    bullets.update()
    for bullet in bullets.copy(): 
        if bullet.rect.bottom<=0:
            bullets.remove(bullet)

           
def create_fleet(settings,screen,aliens,reverse=False):
    """创建外星飞船队伍"""
    alien=Alien(screen=screen,settings=settings,image=settings.alien_image_4)
    alien_width=alien.rect.width
    space_x=settings.screenWidth-alien_width
    alien_space=2*alien_width
    number_aliens_x=int(space_x/alien_space)
    for alien_number in range(number_aliens_x):
        if reverse:
            alien=Alien(screen=screen,settings=settings,image=settings.alien_image_3)
            alien.x=settings.screenWidth+alien_space*alien_number
            settings.is_forward=False
        else:
            alien=Alien(screen=screen,settings=settings,image=settings.alien_image_4)
            alien.x=-alien_width-alien_space*alien_number
            settings.is_forward=True
        alien.rect.x=alien.x
        aliens.append(alien)

def update_forward_aliens(aliens,settings,screen):
    """更新从左往右的外星飞船的位置"""
    for alien in aliens:
        if alien.rect.x<(settings.screenWidth-100) and alien.y==float(alien.rect.height/2):
            alien.x+=settings.alien_x_speed
        else:
            if aliens[0].rect.x>40:
                alien.y+=settings.alien_y_speed
                alien.x-=settings.alien_x_speed
            else:
                if aliens[-1].bullet_number<=3:
                    alien.new_bullet()
                else:
                    alien.y+=settings.alien_y_speed
                    #alien.update_bullet()
        alien.rect.x=alien.x
        alien.rect.y=alien.y
    


def update_reverse_aliens(aliens,settings,screen):
    """更新从右往左的外星飞船的位置"""
    for alien in aliens:
        if alien.rect.x>=0 and alien.y==float(alien.rect.height/2):
            alien.x-=settings.alien_x_speed
        else:
            if aliens[0].rect.x<settings.screenWidth-100:
                alien.y+=settings.alien_y_speed
                alien.x+=settings.alien_x_speed
            else:
                if aliens[-1].bullet_number<=3:
                   alien.new_bullet()
                else:
                    alien.y+=settings.alien_y_speed
                    #alien.update_bullet()
        alien.rect.x=alien.x
        alien.rect.y=alien.y
    


def update_aliens(aliens,settings,screen):
    """更新外星飞船的位置"""
    if settings.is_forward:
        update_forward_aliens(aliens,settings,screen)
        if len(aliens)==0 or aliens[-1].rect.y>settings.screenHeight:
            aliens.clear()
            create_fleet(settings,screen,aliens,reverse=True)
    else:
        update_reverse_aliens(aliens,settings,screen)
        if len(aliens)==0 or aliens[-1].rect.y>settings.screenHeight:
            aliens.clear()
            create_fleet(settings,screen,aliens,reverse=False)

def check_collide(aliens,bullets):
    """监测子弹和外星飞船的碰撞"""
    if aliens==None or bullets==None:
        return
    for alien in aliens.copy():
        alien_x=alien.rect.x
        alien_y=alien.rect.y
        for bullet in bullets.copy():
            if bullet.rect.x>=alien_x and bullet.rect.x<=alien_x+alien.rect.width and bullet.rect.y>=alien_y and bullet.rect.y<=alien_y+alien.rect.height:
                bullets.remove(bullet)
                aliens.remove(alien)
                break

def ship_died(ship,aliens,bullets,screen):
    """飞船死亡后的处理"""
    sleep(1)
    aliens.clear()
    bullets.clear(screen,None)
    ship.centerx=ship.screen_rect.centerx
    ship.centery=ship.screen_rect.bottom-50

def check_collide_ship(aliens,ship,screen,settings,bullets):
    """外星飞船撞击飞船"""
    if aliens==None:
        return
    for alien in aliens.copy():
        alien_x=alien.rect.x
        alien_y=alien.rect.y
        if ship.rect.x>=alien_x and ship.rect.x<=alien_x+alien.rect.width and ship.rect.y>=alien_y and ship.rect.y<=alien_y+alien.rect.height  :
            ship_died(ship,aliens,bullets,screen)
            break





def update_screen(screen,ship,settings,bullets,**args):
    """屏幕更新事件"""
    screen.fill(settings.bgColor)
    ship.update(settings,screen,bullets)
    update_bullets(bullets)
    bullets.draw(screen)
    #for bullet in bullets.sprites():
    #    bullet.draw_bullet()
    ship.blitme()
    #for alien in args['aliens']:
    #    alien.update()
    update_aliens(args['aliens'],settings,screen)
    for alien in args['aliens']:
        #alien.update()
        alien.blitme()
    check_collide(args['aliens'],bullets)
    check_collide_ship(args['aliens'],ship,screen,settings,bullets)
    #collisions=pygame.sprite.groupcollide(bullets,args['aliens'],True,True)
    pygame.display.flip()












