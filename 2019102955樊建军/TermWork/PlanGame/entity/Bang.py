import pygame

# 爆炸效果类
class Bang():
    def __init__(self, screen, x, y):
        self.x = x + 35
        self.y = y + 5
        self.image = pygame.image.load("image/bong.png")
        self.screen = screen

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))