
import random
import string
def floatSet(finalFloatSet):
    fSet=set()
    for i in range(0,1000):
        fSet.add(random.uniform(0,100))
    #print(fSet.__len__())
    for num in fSet:
        if num>=20 and num<=50:
            finalFloatSet.add(num)
    return


def ranStr(num):
    salt = ''.join(random.sample(string.ascii_letters, num))
    return salt


def stringSet(finalStringSet):
    sSet=set()
    for i in range(0,1000):
        sSet.add(ranStr(6))
    for str in sSet:
        if 'at' in str:
            finalStringSet.add(str)
    #print(sSet.__len__())

if __name__ == '__main__':
    finalFloatSet=set()
    floatSet(finalFloatSet)
    #print(finalFloatSet.__len__())
    for num in finalFloatSet:
        print(num)
    finalStringSet=set()
    stringSet(finalStringSet)
    if(finalStringSet.__len__()!=0):
        for str in finalStringSet:
            print(str)
    else:
        print("没有包含at的字符串")
