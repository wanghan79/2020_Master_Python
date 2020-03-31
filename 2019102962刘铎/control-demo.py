#1.随机生成1000个[0,100]范围内的浮点随机数，1000个随机字符串，存放在set集合中；
# 2. 使用控制语句遍历这个集合，取出[20,50]之间的数字和包含子串“at”的字符串；
# 3.上述工作分别封装在不同的函数中，并采用主函数完成整体任务流程。下周课上我们根据这个练习讲解控制语句和函数封装相关内容。
import random

def Add(num1,num2):
    a=set()
    for i in range(num1):
        a.add(random.uniform(0,100))
    for i in range(num2):
        randomlength = random.randrange(1, 12)
        random_str = ''
        base_str = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789'
        length = len(base_str) - 1
        for i in range(randomlength):
            random_str += base_str[random.randint(0, length)]
        a.add(random_str)
    return a

def Select(set1):
    for i in set1:
        if isinstance(i,float):
            if i<=50 and i>=20:
                print(i,end=',')
        else:
            if 'at' in i :
                print(i,end=',')

if __name__=='__main__':
    fin=Add(1000,1000)
    Select(fin)

