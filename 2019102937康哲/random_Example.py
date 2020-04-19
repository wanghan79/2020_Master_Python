"""
  Author:  KangZhe
  Purpose: Random Example
  Created: 4/19/2020
"""
import random
import string


def dataSampling(datatype, datarange, num, strlen=6):
    '''

    :param datatype: input the type of data
    :param datarange:input tehe range of data
    :param num:the number of data
    :param strlen:maximum length
    :return:a set
    '''
    try:
        result = set()
        for index in range(1, num):  # while(result.account == num)
            if datatype is int:
                    it = iter(datarange)
                    item = random.randint(next(it), next(it))
                    result.add(item)
                    continue
            elif datatype is float:
                result.add(random.uniform(1, 10))
                continue
            elif datatype is str:
                item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
                result.add(item)
                continue
        return result
    except:
        print("input error!")
def dataScreening(dataset, condition):
    '''

    :param dataset:  input of data
    :param condition:condition of screening
    :return:final output
    '''
    try:
        result = set()
        for data in dataset:
            if type(data) is int:
                if condition[0] <= data and condition[1] >= data:
                    result.add(data)
            elif type(data) is str:
                if condition[0] in data:
                    result.add(data)
        return result
    except:
        print("type error!")

def apply():
    """
    result = dataSampling(int, (1, 10), 5)
    final_res = dataScreening(result, (5,7))
    """
    result = dataSampling(str, "hhhhhhahhhhhahhahahahahhahahha", 5)
    final_res = dataScreening(result, "ha")
    print(final_res)
apply()