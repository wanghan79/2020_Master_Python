"""
  Author:  HM.yang
  Purpose: homework
  Created: 4/17/2020
  target:  1.解决随机数生成个数问题  2.希望字符串长度可变 3.使用异常处理 4.进行数据筛选
"""
import random
import string


def dataSampling(datatype, dataRange, num, strlen):  # 固定参数；可变参数arg*；默认参数；关键字参数**kwargs
    '''
    :Description: function...
    :param datatype: input the type of data
    :param dataRange: input the range of data, a iterable data object
    :param num: the number of data
    :strlen: the length of string
    :return: a set of sampling data
    '''
    try:
        result = set()
        if datatype is int:
            while (len(result) < num):
                it = iter(dataRange)
                item = random.randint(next(it), next(it))
                result.add(item)
                continue
        elif datatype is float:
            while len(result) < num:
                it = iter(dataRange)
                result.add(random.uniform(next(it), next(it)))
                continue
        elif datatype is str:
            while (len(result) < num):
                item = ''.join(random.SystemRandom().choice(dataRange) for _ in range(strlen))
                result.add(item)
                continue
        else:
            pass
    except TypeError as error:
        if type(dataRange) is not tuple:
            return error
        if datatype is int:
            while not isinstance(dataRange[0], int):
                return error
        elif datatype is float:
            while not isinstance(dataRange[0], float):
                return error
        elif datatype is str:
            if type(dataRange[0]) is not string:
                return error
    finally:
        return result


def dataScreening(datasample, restrict):
    """
        :param datasample: String to process
        :param restrict:Screening conditions
        :return:result of process
    """
    try:
        result = set()
        for data in datasample:
            if type(data) is float or type(data) is int:
                if data >= restrict[0] and data <= restrict[1]:
                    result.add(data)
            else:
                if restrict[2] in data:
                    result.add(data)
    except TypeError as error:
        if type(restrict) is not tuple:
            return error
        else:
            if type(restrict[0] or restrict[1]) is not (int or float):
                return error
            elif type(restrict[2]) is not str:
                return error
    finally:
        return result


if __name__ == "__main__":
    target_int = dataSampling(int, (1, 100), 10, 0)
    target_str = dataSampling(str, string.ascii_letters, 10, 5)
    res1 = dataScreening(target_int, (0, 70, "at"))
    res2 = dataScreening(target_str, (0, 70, "at"))
    print('---builder success---')
    print(target_int)
    print(target_str)
    print('---choice success---')
    print(res1)
    print(res2)
