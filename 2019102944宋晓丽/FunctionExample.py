##!/usr/bin/python3
"""
  Author:  Songxiaoli
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
        if datatype is int:
            while (len(result) != num):
                it = iter(datarange)
                item = random.randint(next(it), next(it))
                result.add(item)
        elif datatype is float:
            while (len(result) != num):
                result.add(random.uniform(1, 10))
        elif datatype is str:
            while (len(result) != num):
                item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
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
                if i>=condition[0] and i<=condition[1]:
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
    dataScreening(result,(10,30,'s'))


apply()
