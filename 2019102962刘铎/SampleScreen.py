"""
  Author:  Amos.Liu
  Purpose: homework
  Created: 4/18/2020
  target:  1.解决随机数生成个数  2.字符串长度可变 3异常处理 4 数据筛选
"""
import random
import string

def dataSampling(datatype, dataRange, num, strlen): # 固定参数；可变参数arg*；默认参数；关键字参数**kwargs
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
            if dataRange[1] - dataRange[0] < num:
                return 'dataRange error'
            while(len(result) < num):
                it = iter(dataRange)
                item = random.randint(next(it), next(it))
                result.add(item)
                continue
        elif datatype is float:
            if dataRange[1] - dataRange[0] < num:
                return 'dataRange error'
            while(len(result) < num):
                it = iter(dataRange)
                result.add(random.uniform(next(it), next(it)))
                continue
        elif datatype is str:
            while(len(result) < num):
                if len(dataRange) < num:
                    return 'dataRange error'
                item = ''.join(random.SystemRandom().choice(dataRange) for _ in range(strlen))
                result.add(item)
                continue
        else:
            pass
    except TypeError as error:
        if type(dataRange) is not tuple:
            return 'raise error',error
        if datatype is int:
            while not isinstance(dataRange[0],int):
                return 'raise error',error
        elif datatype is float:
            while not isinstance(dataRange[0],float):
                return 'raise error',error
        elif datatype is str:
            if type(dataRange[0]) is not string:
                return 'raise error',error
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
                return 'raise error',error
            elif type(restrict[2]) is not str:
                return 'raise error',error
    finally:
        return result

if __name__ == "__main__":
    target_int = dataSampling(int,(1,100),10,0)
    target_str = dataSampling(str,string.ascii_letters, 10, 5)
    print('---builder---')
    print(target_int)
    print(target_str)
    print('---choice---')
    rec_tu = []
    for i in range(3):
        rec = input('input your choice：in order (num,num,str）')
        if i < 2:
            rec=int(rec)
        rec_tu.append(rec)
    res1 = dataScreening(target_int, rec_tu)
    res2 = dataScreening(target_str, rec_tu)
    print(res1)
    print(res2)