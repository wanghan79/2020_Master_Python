##!/usr/bin/python3
"""
  Author:  孙天磊2019102967
  Purpose: Function Example
  Created: 4/21/2020
"""
import random
import string

def dataSampling(datatype, datarange, num, strlen=6): # 固定参数；可变参数arg*；默认参数；关键字参数**kwargs
    '''
    :Description: function...
    :param datatype: input the type of data
    :param datarange: input the range of data, a iterable data object
    :param num: the number of data
    :param strlen: maximum range of character length
    :return: a set of sampling data
    '''
    try:
        result = set()
        for index in range(1, num):  # while(result.account == num)
            if datatype is int:
                it = iter(datarange)
                item = random.randint(next(it), next(it))
                result.add(item)
                continue
            elif datatype is float:
                it = iter(dataRange)
                result.add(random.uniform(next(it), next(it)))
                continue
            elif datatype is str:
                create_len = random.randint(1, strlen + 1)
                item = ''.join(random.SystemRandom().choice(datarange) for _ in range(create_len))
                result.add(item)
                continue
            else:
                pass
    except:
        if datatype is (int or float):
            if type(datarange) is not tuple:
                print('datarange数值类型参数错误')
            elif type(datarange[0] and datarange[1]) is not int:
                print('datarange中数据输入错误')
        elif datatype is str:
            if type(datarange) is not str:
                print('datarange字符串类型参数错误')
    finally:
        return result


def dataScreening(dataset, condition):
    try:
        result = set()
        for i in dataset:
            if type(i) is (int or float):
                if condition[0] <= i and condition[1] >= i:
                    result.add(i)
            else:
                if condition[2] in i:
                    result.add(i)
    except:
        if type(dataset) is not tuple:
            print('dataset数据类型错误')
        elif type(condition) is not tuple:
            print('condition数据类型错误')
        else:
            if type(condition[0] and condition[1]) is not (int or float):
                print("condition中的数值数据的类型错误")
            elif type(condition[2]) is not str:
                print("condition中的字符串数据的类型错误")
    finally:
        return result

def apply():
    result = dataSampling(int, (0, 100), 100) | dataSampling(str, "abdrtaaatttgggdd", 100)
    select = dataScreening(result, (50, 60, "at"))
    print(result)
    print("其中在30~60之间的数字或者含有at的字符串有：")
    print(select)

apply()