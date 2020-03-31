import random

# 随机生成1000个[0,100]范围内的浮点随机数
def randomfloat(float_set):
    for i in range(1000):
        float_set.add(random.uniform(0, 100))
        #random.uniform(a, b)，用于生成一个指定范围内的随机浮点数，两个参数其中一个是上限，一个是下限。

# 随机生成1000个随机字符串
def randomstr(str_set):
    for i in range(1000):
        len = random.randint(1, 10)
        #random.randint(a, b)，用于生成一个指定范围内的整数，其中参数a是下限，参数b是上限。
        str_set.add(''.join(random.sample('abcdefghijklmnopqrstuvwxyz', len)))

# 使用控制语句遍历集合，取出[20,50]之间的数字和包含子串“at”的字符串
def deal_set(data_set):
    for i in data_set:
        if ((type(i) is float) and (20.0 <= i <= 50.0)) or ((type(i) is str) and "at" in i):
            print(i)

def main():
    data_set = set()# 定义set
    randomfloat(data_set)# 生成并添加浮点数元素
    randomstr(data_set)# 生成并添加字符串元素
    deal_set(data_set)# 控制输出[20,50]之间的数字和包含子串“at”的字符串

if __name__ == '__main__':
    main()
