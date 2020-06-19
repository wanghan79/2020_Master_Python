#encoding=UTF-8
"""
Author:liancy
purpose:Function Example
created：4/20/2020
"""

import random
import string

def dataSampling(datatype, datarange, num, strlen=8): # 固定参数；可变参数；默认参数；关键字参数
    '''
    :Description: function...
    :param datatype: input the type of data 输入的数据类型
    :param dataRange: input the range of data, a iterable data object 数据范围，是可迭代对象（即可以用for循环的对象）
    :param num: the number of data  数据的数量
    :return: a set of sampling data 返回数据样本的集合
    '''
    try:
        result = set()
        if datatype is int:
            while(len(result) !=num):
                it = iter(datarange) #list，dict，str是Iterable但不是Iterator。要把list，dict，str等Iterable转换为Iterator可以使用iter()函数
                item = random.randint(next(it), next(it))#next(iterator[, default])。参考链接https://blog.csdn.net/li1615882553/article/details/79360172
                result.add(item)
                continue
        elif datatype is float:
            while(len(result) !=num):
                it = iter(datarange)
                result.add(random.uniform(next(it), next(it)))
                continue
        elif datatype is str:
            while(len(result) !=num):
                item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))# -就是一个循环标志，可以用 i,j代表，起到循环次数的作用。
                result.add(item)
                continue
        else:
            pass
    except TypeError as e:
        if datatype is (int or float):
            if type(datarange) is not tuple:
                return("数据类型错误："+str(e))
            elif type(datarange[0] or datarange[1]) is not int:
                return ("数据类型错误：" + str(e))
        elif datatype is str:
            if type(datarange) is not str:
                return ("数据类型错误：" + str(e))
    finally:
        return result
def dataScreening(dataset, condition):
    """
    :param dataset: String to process 想要筛选的数据集
    :param condition:Screening conditions 输入筛选的条件
    :return:result of process 返回筛选后的数据集
    """
    try:
        result = set()
        for i  in dataset:
            if type(i) is int or type(i) is float:
                if condition[0] <= i and condition[1] >= i:
                    result.add(i)
            else:
                if condition[2] in i:
                    result.add(i)
    except :
        print("出错了")
    finally:
        return result
def apply():

    screenbefore=dataSampling(int,(1,100),100)|dataSampling(str,string.ascii_letters + string.digits,100)
    print("筛选前随机样本集合")
    print(screenbefore)
    screenafter=dataScreening(screenbefore,(20,50,'a'))
    print("筛选后随机样本集合")
    print(screenafter)


if __name__ == "__main__":

    apply()