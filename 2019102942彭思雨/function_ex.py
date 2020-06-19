"""
Author:peng siyu
Purpose:Output data and filter as required
Create: 4/19/2020
"""

'''
函数封装，函数参数如何确定，
解决随机数生成个数问题
解决可变参数问题
异常处理
数据筛选问题
'''
import random
import string
import sys
#数据采样  输入
#  固定参数;*arg可变参数; 默认参数(在样本输入中直接定义数据长度);关键字参数(**kwargs)
def dataSampling(datatype,datarange,num,strlen=6):#生成数据类型，数据范围，数据个数，数据长度
    '''
    :Description:function...
    :param datatype: input the type of data
    :param datarange: input the range of data,a iterable object(可迭代)
    :param num: the number of data
    :return: set of sampling data
    '''
    try:
    # 定义结果类型
        result = set() #集合类型，去重

    #解决结果集合中去重达不到要求的输出个数问题：加判断while(result.account == num)
        for index in range(1,num):# while(len(result) == num)
            if datatype is int:
                while(len(result) != num):
                    it = iter(datarange)
                    item = random.randint(next(it),next(it))#每次随机生成一个整数
                    result.add(item)#添加到结果集中
                continue
            elif datatype is float:
                while (len(result) != num):
                    result.add(random.uniform(1,10))
                continue
            elif datatype is str:
                while (len(result) != num):
                    item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
                    result.add(item)
                continue
            else:
                pass
    except:
        print('出现异常:')

    finally:
            return result

#数字筛选:筛选范围是可变参数
def dataScreening(dataset,condition):
    '''
    :param dataset: input the data
    :param condition:Screening condition
    :return:filtered data
    '''
    try:
        result = set()
        for index in dataset:
            if type(index) is int or type(index) is float:
                if condition[0] <= index and condition[1] >= index:
                    result.add(index)
            else:
                if condition[2] in index:
                    result.add(index)
    except:
        print('输出异常')
    finally:
        return result

def apply():
     str_result = dataSampling(str,"fsdafdsjksdyfustytdsrdtyrtttsaatataa",100,6)
     float_result = dataSampling(float, (1,100), 100, )
     int_result = dataSampling(int, (1,100), 50, )

     print('********************输出结果如下************************')
     print("1、字符串", str_result)
     print("2、浮点数", float_result)
     print("3、整数", int_result)

     print()
     print('************筛选出0,50之间的整数和浮点数以及含有at的字符串*************')
     result = str_result | float_result | int_result
     select_result = dataScreening(result, (0, 50, "at"))
     print('筛选后数据：', select_result)
#调用
apply()
