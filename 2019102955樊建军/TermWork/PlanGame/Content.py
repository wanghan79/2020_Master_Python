import pygame
#初始化游戏
pygame.init()
#子弹的集合
bullet_list = []
#敌机的集合
emeny_list = []
#爆炸的集合
bong_list = []
#全局变量分数值
score = 0
#设置分数和生命值的字体字号
font = pygame.font.Font('./font/汉仪粗圆简.ttf', 25)
#设定游戏结束字体和字号
gameover_font = pygame.font.Font('./font/汉仪粗圆简.ttf', 100)
#创建敌机自定义事件
CREATE_ENEMY = pygame.USEREVENT+1
pygame.time.set_timer(CREATE_ENEMY,1000)
#移除爆炸效果自定义事件
REMOVE_BANG = pygame.USEREVENT+2
pygame.time.set_timer(REMOVE_BANG,100)
#设定游戏爆炸音效及音量
bang_sound = pygame.mixer.Sound("./music/bang.wav")
bang_sound.set_volume(1)
#设定子弹发射音效及音量
bullet_sound = pygame.mixer.Sound("./music/bullet.wav")
bullet_sound.set_volume(0.7)