import random
import string


def randomFloat(start, end):
    # 1000个随机浮点数,取出[20,50]之间的数字，并放在集合中
    set_random_float = set()
    for i in range(1000):
        randomFloat = random.uniform(start, end)
        if randomFloat >= 20 and randomFloat <= 50:
            print('在20与50之间的浮点数：', randomFloat)
        set_random_float.add(randomFloat)
    # print('随机浮点数集合：', set_random_float)


def randomStr(num):
    # 1000个随机字符串,输出包含at的字符串
    set_random_str = set()
    str_content = string.ascii_letters + string.digits + string.punctuation
    for i in range(num):
        str = ''
        for j in range(10):  # 字符串长度为10
            random_Str = random.choice(str_content)  # 随机生成字符串
            str += random_Str
        set_random_str.add(str)
    set_str = set(set_random_str)
        # print('随机字符串：',set_str)
    for i in set_str:
        if 'at' in i:
            print('包含at的字符串：')
            print(i)


if __name__ == '__main__':
    randomFloat(0, 100)
    randomStr(1000)
