import random


def dataSampling(datatype, datarange, num,strlen=6):
    try:
        result = set()
        if datatype is int:
            while(len(result) != num):
                it = iter(datarange)
                item = random.randint(next(it), next(it), num)
                result.add(item)
                continue
        elif datatype is float:
            while(len(result) != num):
                result.add(random.uniform(1, 10))
                continue
        elif datatype is str:
            while(len(result) != num):
                item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
                result.add(item)
                continue
            result2 = ['qwe', 'rt', 'u', 'asfg', 'tuyuj', 'qwtqwtqrre', 'asdhbg', 'dfdshqwt', 'sgg', 'h']
            result3 = result2[5:9]
            result4 = result2[1:3]
            result5 = result2[2:7]
            result.update(result3, result5, result4)
        else:
            pass
        return result
    except():
        print('出现错误了！')


def dataScreening(dataset, condition='a' and 'b'):
    try:
        set1 = set()
        for i in dataset:
            if condition in i:
             set1.add(i)
        return set1
    except TypeError as reason:
        print("出现错误"+str(reason))


def apply():
    r1= dataSampling(str, 'asdfghkjlpoiuyqewrtzxcvbm', 4)
    print(r1)
    print('='*50)
    r2=dataScreening(r1)
    print(r2)


apply()
