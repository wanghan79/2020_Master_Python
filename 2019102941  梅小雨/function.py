import random
import string
"""
  Author:  Xiaoyu Mei
  Purpose: Screening random dataset
  Created: 4/20/2020
"""

def dataSampling(datatype, datarange, num, strlen=6): # 固定参数；可变参数arg*；默认参数；关键字参数**kwargs
    '''
    :Description: function...
    :param datatype: input the type of data
    :param datarange: input the range of data, a iterable data object
    :param num: the number of data
    :return: a set of sampling data
    '''
    try:
        result=set()
        if datatype is int:
            while (len(result) != num):
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
    except:
        print('You are not right')
    finally:
        return result

def dataScreening(dataset, condition):#数字筛选
    try:
        result=set()
        for i in dataset:
            if type(i) is int or type(i) is float:
                if i>= condition[0] and i<= condition[1]:
                    result.add(i)
            else:
                if condition[2] in i:
                    result.add(i)
    except:
        pass
    finally:
        return result

if __name__ == "__main__":
    result = dataSampling(int, (1, 100), 10)|dataSampling(str,string.ascii_letters+string.digits, 30)
    print(result)
    result = dataScreening(result, (0, 30, "a"))
    print(result)




