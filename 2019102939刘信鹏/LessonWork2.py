##!/usr/bin/python3
"""
  Author:  Xp.Liu
  Purpose: Lesson Work
  Created: 4/14/2020
"""
import random
import string
import re

def dataSampling(datatype, datarange, num, strlen=(1, 5)):
    '''
    :Description: function...
    :param datatype: input the type of data
    :param datarange: input the range of data, a iterable data object
    :param num: the number of data
    :param strlen: input the range of random interval of string length, a iterable data object
    :return: a set of sampling data
    '''
    try:
        result = set()
        if datatype is int:
            it = iter(datarange)
            start = next(it)
            end = next(it)
            if (end - start <= 0 or end - start < num):
                raise Exception("输入区间错误")
            while (len(result) != num):
                item = random.randint(start, end)
                result.add(item)
        elif datatype is float:
            it = iter(datarange)
            start = next(it)
            end = next(it)
            if (end - start <= 0):
                raise Exception("输入区间错误")
            while (len(result) != num):
                item = random.uniform(start, end)
                result.add(item)
        elif datatype is str:
            it = iter(strlen)
            start = next(it)
            end = next(it)
            if (end - start <= 0 or start <= 0):
                raise Exception("输入区间错误")
            while (len(result) != num):
                str_len = random.randint(start, end)
                item = ''.join(random.SystemRandom().choice(datarange) for _ in range(str_len))
                result.add(item)
        else:
            pass
    except Exception as e:
        print('出现异常:', e)
    finally:
        pass

    return result

def dataScreening(dataset, condition):
    '''
    :Description: function...
    :param dataset: input the set of data
    :param condition: input the condition of data
    '''
    try:
        conditions = condition.split('and')
        orders = " 1==2 "
        for order in conditions:
            if order.find('number') != -1:
                number_section = re.search(r'(?<=\()\S+(?=\))', order, re.I)  # 对大小写不敏感
                if number_section:
                    section = number_section.group().split(',')
                    start = int(section[0])
                    end = int(section[1])
                    if (end - start < 0):
                        raise Exception("输入区间错误")
                    orders += "or ((type(item) is float or type(item) is int) and (start <= item <= end))"

            elif order.find('string') != -1:
                str_section = re.search(r'(?<=\')\S+(?=\')', order)  # 对大小写敏感
                if str_section:
                    sub_str = str_section.group()
                orders += " or ((type(item) is str) and (sub_str in item))"
            else:
                pass

        for item in dataset:
            if (eval(orders)):
                print(item)
    except Exception as e:
        print('出现异常:', e)
    finally:
        pass

def apply():
    set_int = dataSampling(int, (0, 100), 100) # 随机生成100个0-100之间的整数
    set_float = dataSampling(float, (0, 100), 1000) # 随机生成1000个0-100之间的浮点数
    set_str = dataSampling(str, string.ascii_letters+string.digits, 1000, (1, 10)) # 随机生成1000个长度为1-10之间的字符串

    result = set()
    result.symmetric_difference_update(set_int)
    result.symmetric_difference_update(set_float)
    result.symmetric_difference_update(set_str)

    condition = input("请输入指定数据类型的数据筛选指令（例如：Takes the number between (20,50) and the string containing the substring 'at' ）：\n")
    dataScreening(result, condition) # 数据筛选

if __name__ == '__main__':
    apply()
