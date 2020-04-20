##!/usr/bin/python3
"""
  Author:  Liu Yang
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
    except:
        if datatype is (int or float):
            if type(datarange) is not tuple:
                print("Make sure datarange is a tutle!")
        elif datatype is str:
            if type(datarange) is not str:
                print("Make sure datarange is a str!")
    finally:
        return result


def dataScreening(dataset, condition):
    """
    :param dataset: input  data
    :param condition:input the condition of data
    :return:Filtered data
    """
    try:
        result = set()
        for data in dataset:
            if type(data) is int:
                if data>=condition[0] and data<=condition[1]:
                    result.add(data)
            elif type(data) is str:
                if condition[2] in data:
                    result.add(data)
    except:
        if type(condition[0] or condition[1]) is not (int or float):
            print("condition one or condition two error!")
        elif type(condition[2]) is not str:
            print("condition three error!")
    finally:
        return result


def apply():
    init_data = dataSampling(int, (0,100), 10)|dataSampling(str,string.ascii_letters,10)
    filter_data = dataScreening(init_data,(20,50,"at"))
    print("init_data:")
    print(init_data)
    print("filter_data:")
    print(filter_data)


apply()
