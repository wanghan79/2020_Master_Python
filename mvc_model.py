'''
by: zoubin
模拟MVC模式，其中模型和控制器就是使用类名，视图层使用的是main，show方法
主要模拟一个用户登录注册程序的MVC实现．
用户在main函数中根据提示输入登录、注册或离开选项.
登录(L)：用户提供登录信息：　用户名，密码．登录成功后，程序跳转show方法，输入'L'离开．
注册(R)：用户提供注册信息：用户名，性别，年龄，密码，注册成功后使用应户名＋密码登录
离开(任意字符)：用户输入除'L'，'R'外的任意字符／字符串退出程序

users: 模拟数据库
User: 封装对象信息
number: 数据库表主键
show方法: 模拟登录成功后的视图
main方法:　模拟登录注册界面视图
Model类:　模型类
Controller类:　控制器类

已知BUG：　没做类型输入正确性验证
'''

from collections import namedtuple

users = dict()
User = namedtuple('User', ['name', 'sex', 'age', 'password'])
number = 0


def show(user):
    '''
    视图层，只负责展示信息
    :param user: 登录成功的用户
    :return: 无
    '''
    print('Welcome you {}, this is home page'.format(user.name))
    while True:
        leave = input('Enter [L]eave to leave there')
        if leave == 'L':
            break


class Model:
    '''
    模型：　用于和数据库交互
    '''
    def __init__(self):
        global users
        global number
        number = number + 1

    def register(self, name, sex, age, password):
        '''
        数据库插入操作
        :param name: 用户名
        :param sex: 用户性别
        :param age: 用户年龄
        :param password: 密码
        :return: True: 注册成功 False: 注册失败，已存在此人
        '''
        for key in users:
            if name is users.get(key).name:
                return False
        self.user = User(name=name, sex=sex, age=age, password=password)
        users[number] = self.user
        return True

    def check_user(self, name, password):
        '''
        数据库查询操作
        :param name: 登录用户名
        :param password: 密码
        :return: {flag, User} : {True, user} / {False , None} 登录成功，重定向至show方法．　登录失败，重定向至main方法
        '''
        for key in users:
            if users[key].password == password and users[key].name == name:
                return {True, users[key]}
        return {False, None}


class Controller:
    '''
    控制器：业务逻辑，作为视图和模型的中间层
    '''
    def __init__(self):
        self.model = Model()

    def to_register(self, name, sex, age, password):
        '''
        注册
        :param name: 用户名
        :param sex: 用户性别
        :param age: 用户年龄
        :param password: 密码
        :return: True: 注册成功 False: 注册失败
        '''
        return self.model.register(name, sex, age, password)

    def to_login(self, name, password):
        '''
        用户登录
        :param name: 用户名
        :param password:　密码
        :return:　{flag, User} : {True, user} / {False , None} 登录成功，重定向至show方法．　登录失败，重定向至main方法
        '''
        return self.model.check_user(name, password)


def main():
    '''
    视图层，只负责展示信息
    :return:
    '''
    while True:
        want = input('What you want, [R]egister or [L]ogin (Others to leave)?')
        controller = Controller()
        if want == 'R':
            name = input('Input your name for register: ')
            sex = input('Input your sex for register: ')
            age = input('Input your age for register: ')
            password = input('Input your password for register: ')
            if controller.to_register(name, sex, age, password):
                print('Register Success!!!')
            else:
                print('The user not exit in database')
        elif want == 'L':
            name = input('Input your name for login: ')
            password = input('Input your password for login: ')
            flag, user = controller.to_login(name, password)
            if flag:
                show(user)
            else:
                print('The {} is not in database, please to register'.format(name))
        else:
            print('Bye...')
            break


main()
