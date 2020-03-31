import random

# 随机生成1000个[0,100]范围内的浮点随机数
def generate_float(float_set):
    for i in range(1000):
        float_set.add(random.uniform(0, 100))
    # return float_set

# 随机生成1000个随机字符串
def generate_str(str_set):
    for i in range(1000):
        len = random.randint(1, 10)
        str_set.add(''.join(random.sample('zyxwvutsrqponmlkjihgfedcba', len)))

# 使用控制语句遍历集合，取出[20,50]之间的数字和包含子串“at”的字符串
def deal_set(data_set):
    for item in data_set:
        if ((type(item) is float) and (20.0 <= item <= 50.0)) or ((type(item) is str) and "at" in item):
            print(item)

def main():
    # 1、定义set
    data_set = set()
    # 2、生成并添加浮点数元素
    generate_float(data_set)
    # 3、生成并添加字符串元素
    generate_str(data_set)
    # 4、控制输出[20,50]之间的数字和包含子串“at”的字符串
    deal_set(data_set)

if __name__ == '__main__':
    main()