"""
    Author: B.Zou
    Purpose: Generating data of different format(e.g numbers, strings and so on)
    Created: 4/17/2020
"""
import random

str_len = 0  # for length of to generate string, it must set by user, default is 0
to_break = 10000  # if the range of you want get numbers less than the 'num', it will be infinite loop, it break it.

def dataSampling(dataType, dataRange, num):
    '''
    :param dataType: input the type of data
    :param dataRange: input the range of data, must be able to iterate
    :param num: the number of data
    :return result: a set of save what your want
    '''

    global str_len
    global to_break

    if type(num) != int:
        print('the parameter of \'num\' must be a integer number')
        return 0  # the '0' represent a code of some error occurrence

    try:
        len_dataRange = len(dataRange)  # for generate string
    except TypeError:
        print('the parameter of \'dataRange\' must be able to iterate')
        return 0  # the '0' represent a code of some error occurrence

    result = set()

    if dataType is int:
        try:
            i_from = dataRange[0]
            i_to = dataRange[1]
            while num > 0 and to_break > 0:
                to_break -= 1
                number = random.randint(i_from, i_to)
                if number in result:
                    continue
                else:
                    result.add(number)
                    num -= 1
            return result
        except ValueError:
            print('ValueError:empty range for randrange() %s %s. check your parameter' % (i_from, i_to))
            return 0   # the '0' represent a code of some error occurrence
    elif dataType is float:
        try:
            i_from = dataRange[0]
            i_to = dataRange[1]
            while num > 0 and to_break > 0:
                to_break -= 1
                number = round(random.uniform(i_from, i_to), 2)  # accurate to two decimal places
                if number in result:
                    continue
                else:
                    result.add(number)
                    num -= 1
            return result
        except ValueError:
            print('ValueError:empty range for uniform() %s %s, please input two number correctly.' % (i_from, i_to))
            return 0
    elif dataType is str:
        try:
            while num > 0 and to_break > 0:
                to_break -= 1
                str_long = random.randint(1, int(str_len)) # define the length of current generating string
                blank = ''
                for i in range(str_long):
                    ch = dataRange[random.randint(0, len_dataRange - 1)]
                    blank += ch
                if blank in result:
                    continue
                else:
                    result.add(blank)
                    num -= 1
            return result
        except ValueError:
            print('ValueError:  empty range for randrange()')


def create_table():  # create table [a-zA-Z]
    dataRange = []
    for i in range(65, 91):
        dataRange.append(chr(i))
    for i in range(97, 123):
        dataRange.append(chr(i))
    return dataRange


def show_result(result):  # show result
    '''
    :param result: a set of you want to print
    :return: null
    '''

    if type(result) is int:
        print('some error occur')
        return
    for item in result:
        print(str(item), end=' ')
    print()
    print()


while True:
    # input '#' represent you want to get integer number set
    # input '*' represent you want to get float number set
    # input 'some number' represent you want to get string set
    # input '$' represent you want to end.
    print('Enter:\n\'#\'\twill generate set of integer number\n'
          '\'*\'\twill generate set of float number\n'
          '\'number\'\twill generate set of string, number is range of string`s length\n'
          'Press \'$\' to end')

    str_len = input()

    if str_len == '$':
        print('Bye...')
        break

    elif str_len == '#':  # integer number
        print('Please input the range of you want to generate number and how much numbers you want to get.')
        try:
            i_from, i_to, num = map(int, input().split())
            dataRange = [i_from, i_to]
            result = dataSampling(int, dataRange, num)
            show_result(result)
        except ValueError:
            print('ValueError: could not convert string to float or int')
            exit(0)

    elif str_len == '*':  # float number
        print('Please input the range of you want to generate number, and how much numbers you want.')
        try:
            i_from, i_to, num = map(float, input().split())
            dataRange = [i_from, i_to]
            result = dataSampling(float, dataRange, int(num))
            show_result(result)
        except ValueError:
            print('ValueError: could not convert string to float or int')
            exit(0)

    elif str_len .isdecimal() and int(str_len) > 0:  # string
        dataRange = create_table()
        print('Please input how much you want to generate strings')
        try:
            num = int(input())
            result = dataSampling(str, dataRange, num)
            show_result(result)
        except ValueError:
            print('ValueError: could not convert string to int')
            exit(0)
    else:
        print('Can`t to recognize what your input, please re-enter\n')
