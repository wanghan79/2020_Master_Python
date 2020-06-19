##!/usr/bin/python3
"""
  Author:  hejingwen
  Purpose: Function Example
  Created: 4/16/2020
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
        for index in range(1, num):# while(result.account == num)
            if datatype is int:
                it = iter(datarange)
                item = random.randint(next(it), next(it))
                result.add(item)
                continue
            elif datatype is float:
                result.add(random.uniform(1, 10))
                continue
            elif datatype is str:
                item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
                result.add(item)
                continue
            else:
                pass
    except:
        if type(datatype) is int and type(datarange) is tuple:
            print()
        elif type(datatype) is str and type(datarange) is str:
            print()
        else:
            print("数据类型或者数据范围出错")


    finally:
        return result

def dataScreening(dataset, condition):
    try:
        for i in dataset:
            if type(i) is int:
                if i>condition[0] and i<condition[1]:
                    print(i)
            elif type(i) is str:
                if condition[2] in i:
                    print(i)
    except:
        if type(condition[1]) is int and type(condition[0]) is int and condition[2] is str:
            print()
        else:
            print("条件数据错误")
    finally:
        return 0

def apply():
    result = dataSampling(int,(0,50),50)|dataSampling(str,string.ascii_letters+string.digits, 50)
    print("输出20-30的数字或者含有字符a的字符串")
    dataScreening(result,(20,30,'a'))

apply()

