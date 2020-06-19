import Content as con
import pygame

pygame.init()

emeny_list = con.emeny_list

def show_funcName(func):
    def wrapper(*args):
        func(*args)
        print("执行了" + func.__name__ + "函数")
    return wrapper

# 渲染分数显示
@ show_funcName
def show_score(screen):
    text = f"分数：{con.score}"
    score_render =con.font.render(text, True, (0, 255, 0))
    screen.blit(score_render, (10, 17))

# 渲染显示生命值字
@ show_funcName
def show_life(screen, hero):
    text = f"生命值：{hero.life}"
    score_render = con.font.render(text, True, (255, 255, 255))
    screen.blit(score_render, (750, 17))

# 渲染游戏结束字符
@ show_funcName
def gameover(screen, hero):
    if(hero.life == 0):
        emeny_list.clear();
        text = "GAME OVER"
        score_render =con.gameover_font.render(text, True, (255, 0, 0))
        screen.blit(score_render, (200, 450))

# 渲染血槽
def show_lifeRect(screen, hero):
    pygame.draw.rect(screen, (255, 0, 0), (600, 15, 400, 30), 0)
    pygame.draw.rect(screen, (0, 255, 0), (600, 15, hero.life * 4, 30), 0)