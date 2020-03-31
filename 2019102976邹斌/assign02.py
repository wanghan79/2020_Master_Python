#!python3.8
#assign02.py: generate 1000 numbers of float and 1000 strings

#random.uniform(a, b) 生成随机浮点数, a <= N <=b for a <= b and b<=N<=a for b < a
#random.randint(a, b) 生成随机整数 a <= N <= b

import random

lenOfNum = 1000
lenOfStr = 1000
num_range = 100
contents = set()
letters = []
def randow_num():               #生成1000个随机数,并加入set
    global contents
    for i in range(lenOfNum):
        num = random.uniform(0, num_range)
        contents.add(round(num, 2))

def random_string():     #生成1000个随机字符串,由[a-zA-Z]组成,并加入set
    global letters
    global contents
    l = len(letters) - 1
    for i in range(lenOfStr):
        letter_len = random.randint(0, 10) #随机获取字符串长度 字符串长度0-10
        str = ''
        for j in range(letter_len):
            index = random.randint(0,  l)
            str += letters[index]
        contents.add(str)

def create_table():             #生成字母表[a-zA-Z]
    global letters #test
    for i in range(65, 91):
        letters.append(chr(i))
    for i in range(97, 123):
        letters.append(chr(i))

create_table()
randow_num()
random_string()

for item in contents:
    if str(item).isalpha():
        if 'at' in item:
            print('The target string is %s' % (item))
    elif item != '':
        if 20 <= float(item) <= 50:
            print('The target number is %s' % (item))

