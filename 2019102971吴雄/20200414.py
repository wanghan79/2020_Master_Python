##!/usr/bin/python3
"""
  Author:  wuxiong
  Purpose: Function Example
  Created: 4/14/2020 17:34
  goal:
  1.for循环解决随机数生成个数  2.字符串长度可变 3异常处理 4 数据筛选 
"""
import random
import string

def dataSampling(datatype, datarange, num, strlen=8,**kwargs): # 固定参数；可变参数arg*；默认参数；关键字参数**kwargs

    #参数顺序datatype, datarange, num, strlen=8,func=lambda x:x>-1
    '''
    :Description: function...
    :param datatype: 输入的数据类型
    :param datarange: 输入一个范围值，是一个可迭代类型
    :param num: 生成字符或者数字数量
    :param strlen:字符串长度最大范围
    :return: 返回取样数据
    '''
    func = lambda x : 1==1   #设置一个默认的lambda表达式
    for key in kwargs:
        if(key == 'func'):
            func = kwargs['func']     #取出lambda函数
    try:
#         datatype = arg
        iter(datarange)
        if datatype is int:{}
        elif datatype is float:{}
        elif datatype is str:{}
        else:
            return("datatype参数错误")
        pass
    except Exception as e:
         return("参数输入错误:"+str(e))
    finally:
        pass

    result = set()
    for index in range(0, num):# while(result.account == num)
        if datatype is int:
            it = iter(datarange)
            item = random.randint(next(it), next(it))
            if func(item):  #用lambda表达式筛选
                result.add(item)
            continue
        elif datatype is float:
            it = iter(datarange)
            item = random.uniform(next(it), next(it))
            if func(item):  #用lambda表达式筛选
                result.add(item)
            continue
        elif datatype is str:
            realstrlen = random.randrange(1,strlen+1) #随机字符串长度
            '''
            官方文档
            random.randint(a, b)
            Return a random integer N such that a <= N <= b. Alias for randrange(a, b+1).
            '''
            item = ''.join(random.sample('abcdefghijklmnopqrstuvwxyz',realstrlen))
            if func(item): #用lambda表达式筛选
                result.add(item)
            continue
        else:
            pass

    return result

def dataScreening():
    result = dataSampling(str, (1,100), 10)#测试随机长度字符串
    print('测试字符串')
    print(result)
    result = dataSampling(int, 1, 100)  #测试第二个参数为非迭代类型
    print('测试第二个参数为非迭代类型')
    print(result)
    result = dataSampling(1, (1,100), 10) #测试第一个参数非类型参数,注意数字1和int不是同一个类型 1是int类，int是type类
    print("#测试第一个参数非类型参数,注意数字1和int不是同一个类型 1是int类，int是type类")
    print(result)
    result = dataSampling(int, (1,100), 100,**{'func':lambda x : x>=5 and x <= 10}) #加入筛选条件，用lambada表达式作为筛选条件
    print("测试入筛选条件，用lambada表达式作为筛选条件，筛选5到10之间的数字")
    print(result)
    result = dataSampling(str, (1,100), 1000,10,**{'func':lambda x : 'at' in x}) #加入筛选条件，用lambada表达式作为筛选条件
    print("测试入筛选条件，用lambada表达式作为筛选条件，筛选包包含at的字符串")
    print(result)
    pass

def apply():
    dataScreening()

apply()



"""
运行结果：
测试字符串
{'qi', 'tlfbsw', 'tmsl', 'epsjic', 'kfhibsn', 'rzfvwkb', 'qk', 'kquyzhx', 'wgvach', 'zrut'}
测试第二个参数为非迭代类型
参数输入错误:'int' object is not iterable
#测试第一个参数非类型参数,注意数字1和int不是同一个类型 1是int类，int是type类
datatype参数错误
测试入筛选条件，用lambada表达式作为筛选条件，筛选5到10之间的数字
{5, 6, 7, 9, 10}
测试入筛选条件，用lambada表达式作为筛选条件，筛选包包含at的字符串
{'atmq', 'fxat', 'atslyo', 'at', 'irwatmodq', 'hywugatnde'}

"""
