"""
  Author:  JianjunFan
  Purpose: Function Example
  Created: 4/14/2020
"""
import random
import string

def dataSampling(datatype, dataRange, num, strlen=6): # 固定参数；可变参数arg*；默认参数；关键字参数**kwargs
    '''
    :Description: function...
    :param datatype: input the type of data
    :param dataRange: input the range of data, a iterable data object
    :param num: the number of data
    :return: a set of sampling data
    '''
    try:
        result = set()
        if datatype is int:
            while(len(result) < num):
                it = iter(dataRange)
                item = random.randint(next(it), next(it))
                result.add(item)
                continue
        elif datatype is float:
            while(len(result) < num):
                it = iter(dataRange)
                result.add(random.uniform(next(it), next(it)))
                continue
        elif datatype is str:
            while(len(result) < num):
                item = ''.join(random.SystemRandom().choice(dataRange) for _ in range(strlen))
                result.add(item)
                continue
        else:
            pass
    except TypeError:
        if datatype is (int or float):
            if type(dataRange) is not tuple:
                print("[Errno] when datatype is int or float, dataRange must is tuple")
            elif type(dataRange[0] or dataRange[1]) is not int:
                print("[Errno] dataRange elements type must is int or float")
        elif datatype is str:
            if type(dataRange) is not str:
                print("[Errno] when datatype is str, dataRange must is str")
    finally:
        return result

def dataScreening(dataset, condition):
    """

    :param dataset: String to process
    :param condition:Screening conditions
    :return:result of process
    """
    try:
        result = set()
        for data in dataset:
            if type(data) is float or type(data) is int:
                if data >= condition[0] and data <= condition[1]:
                    result.add(data)
            else:
                if condition[2] in data:
                    result.add(data)
    except:
        if type(condition) is not tuple:
            print("[Errno] condition must is tuple")
        else:
            if type(condition[0] or condition[1]) is not (int or float):
                print("[Errno] condition's the first two elements type must is int or float")
            elif type(condition[2]) is not str:
                print("[Errno] condition's the third element type must is str")
    finally:
        return result

if __name__ == "__main__":
    result = dataSampling(int, (1,100), 10) | dataSampling(str, "aasbhjcuyewbasdlapoqmalzeropf", 10, 5)
    print("Before Set : " )
    print(result)

    re = dataScreening(result, (0,50,"a"))
    print("After Set : ")
    print(re)

