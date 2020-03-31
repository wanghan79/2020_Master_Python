import random

def randomFloat(start, end): #1.随机生成1000个[0,100]范围内的浮点随机数，取出[20,50]之间的数字，存放在set集合中
    set_random_float = set()
    for i in range(1000):
        randomFloat = random.uniform(start, end)                           #生成随机浮点数
        if randomFloat>= 20 and randomFloat<= 50:
            print('小于20并大于50的浮点数： ', randomFloat)
        set_random_float.add(randomFloat)                #加入集合
    print('随机浮点数集合：', set_random_float)


def randomStr(num):  # 2. 1000个随机字符串,输出包含子串“at”的字符串
    random_float_str = set()
    for i in range(num):#生成1000个字符串
        len = 10#每个字符串长度为10
        str = ''
        for j in range(len):
            str += random.choice('abcdefghijklmnopqrstuvwxyz')  # 随机生成字符串
        random_float_str.add(str)
    set_ramdom_str = set(random_float_str)
    print('随机字符串：',set_ramdom_str)
    for i in random_float_str:  # 取出包含at的字符串
        if 'at' in i:
            print(i)



if __name__ == '__main__':  #3.封装后使用主函数
    randomFloat(0, 100)
    randomStr(1000)
