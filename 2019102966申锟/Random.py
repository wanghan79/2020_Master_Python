#!/usr/bin/python3

import random
import string

def dataSampling(datatype, datarange, num, strlen=10): # 固定参数；可变参数arg*；默认参数；关键字参数**kwargs
    try:
        result = set()
        for index in range(1, num):
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
                reallen = random.randint(1,strlen+1)
                item = ''.join(random.SystemRandom().choice(datarange) for _ in range(reallen))
                result.add(item)
                continue
            else:
                pass
    except:
            if datatype is (int or float):
                if type(datarange) is not tuple:
                    print('datarange数值参数错误')
                elif type(datarange[0] and datarange[1] ) is not int:
                    print('datarange中数据输入错误')
            elif datatype is str:
                if type(datarange) is not str:
                    print('datarange字符串参数错误')
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
    result = dataSampling(int, (1, 1000), 100) | dataSampling(str, string.ascii_letters, 5000)
    final_res = dataScreening(result, (10, 30, "at"))
    print(result)
    print(final_res)

apply()