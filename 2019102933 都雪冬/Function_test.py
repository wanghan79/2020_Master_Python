import random
import string

"""
  Author:  duxuedong
  Purpose: Function Example
  Created: 4/19/2020
"""

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
        for index in range(1,num):
            if datatype is int:
                it = iter(datarange)
                item = random.randint(next(it),next(it))
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
                print('datarange error!')
            elif type(datatype[0] and datatype[1]) is not int:
                print('datatype error!')
        elif datatype is str:
            if type(datatype) is not str:
                print('datatype error!')
    finally:
        return result
def dataScreening(dataset,condition):
    '''
        :Description:filter data
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
            print('dataset error!')
        elif type(condition) is not tuple:
            print('condition error!')
        else:
            if type(condition[0] and condition[1]) is not (int or float):
                print("datatype in condition is error!")
            elif type(condition[2]) is not str:
                print("datatype in condition is error!")
    finally:
        return result
def apply():
    result = dataSampling(int,(0,50),50)|dataSampling(str,string.ascii_letters+string.digits, 50)
    print("digit between 10-20 or string involved 'at':")
    res=dataScreening(result,(10,20,'at'))
    print(res)

apply()