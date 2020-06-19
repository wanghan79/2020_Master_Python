import re,time

##装饰器查看每次计算运行时间
def timer(func):
    def inner(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        end_time = time.time()
        print("本次计算花费时间:", end_time - start_time)
        return res

    return inner

#连加
def  num_add(exy):
    '''多数连加'''
    res = re.split('\+',exy)
    out = float(res[0]) + float(res[1])
    if len(res) > 2:
        for i in range(2,len(res)):
            out = out + float(res[i])
    return out
#连减
def num_minus(exy):
    '''多数连减'''
    res = re.split('\-', exy)
    if res[0] == '':
        if len(res) == 2:
            return exy
        out = -float(res[1]) - float(res[2])
        if len(res) > 3:
            for i in range(3, len(res)):
                out = out - float(res[i])
    else:
        out = float(res[0]) - float(res[1])
        if len(res) > 2:
            for i in range(2, len(res)):
                out = out - float(res[i])
    return out
#连乘
def num_multiply(exy):
    '''多数连乘'''
    res = re.split('\*', exy)
    out = float(res[0]) * float(res[1])
    if len(res) > 2:
        for i in range(2, len(res)):
            out = out * float(res[i])
    return out
#连除
def num_divide(exy):
    '''多数连除'''
    res = re.split('\/', exy)
    for i in res:
        if i == '0':
            exit("除数不能为0.请检查表达式")
    out = float(res[0]) / float(res[1])
    if len(res) > 2:
        for i in range(2, len(res)):
            out = out / float(res[i])
    return out


def judge(u_str):
    '''含有*和/的表达式，进行去*和/'''
    if  '*' in u_str or '/' in u_str:
        red = re.split('[\+\-]',u_str)
        ok = 0
        for i in red:
            if re.findall(r'[\+\-\/\*]',i):
                if '*' in i and  '/' in i:
                    blue = re.split('\*',i)
                    zhuan = i
                    for k in blue:
                        if re.findall(r'[\+\-\/\*]',k):
                            mid = num_divide(k)
                            zhuan = zhuan.replace(k,str(mid))
                    ok = num_multiply(zhuan)
                elif '*' in i:
                    ok = num_multiply(i)
                elif '/' in i:
                    ok = num_divide(i)
                u_str = u_str.replace(i, str(ok))
    return u_str



def second(u_str):
    ##去掉表达式中的加减，得出结果
   if '+' in u_str or '-' in u_str:
         if '+' in u_str and '-' in u_str:
             black = re.split('\+',u_str)
             ok = 0
             for i in black:
                 if re.findall(r'[\+\-\/\*]',i):
                     ok = num_minus(i)
                     u_str = u_str.replace(i,str(ok))
             u_str = num_add(u_str)
             return u_str
         elif '+' in u_str:
            u_str = num_add(u_str)
            return u_str
         elif '-' in u_str:
            u_str = num_minus(u_str)
         return u_str

   return u_str

@timer
def core(expcetions):
    aa = re.search(r'\(([\-\+\*\/]?\d+\.?\d*)+\)', expcetions).group()
    bb = re.findall(r'\((.*)\)',aa)
    bb = ''.join(bb)
    cc = judge(bb)
    dd = second(cc)
    expcetions = expcetions.replace(aa,str(dd))
    return expcetions


def  fixbug(come):
    '''修复返回表达式中运算符重叠的问题'''
    if  re.search(r'([\-\*\/\+][\-\*\/\+])', come):

        s = re.search(r'([\-\*\/\+][\-\*\/\+])', come).group()
        if s == '*-' or s == '/-':
            res = re.search(r'[\+\-\(][^+\-\(]+[\*\/]\-',come).group()
            if  res[:1] == '+':
                new = res[:-1].replace('+','-')
                come = come.replace(res,new)
            elif res[:1] == '-':
                new = res[:-1].replace('-', '+')
                come = come.replace(res, new)
            elif  res[:1] == '(':
                new = res[:-1].replace('(', '(-')
                come = come.replace(res, new)
        if s == '+-':
            come = come.replace('+-', '-')
        if s == '--':
            come = come.replace('--','+')
    return come

def verify():
    while True:
        imm = input("输入您的表达式:>>").strip()
        res = re.findall(r'[\-\*\/\+]([\-\*\/\+])*',imm)
        monitor = [k for k in res if len(k) > 0]
        if monitor :
            print('error:两个或多个运算符相连，表达式有误!')
            continue
        if re.match(r'^[\+\-\*\/]',imm):
            print('error：{0}:运算符前缺失字符'.format(imm))
            continue
        if imm.endswith(('+','-','*','/')):
            print('error: {0}:运算符后缺失字符'.format(imm))
            continue
        break
    return imm



if __name__ == '__main__':

    while True:

            imm = verify()
            num = 0
            middle_num = imm
            while True:
                if  not re.search(r'\(([\-\+\*\/]?\d+\.?\d*)+\)',middle_num) == None:
                    middle_num = core(middle_num)
                    middle_num = fixbug(middle_num)
                    num+=1
                    print('第{0}次计算结果:'.format(num))
                    print(middle_num)
                else:
                    mutiply = judge(middle_num)
                    last = second(mutiply)
                    print('最终结果{0}'.format(last))
                    res_eval = eval(imm)
                    print('eval计算结果:{0}'.format(res_eval))
                    break










