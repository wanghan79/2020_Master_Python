import random

def randomfloat():
    randnum = set()
    for i in range(1000):
        randnum.add(random.uniform(0,100))
    for num in randnum:
        if(num >= 20 and num <= 50):
            print(num)

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
            print(i)


if __name__ == '__main__':
    randomfloat()
    print('-----------分割线-------------')
    randomstring()