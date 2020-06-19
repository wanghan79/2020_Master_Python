##!/usr/bin/python3
"""
  Author:  WangZhiwen
  Purpose: Function Example
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
        for index in range(1, num):  # while(result.account == num)
            if datatype is int:
                it = iter(datarange)
                item = random.randint(next(it), next(it))
                result.add(item)
                continue
            elif datatype is float:
                it = iter(datarange)
                result.add(random.uniform(next(it), next(it)))
                continue
            elif datatype is str:
                item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
                result.add(item)
                continue
            else:
                pass
    except:
        if datatype is (int or float):
            if type(datarange) is not tuple:
                prnt('datarange error')
            elif type(datarange[0] and datarange[1]) is not int:
                print('datarange error')
        elif datatype is str:
            if type(datarange) is not str:
                print('datarange error')
        pass
    finally:
        return result




def dataScreening(dataset, condition):
    '''
    :param dataset: input the data
    :param condition:Screening condition
    :return:filtered data
    '''
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
            print('dataset error')
        elif type(condition) is not tuple:
            print('condition error')
        else:
            if type(condition[0] and condition[1]) is not (int or float):
                print("condition error")
            elif type(condition[2]) is not str:
                print("condition error")
    finally:
        return result


def apply():

    result = dataSampling(int, (1, 50), 10) | dataSampling(str, "aaaaaaabcdefghijklmnopqrstttttttuvwxyz", 10, )
    print(result)
    finresult = dataScreening(result, (0, 30, "at"))
    print(finresult)
apply()
