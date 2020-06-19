import pygame
from pygame.locals import *
from entity import EnemyPlan
import Content as con

bong_list = con.bong_list

def move_contrller(hero, emeny_list, screen):
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        elif event.type == KEYDOWN: # 当操作方式为键盘时
            if event.key == K_LEFT or event.key == K_a: #按下左键或者a
                hero.move_left()
            elif event.key == K_RIGHT or event.key == K_d: # 按下右键或者d
                hero.move_right()
            elif event.key == K_DOWN or event.key == K_s: # 按下下键或者s
                hero.move_down()
            elif event.key == K_UP or event.key == K_w: #按下上键或者w
                hero.move_up()
            elif event.key == K_SPACE: # 按下空格键
                hero.fire()
            elif event.key == K_ESCAPE: #按下esc键
                exit()
        elif event.type == MOUSEMOTION: # 当操作方式为鼠标时
            pos = pygame.mouse.get_pos() #获取鼠标坐标
            hero.x = pos[0]-105
            hero.y = pos[1]-50
        elif event.type == MOUSEBUTTONDOWN: # 按下鼠标左键
            pressed_left = pygame.mouse.get_pressed()[0]
            if(pressed_left):
                hero.fire()
        elif event.type == con.CREATE_ENEMY: # 触发创建敌机事件
            emeny_list.append(EnemyPlan.EnemyPlan(screen))
        elif event.type == con.REMOVE_BANG: # 触发移除爆炸效果事件
            if bong_list:
                bong_list.pop(0)