
import random
import string

def dataSampling(datatype, datarange, num, strlen=6):

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
            else:
                pass
    except:
        if type(datarange) is not tuple:
            print('error')
        elif type(datarange[0] )is not int and (datarange[1]) is not int:
            print('error')
        elif type(datarange[0]) is not str:
                print('error')
    finally:
        return result

def dataScreening(dataset, condition):
    try:
        result = set()
        for i in dataset:
            if type(i) is  int or type(i) is float:
                if i>=condition[0]  and i<=condition[1] :
                    result.add(i)
            else:
                if condition[2] in i:
                    result.add(i)
    except:
        if type(condition[0]) is not int and type(condition[1]) is not int :
            print('error')
        elif type(condition[0]) is not float and type(condition[1]) is not float :
            print('error')
        elif type(condition[2]) is not str:
                print('error')

    finally:
        return result
def apply():
    resultint = dataSampling(int, (1,100), 10)
    print(resultint)
    resultstr= dataSampling(str,string.ascii_letters, 10, 5)
    print(resultstr)
    result1=dataScreening(resultstr,(0,10,"a"))
    print(result1)
apply()