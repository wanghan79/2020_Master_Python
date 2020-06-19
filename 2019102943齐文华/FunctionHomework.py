#!/user/bin/env python
# -*- coding:utf-8 -*-
"""
  Author:  Wenhua.Qi
  Purpose: Function Homework
  Created: 4/19/2020
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
            while (len(result) < num):
                it = iter(datarange)
                item = random.randint(next(it), next(it))
                result.add(item)
                continue
        elif datatype is float:
            while (len(result) < num):
                it = iter(datarange)
                result.add(random.uniform(next(it), next(it)))
                continue
        elif datatype is str:
            while (len(result) < num):
                item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
                result.add(item)
                continue
        else:
            pass
    except TypeError as error:
        if type(datarange) is not tuple:
            return 'TypeError', error
        if datatype is int:
            while not isinstance(datarange[0], int):
                return 'TypeError', error
        elif datatype is float:
            while not isinstance(datarange[0], float):
                return 'TypeError', error
        elif datatype is str:
            if type(datarange[0]) is not str:
                return 'TypeError', error
    finally:
        return result
def dataScreening(dataset, condition):
    try:
        result = set()
        for data in dataset:
            if type(data) is float or type(data) is int:
                if data >= condition[0] and data <= condition[1]:
                    result.add(data)
            else:
                if condition[2] in data:
                    result.add(data)
    except:
        if type(condition) is not tuple:
            print("[Error] condition must is tuple")
        else:
            if type(condition[0] or condition[1]) is not (int or float):
                print("[Error] condition's the first two elements type must is int or float")
            elif type(condition[2]) is not str:
                print("[Error] condition's the third element type must is str")
    finally:
        return result

if __name__ == "__main__":
    result = dataSampling(int, (1, 100), 10) | dataSampling(str, "abcdeffffghlmnmmopqrst", 10, 5)
    print("筛选前随机样本集合")
    print(result)
    afterRes = dataScreening(result, (0, 50, "a"))
    print("筛选后随机样本集合")
    print(afterRes)
