##!/usr/bin/python3
"""
  Author:  P.yang
  Purpose: Function Example
  Created: 4/19/2020
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
      # while(result.account == num)
      if datatype is int:
          while (result.account != num):
            it = iter(datarange)
            item = random.randint(next(it), next(it), num)
            result.add(item)

      elif datatype is float:
          while (result.account != num):
            result.add(random.uniform(1, 10))

      elif datatype is str:
          while (result.account != num):
            item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
            result.add(item)

      else:
            pass
    except:
        print("ERROR")
    finally:
        return result

def dataScreening(dataset, condition):
    try:
        for i in dataset:
            if type(i) is int:
                if i>condation[0] and i<condition[1]:
                    print(i)
            elif type(i) is str:
                if condition[2] in i:
                    print(i)
    except:
        print(EPPOR)
    finally:
        return 0


def apply():
    result = dataSampling(str, string.ascii_letters+string.digits, 20)
    print(result)
    print(dataScreening(result,'b'))
    result =dataSampling(int, (0, 50), 50)
    print(result)
    print(dataScreening(result, 10,20))

apply()
