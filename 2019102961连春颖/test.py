"""
1.随机生成1000个[0,100]范围内的浮点随机数，1000个随机字符串，存放在set集合中；
2. 使用控制语句遍历这个集合，取出[20,50]之间的数字和包含子串“at”的字符串；
3.上述工作分别封装在不同的函数中，并采用主函数完成整体任务流程
"""

#encoding=UTF-8
import random
import string

def randomnum():#输出20到50的随机浮点数
    a=set() #建立空集合存放筛选过的浮点数
    b =set()#建立空集合存全部的浮点数
   # set = {random.uniform(0, 100) for i in range(1000)}
    for i in range(0, 1000): #生成1000个浮点数
        num = random.uniform(0, 100) # 生成的随机浮点数归一化到区间0-100
        b.add(num) #添加到集合里
        if num >= 20 and num <= 50: #如过浮点数在20到50 之间就添加到集合a中
            a.add(num)
    #print(b)输出所有的
    print(a)


def str():#输出有'at'的字符
    a = set()#建立空集合存全部的随机字符串
    b =set()#建立空集合存放有字符‘at’的字符串
    for i in range(1000):#生成1000个字符串
       long = random.randrange(10) #随机生成0到9的整数，确定的是随机输出的字符串中的字符个数，每次都不一样
       value = ''.join(random.sample(string.ascii_letters + string.digits,long))#ascii_letters是生成所有字母，从a-z和A-Z,digits是生成所有数字0-9.#以空字符串返回一个拼接各个元素后生成的字符串
       a.add(value) #添加到集合里
    #print(a) 输出所有的
    for j in a:#遍历集合a
        if 'at' in j: #如果在集合a中有”at‘字符就把这个字符串添加到集合b中，循环结束后输出
            b.add(j)#添加到集合里
    print(b)


def main():
    randomnum()
    str()


if __name__ == "__main__":

    main()

