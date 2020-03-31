import random

def randomfloat():
    randnumber = set()
    for i in range(1000):
        randnumber.add(random.uniform(0,100))
    for num in randnumber:
        if(num >= 20 and num <= 50):
            print(num, '\r')

def randomstring():
    randstr = set()
    for i in range(1000):
        len = random.randint(1,10)
        str = ''
        for j in range(len):
            str += random.choice('abcdefghijklmnopqrstuvwxyz')
        randstr.add(str)
    for i in randstr:
        if 'at' in i:
            print(i,'\r')


if __name__ == '__main__':
    #生成随机浮点数
    randomfloat()
    print('------------------------')
    #生成随机字符串
    randomstring()