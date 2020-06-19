from GameMain import *
import Content as con
from entity import Bullet,Bang
from util import Distance

bullet_list = con.bullet_list

# 我方飞机类
class HeroPlan(object):
    def __init__(self, screen):
        self.x = 385
        self.y = 770
        self.moveNum = 50 # 每次按键移动速度
        self.image = pygame.image.load("image/hero.png")
        self.screen = screen
        self.life = 100 # 我方飞机总血量

    # 显示我方飞机的方法
    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
        for bullet in bullet_list:
            bullet.display()
            bullet.move()
            if bullet.judge():
                bullet_list.remove(bullet)

    # 想左移动的方法
    def move_left(self):
        if self.x > 0:
            self.x -= self.moveNum

    def move_right(self):
        if self.x < 795:
            self.x += self.moveNum

    def move_up(self):
        if self.y > 0:
            self.y -= self.moveNum

    def move_down(self):
        if self.y < 770:
            self.y += self.moveNum

    # 飞机开火的方法
    def fire(self):
        # 向子弹集合中添加子弹
        bullet_list.append(Bullet.Bullet(self.screen, self.x, self.y))
        con.bullet_sound.play()

    # 我方飞机被敌机撞击
    def isHunt(self, emeny_list):
        # 计算每个敌机与我方飞机的距离是否构成撞击
        for enemy in emeny_list:
            if(Distance.distance( self.x, self.y, enemy.x, enemy.y)): # 如果撞击
                self.life -= 10 # 我方飞机血量减10
                emeny_list.remove(enemy) # 敌机坠毁，删除
                con.bang_sound.play() # 播放撞击有效
                bong_list.append(Bang.Bang(enemy.screen, enemy.x - 55, enemy.y - 55)) # 添加爆炸动画效果