##!/usr/bin/python3
"""
  Author:  Fuyz
  Purpose: Function Example
  Created: 4/19/2020
"""
import random
import string


def dataSampling(datatype, datarange, num):  # 固定参数；可变参数arg*；默认参数；关键字参数**kwargs
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
                item = ''.join(random.SystemRandom().choice(datarange) for _ in range(random.randint(2, 10)))
                result.add(item)
                continue
        return result
    except:
        print("input type error")


def dataScreening(dataset, condition):
    '''
    :Description:Filter data
    :param dataset:DataSet needs to filter
    :param condition:Filter condition
    :return:Filtered set
    '''
    try:
        final_result = set()
        for data in dataset:
            if type(data) is int or type(data) is float:
                if condition[0] <= data <= condition[1]:
                    final_result.add(data)
            elif type(data) is str:
                if condition[2] in data:
                    final_result.add(data)
        return final_result
    except:
        print("input type error")


def apply():
    result = dataSampling(int, (1, 1000), 100) | dataSampling(str, string.ascii_letters, 5000)
    final_res = dataScreening(result, (100, 300, "fu"))
    print(result)
    print(final_res)


apply()
