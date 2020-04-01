import random

#1.随机生成1000个随机浮点数，取出[20,50]之间的数字
def randomFloat(num):
    random_float = set()
    print('大于20并小于50的浮点数:')
    for i in range(num):
        randomFloat = random.uniform(1, 100)
        if randomFloat>= 20 and randomFloat<= 50:
            print(randomFloat)
        random_float.add(randomFloat)


def randomStr(num):  # 2. 1000个随机字符串,输出包含子串“at”的字符串
    random_str = set()
    for i in range(num):#生成1000个字符串
        str = ''
        for j in range(12):
            str += random.choice('abcdefghijklmnopqrstuvwxyz0123456789')  # 随机生成字符串
        random_str.add(str)
    print('包含at的随机字符串：')
    for i in random_str:  # 取出包含at的字符串
        if 'at' in i:
            print(i)

if __name__ == '__main__':
    randomFloat(1000)
    randomStr(1000)