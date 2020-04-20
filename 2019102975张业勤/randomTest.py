import random

def randomNumber(low, high, lenth):
    result = set();
    for i in range(0, lenth):
        num = random.uniform(low, high);
        if((num>20)&(num<50)):
            result.add(num);
    print(result);

def randomStr(num):
    result = set()
    for i in range(num):
        lenth = random.randrange(1, 5);
        strs = '';
        for j in range(lenth):
            strs += random.choice('abcdefghijklmnopqrst')
        result.add(strs)
    for str in result:
        if 'at' in str:
            print(str);
    return result;

if __name__ == '__main__':
    randomNumber(0, 101, 1000);
    result = randomStr(1000);
