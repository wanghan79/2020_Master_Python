import random


def generate_float(float_set):
    '''# 随机生成1000个[0,100]范围内的浮点数'''
    for i in range(1000):
        #添加数据
        float_set.add(random.uniform(0, 100))                                    
        

def generate_str(str_set):
    '''随机生成1000个随机字符串'''
    for i in range(1000):
        #限制位数
        len = random.randint(1, 10)
        #限制位数
        str_set.add(''.join(random.sample('zxcvbnmasdfghjklqwertyuiop', len))) 


def prt_set(data_set):
    '''取出[20,50]之间的数字和包含子串“at”的数据'''
    for item in data_set:
        if ((type(item) is float) and (20.0 <= item <= 50.0)) or ((type(item) is str) and "at" in item):
            print(item)

def main():
    #creat a set
    data_set = set()
    # generate float type data
    generate_float(data_set)
    # generate str type data
    generate_str(data_set)
    # print data   number<20,50> str{at}
    prt_set(data_set)

if __name__ == '__main__':
    main()
