##!/usr/bin/python3
"""
  Author:  zhangyeqin
  Purpose: Function Example
  Created: 4/20/2020
"""
import random
import string

def dataSampling(datatype, datarange, num, strlen=6): # 固定参数；可变参数arg*；默认参数；关键字参数**kwargs
    '''
        :Description: function...
        :param datatype: input the type of data
        :param datarange: input the range of data, a iterable data object
        :param num: the number of data
        :return: a set of sampling data
    '''
    try:
        result = set()
        if datatype is int:
            while (len(result) != num):# 按照要求加入while循环
                it = iter(datarange)
                item = random.randint(next(it), next(it))
                result.add(item)
        elif datatype is float:
            while (len(result) != num):
                it = iter(datarange)
                item = random.uniform(next(it), next(it))
                result.add(item)
        elif datatype is str:
            while (len(result) != num):
                len = random.randint(1, strlen + 1) #随机一个字符串长度len，根据len生成字符串
                item = ''.join(random.SystemRandom().choice(datarange) for _ in range(len))
                result.add(item)
        else:
            pass
    except:
        pass
    finally:
        return result

def dataScreening(dataset, condition):
    try:
        for i in dataset:
            if type(i) is int or type(i) is float:
                if i >= condition[0] and i <= condition[1]:
                    print(i)
            elif type(i)is str:
                if condition[2] in i:
                    print(i)
    except:
        pass
    finally:
        return 0

def apply():
    result = dataSampling(int,(1,100),50)|dataSampling(str,string.ascii_letters+string.digits, 30)
    print(result)
    dataScreening(result,(10,30,'a')) #数据筛选，筛选出10到30的数和带有a的字符串

apply()
