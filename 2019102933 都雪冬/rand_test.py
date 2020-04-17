import random
def rand_Float():
    randnumber = set()
    for i in range(0,1000):
        randnumber.add(random.uniform(0,100))
    for num in randnumber:
        if (num >= 20 and num <= 50):
            print(num,'\r')

def rand_Str():
    randstr = set()
    for i in range(1000):
        len = random.randint(0, 10)
        str = ''
        for j in range(len):
            str += random.choice('abcdefghijklmnopqrstuvwxyz')
        randstr.add(str)
    for i in randstr:
        if 'at' in i:
            print(i)

if  __name__ == '__main__':
    # 生成浮点随机数
    rand_Float()
    print('-----------------------')
    # 生成随机字符串
    rand_Str()