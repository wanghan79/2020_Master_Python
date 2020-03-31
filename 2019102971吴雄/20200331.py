'''
#wuxiong 2020/3/31 14:00
1.随机生成1000个[0,100]范围内的浮点随机数，1000个随机字符串，存放在set集合中；
2. 使用控制语句遍历这个集合，取出[20,50]之间的数字和包含子串“at”的字符串；
3.上述工作分别封装在不同的函数中，并采用主函数完成整体任务流程。
'''
import random
def randNumber(low,high,lenth):   #生成随机数
    for i in range(0,lenth):    #set有去重的功能，1000个随机数如果用set保存，最后很有可能就是0-100这100个数
        num = random.randint(low,high)#所以随机生成的数字字符我没有用set来保存
        if num >=20 and num <=50:  
            print(num,end=" ") 
def randStr(num):  #生成num个1-10个字符长度的字符串
    rds = set()     #set有自动去重的功能
    for i in range(num):
        lenth = random.randrange(1,10)
        strs = ''
        for j in range(lenth):
            strs += random.choice('abcdefghijklmnopqrstuvwxyz')#随机生成字符串
        rds.add(strs)
    for i in rds:    #取出包含at的字符串
        if 'at' in i:
            print(i,end=',')
    return rds        #返回集合
    

if __name__ == '__main__':
    randNumber(0,100,1000)      #遍历随机数
    print('\n-----------------------------------------------------')
    rds = randStr(1000)          #遍历随机字符串
    
