"""
    Author:XY Wang
    Created:4/20/20
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
            while (len(result) != num):
                it = iter(datarange)
                item = random.randint(next(it), next(it))
                result.add(item)
                continue
        elif datatype is float:
            while (len(result) != num):
                result.add(random.uniform(1, 10))
                continue
        elif datatype is str:
            while (len(result) != num):
                item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
                result.add(item)
                continue
        else:
            pass
    except:
        print('error')
    finally:
        pass
    return result


def dataScreening(dataset, condition):
    '''
    :param dataset:input the set of data
    :param condition:input the condition of data
    '''
    try:
        result = set()
        for i in dataset:
            if type(i) is int:
                if condition[0] < i < condition[1]:
                    print(i)
            elif type(i) is str:
                if condition[2] in i:
                    print(i)
    except:
        print('error')
    finally:
        pass


def apply():
    result = dataSampling(int, (0, 50), 5)
    print(result)
    print(dataScreening(result, (10, 30)))  # 输出在10-30之间的数字
    result = dataSampling(str, string.ascii_letters + string.digits, 10)
    print(result)
    print(dataScreening(result, '59a'))  # 输出在0-9之间以及带有字母a的字符串


apply()
