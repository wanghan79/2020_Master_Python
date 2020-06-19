
"""
  Author:  Weihua Hong
  Purpose: Perfect random number or string generation and screening
  Created: 4/19/2020
"""
import random
import string

def dataSampling(datatype, datarange, num, strlen=6):
    '''
    :Description: Generate random set
    :param datatype: input the type of data
    :param datarange: input the range of data, a iterable data object
    :param num: the number of data
    :return: a set of sampling data
    '''
    try:
        result = set()
        if datatype is int:
            while(len(result)<num):
                it = iter(datarange)
                item = random.randint(next(it), next(it))
                result.add(item)
                continue
        elif datatype is float:
            while (len(result) < num):
                it = iter(datarange)
                result.add(random.uniform(next(it), next(it)))
                continue
        elif datatype is str:
            while (len(result) < num):
                item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
                result.add(item)
                continue
    except TypeError:
        if(datatype is (int or float)):
            if(type(datarange)is not tuple):
                print('[Range Error] if datatype is int or float,datarange must be tuple')
            elif type(datarange[0] or datarange(1)) is not int:
                print('[Range Data Error] element in datarange must be int')
        elif datatype is str:
            if type(datarange) is not str:
                print("[Range Error] if datatype is str,datarange must be str")
        else:
            print('[Datatype Error] datatype must be int,float or str')
    finally:
        return result


def dataScreening(dataset, condition):
    '''
    :Description: Filter data
    :param dataset:DataSet to be filtered
    :param condition:Filter condition
    :return:Filtered set
    '''
    try:
        result = set()
        for data in dataset :
            if type(data) is int or type(data) is float:
                if data >= condition[0] and data <= condition[1]:
                    result.add(data)
                elif type(data) is str:
                    if condition[2] in data:
                        result.add(data)
    except:
        if type(condition) is not tuple:
            print('[Condition Error] condition must be tuple')
        else:
            if type(condition[0] or condition[1]) is not (int or float):
                print('[Condition Type Error] The first and second elements of the Condition must be int or float')
            elif type(condition[2]) is not str:
                print('[Condition Type Error] The third element of the Condition must be string')
            else:
                print('[Condition Error]')
    finally:
        return result

if __name__ == "__main__":

    result = dataSampling(int, (1, 1000), 20) | dataSampling(str, string.ascii_letters, 100, 9)
    print('before filter:')
    print(result)

    filerResult=dataScreening(result,(5,600,"th"))
    print('after filter:')
    print(filerResult)

