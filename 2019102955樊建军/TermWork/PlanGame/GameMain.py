import pygame
import os
from entity import HeroPlan
import Content as con
import EventController as ec
import View as view

#初始化游戏
pygame.init()

#获取Content中的全局集合变量
bullet_list = con.bullet_list
emeny_list = con.emeny_list
bong_list = con.bong_list

def main():
    #设置窗口启动初始位置
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (30,40)
    #创建窗体
    screen = pygame.display.set_mode((1006, 937), 0, 32)
    #设置游戏名称
    pygame.display.set_caption("飞机大战")
    #设置背景音乐
    pygame.mixer.music.load("music/background.mp3")
    pygame.mixer.music.set_volume(0.42)
    pygame.mixer.music.play(-1)
    #设置刷新时钟频率
    clock = pygame.time.Clock()
    #创建背景图片
    backgroundPath = "image/background.jpg"
    background = pygame.image.load(backgroundPath)
    #创建飞机
    hero = HeroPlan.HeroPlan(screen)

    while True:
        # 设置背景图片
        screen.blit(background, (0, 0))
        # 设置飞机图片
        hero.display()
        # 控制飞机
        ec.move_contrller(hero, emeny_list, screen)
        for emeny in emeny_list:
            # 显示敌机
            emeny.display()
            # 敌机向下移动
            emeny.move()
            # 移除越界敌机
            if(emeny.y > 937):
                emeny_list.remove(emeny)


        # 子弹击中敌机
        for bullet in bullet_list:
            bullet.fit()
        # 被敌机撞击
        hero.isHunt(emeny_list)
        # 显示爆炸烟花
        for bong in bong_list:
            bong.display()
        # 显示成绩
        view.show_score(screen)
        # 显示血槽1
        view.show_lifeRect(screen,hero)
        # 显示血槽2
        view.show_life(screen,hero)
        # 显示游戏结束
        view.gameover(screen, hero)
        # 更新游戏画面
        pygame.display.update()
        clock.tick(30)

if __name__ == '__main__':
    main()