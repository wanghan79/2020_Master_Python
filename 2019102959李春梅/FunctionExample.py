#!/usr/bin/python3
"""
  Author:  Li Chunmei
  Purpose: Function Example
  Created: 4/19/2020
"""
import random
import string

def dataSampling(datatype, datarange, num, strlen=10): # 固定参数；可变参数arg*；默认参数；关键字参数**kwargs
    '''
    :Description: function...
    :param datatype: input the type of data数据类型
    :param datarange: input the range of data, a iterable data object数据范围
    :param num: the number of data 数据数量
    :param strlen: maximum range of character length 字符串最大长度
    :return: a set of sampling data数据样本
    '''
    try:#捕捉异常可以使用try/except语句,try/except语句用来检测try语句块中的错误，从而让except语句捕获异常信息并处理
        result = set()
        for index in range(1, num):# while(result.account == num)
            if datatype is int:
                it = iter(datarange)
                item = random.randint(next(it), next(it))#random.randint()用于生成一个指定范围内的整数
                result.add(item)
                continue
            elif datatype is float:
                it = iter(dataRange)
                result.add(random.uniform(next(it), next(it)))#random.uniform用于生成一个指定范围内的随机符点数
                continue
            elif datatype is str:
                reallen = random.randint(1,strlen+1)
                item = ''.join(random.SystemRandom().choice(datarange) for _ in range(reallen))#random.choice从序列中获取一个随机元素
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
    '''
    :param dataset: input the data输入数据
    :param condition:Screening condition筛选条件
    :return:filtered data筛选后的数据
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
