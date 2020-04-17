"""
第三次作业 佘浩楠
1.随机生成1000个[0,100]范围内的浮点随机数，1000个随机字符串，存放在set集合中；
2. 使用控制语句遍历这个集合，取出[20,50]之间的数字和包含子串“at”的字符串；
3.上述工作分别封装在不同的函数中，并采用主函数完成整体任务流程
"""


import random


def randomFloat(start, end):
    set_random_float = set()

    for i in range(1000):
        randomFloat = random.uniform(start, end) #生成随机浮点数
        if randomFloat>= 20 and randomFloat<= 50:
            print('[20,50]之间的浮点数： ', randomFloat)
        set_random_float.add(randomFloat) #加入set集合

    print('随机浮点数集合：', set_random_float)
    print('--------------------------------------------------')

def randomStr(num):
    random_float_str = set()

    for i in range(num):#生成1000个字符串
        len = 5#设置每个字符串长度
        str = ''
        for j in range(len):
            str += random.choice('abcdefghijklmnopqrstuvwxyz')  # 随机生成字符串
        random_float_str.add(str)
    set_ramdom_str = set(random_float_str)
    print('随机字符串集合：',set_ramdom_str)

    for i in random_float_str:  #取出包含at的字符串
        if 'at' in i:
            print('包含at的字符串:',i)



if __name__ == '__main__':
    randomFloat(0, 100)
    randomStr(1000)