##!/usr/bin/python3
"""
  Author:  liangmengyao
  Purpose: Function Example
  Created: 4/18/2020
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
            while(len(result)!=num):
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
        print("error")
    finally:
        return result

def dataScreening(dataset, condition):
    try:
        result=set()
        for i in dataset:
            if type(i)==int or type(i)==float:
                if i>=condition[0] and i<=condition[1]:
                    result.add(i)
            elif type(i)==str:
                if condition[2] in i:
                    result.add(i)
    except:
        print("error")
    finally:
        return result
def apply():
    result = dataSampling(int, (1,100), 100)
    result.symmetric_difference_update(dataSampling(float,(1,100),100))
    length=random.randint(1,10)
    result.symmetric_difference_update(dataSampling(str,string.ascii_letters+string.digits,1000,length))
    print(result)
    print()
    result1=dataScreening(result,(1,10,"at"))
    print(result1)
apply()
