##!/usr/bin/python3
"""
  Author:  hanhao
  Purpose: Function Example
  Created: 4/15/2020
"""
import random
import string

def dataSampling(datatype, datarange, num, strlen=6): # 固定参数；可变参数arg*；默认参数；关键字参数**kwargs
    '''
    :Description: function...
    :param datatype: input the type of data数据类型
    :param datarange: input the range of data, a iterable data object范围
    :param num: the number of data 数据数量
    :param strlen: maximum range of character length 最大长度
    :return: a set of sampling data数据样本
    '''
    try:
        result = set()
        for index in range(1, num):# while(result.account == num)
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
                    prnt('datarange数值参数错误')
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
    result = dataSampling(int, (1,100), 10) | dataSampling(str, "aasbttttttaaaaoqmalzeropf", 10, )
    print('目标数据:', result)
    print('---------筛选出0,50之间的数字和含有at的字符串--------------')
    realresult = dataScreening(result, (0, 50, "at"))
    print('筛选后数据：', realresult)



apply()
