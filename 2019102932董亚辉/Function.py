##!/usr/bin/python3
"""
  Author:  YH.Dong
  Purpose: Function Example
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

    result = set()
    if datatype is int:
        for _ in range(num):
            item = random.randint(0, num)
            result.add(item)

    elif datatype is float:
        for _ in range(num):
            result.add(random.uniform(0, 100))
    elif datatype is str:
        try:
                if strlen == -1:
                    for _ in range(num):
                        strlen = random.randint(2, 18)
                        item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
                        result.add(item)
                else:
                    for _ in range(num):
                        item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
                        result.add(item)
        except:
             n = input('字符型输入的取值范围类型错误,是否处理[y / n]？')                   #处理取值范围错误的情况，用户可以选择是否处理
             if ( n == 'y'):
                datarange = input('请输入正确格式：')                                   #对取值范围进行重新输入
                return dataSampling(datatype, datarange, num, strlen=6)
             else:
                 pass

    else:
        pass

    return result

def dataScreening(dataset, condiction):
    """
    ：Description: Fetching a condition set in dataset
    :param dataset: datasets
    :param condiction: Judgement condition
    :return: reslut set
    """
    result = set()
    for data in dataset:
        if isinstance(data, int):
            if condiction(data):
                result.add(data)
        elif isinstance(data, float):
            if condiction(data):
                result.add(data)
        elif isinstance(data, str):
           if condiction(data):
               result.add(data)
    return result


def apply():
    result = dataSampling(int,(1, 10), 100, -1)  #产生整数集合
    func = lambda num : num>=20 and num<=50   # 取值范围表达式
    results = dataScreening(result, func)    #取出范围为（20， 50）的整数集合
    print(results)

    result = dataSampling(str, (string.ascii_letters+string.digits), 1000, -1)   #产生字符型集合
    func = lambda num: 'st' in num               #取值范围表达式
    results = dataScreening(result, func)        #取出带有‘ao’的字符
    print(results)

    result = dataSampling(float,(1,10), 100, -1)   #产生浮点型的集合
    func = lambda  num: num > 10.0 and num <= 20.0  #取值范围（10.0 , 50.0）表示式
    results = dataScreening(result, func)           #取出范围为（10.0， 50.0）的浮点数集合
    print(results)



if __name__ == '__main__':
    apply()
