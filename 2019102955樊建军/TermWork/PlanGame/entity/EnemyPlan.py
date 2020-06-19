import random
import pygame

class EnemyPlan(object):
    def __init__(self, screen):
        # pygame.sprite.Sprite.__init__(self)
        self.x = random.uniform(0, 950)
        self.y = -100
        self.image = pygame.image.load("image/emeny" + str(random.randint(1, 6)) + ".png")
        self.screen = screen

    # 显示敌机的方法
    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    # 敌机以1-10的随机速度下降
    def move(self):
        self.y += random.uniform(1, 10)