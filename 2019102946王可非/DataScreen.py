
"""
  Author:  Kefei.Wang
  Created: 4/19/2020
"""
import random
import string


def dataSampling(datatype, datarange, num, strlen=6):  # 固定参数；可变参数arg*；默认参数；关键字参数**kwargs
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
            for _ in range(num):
                item = random.randint(0, 100)
                result.add(item)
        elif datatype is float:
            for _ in range(num):
                result.add(random.uniform(0, 100))
        elif datatype is str:
            if strlen == -1:
                for _ in range(num):
                    strlen = random.randint(2, 18)
                    item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
                    result.add(item)
            else:
                for _ in range(num):
                    item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
                    result.add(item)
        else:
            pass
    except:
        print("输入有误")
    finally:
        return result


def dataScreening(dataset, condiction):
    try:
        result = set()
        for i in dataset:
            if type(i) is int:
                if condiction[0] < i < condiction[1]:
                    print(i)
            elif type(i) is str:
                if condiction[2] in i:
                    print(i)
    except:
        print('输入有误')
    finally:
        return 0


def apply():
    result = dataSampling(int, (10, 100), 10)
    print(result)
    result = dataSampling(float, (10, 100), 10)
    print(result)
    result = dataSampling(str, string.ascii_letters, 10)
    print(result)
    dataScreening(result, (20, 50, "at"))

apply()