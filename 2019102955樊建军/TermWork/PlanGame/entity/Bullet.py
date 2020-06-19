import pygame
import Content as con
from entity import Bang
from util import Distance

bullet_list = con.bullet_list
emeny_list = con.emeny_list
bong_list = con.bong_list

# 子弹类
class Bullet():
    def __init__(self, screen, x, y):
        self.x = x + 35
        self.y = y + 5
        self.moveNum = 10
        self.image = pygame.image.load("image/bullet.png")
        self.screen = screen

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    # 子弹向上移动方法
    def move(self):
        self.y -= 10

    #判断子弹是否出界
    def judge(self):
        if self.y < -81:
            return True
        else:
             return False

    # 子弹击中敌机
    def fit(self):
        for enemy in emeny_list:
            for bullet in bullet_list:
                if (Distance.distance(bullet.x, bullet.y, enemy.x, enemy.y)): # 如果子弹和敌机相撞
                    emeny_list.remove(enemy) # 则移除敌机
                    bullet_list.remove(bullet) # 也移除子弹
                    con.bang_sound.play() # 播放爆炸音效
                    con.score += 5 #分数+5
                    bong_list.append(Bang.Bang(enemy.screen, enemy.x - 55, enemy.y - 55)) # 添加爆炸效果