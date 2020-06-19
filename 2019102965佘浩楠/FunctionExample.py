##!/usr/bin/python3
"""
  Author:  Haonan She
  Purpose: Function Example
  Created: 4/20/2020
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
                print("Errro datatype , dataRange must be tuple")
            elif type(dataRange[0] or dataRange[1]) is not int:
                print("Errro dataRange,elements type must be int or float")
        elif datatype is str:
            if type(dataRange) is not str:
                print("Error dataRange,  dataRange must be str")
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
            print("Error condition ,it must be tuple")
        else:
            if type(condition[0] or condition[1]) is not (int or float):
                print("Error type condition[0] or condition[1],they bust be int or float")
            elif type(condition[2]) is not str:
                print("Error type condition[2],the element type must be str")
    finally:
        return result

if __name__ == "__main__":
    result = dataSampling(int, (1,100), 10) | dataSampling(str, "aacbghhhujooooooommmmnnnnjgggkop", 10, 5)
    print("RandomSet : ",result )

    result = dataScreening(result, (0,20,"a"))
    print("ScreeningSet: ",result)
