import random

def randNum():
    s1 = []

    for i in range(0,1000):
        num = random.uniform(0,100)
        if num >= 20 and num <= 50:
            s1.append(num)

    print('[20,50]之间的数字集合为：',s1,end = " ")

def randStr():
    s2 = []

    for i in range(1000):
        s = ''
        for j in range(8):
            s += random.choice('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890')
        s2.append(s)

    for i in s2:
        if 'at' in i:
            print(i, end = '  ')

#主函数
if __name__ == '__main__':
    randNum()
    print('')
    randStr()
