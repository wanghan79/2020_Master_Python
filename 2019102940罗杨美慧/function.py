#!/usr/bin/python3
"""
  Author:  LuoYMH
  Purpose: function
  Created: 4/20/2020
"""
import random
import string

def dataSampling(datatype, datarange, num, strlen=6):
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
        if datatype is int:
            for index in range(num):
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
        print('datatypeError')
    finally:
        return result

def dataScreening(dataset, condition):
    '''
    :Description: function...
    :param dataset: input the data输入数据
    :param condition:筛选条件
    :return:筛选结果
    '''
    try:
        result = set()
        for i in dataset:
            if type(i) == int or type(i) == float:
                if i >= condition[0] and i <= condition[1]:
                    result.add(i)
            else:
                if condition[2] in i:
                    result.add(i)
    except:
        print('error')
    finally:
        return result

def apply():
    result = dataSampling(int, (1, 100), 100)
    #symmetric_difference_update()移除当前集合中在另外一个指定集合相同的元素，并将另外一个指定集合中不同的元素插入到当前集合中
    result.symmetric_difference_update(dataSampling(float, (1, 100), 100))
    #ascii_letters是生成所有字母，从a-z和A-Z,digits是生成所有数字0-9
    result.symmetric_difference_update(dataSampling(str, string.ascii_letters + string.digits, 1000, 50))
    result1 = dataScreening(result, (1, 10, "at"))
    print(result)
    print(result1)

if __name__ == '__main__':
    apply()