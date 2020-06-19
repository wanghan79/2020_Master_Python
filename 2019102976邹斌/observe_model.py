'''
by zoubin
模拟观察者模式，将发布者的基础功能抽象至父类Publisher，使用DefaultFormatter类继承Publisher类进行扩展．
主要模拟：当Publisher的_data属性发生改变时，通知注册的观察者进行响应，本该示例代码主要是观察者打印Publisher的_data信息

Publisher:　发布者父类，提供消息发布者的基础功能和_data信息
DefaultFormatter: 发布者的扩展类，主要扩展消息发布者的唤醒观察者的方式机制
HexFormatter:　观察者，以十六进制形式打印更改后的发布者的_data属性
BinaryFormatter:　观察者，以二进制形式打印更改后的发布者的_data属性
'''


class Publisher:
    def __init__(self):
        '''
        初始化注册观察者列表
        '''
        self.observes = []

    def add(self, observe):
        '''
        向观察者注册列表observes中添加观察者
        :param observe: 观察者
        :return: 无
        '''
        if observe not in self.observes:
            self.observes.append(observe)
        else:
            print('Failed to add: {}'.format(observe))

    def remove(self, observe):
        '''
        删除观察者列表observes中已存在的观察者
        :param observe: 观察者
        :return: 无
        '''
        try:
            self.observes.remove(observe)
        except ValueError:
            print('Failed to remove: {}'.format(observe))
        else:
            print('Success to remove: {}'.format(observe))

    def notify(self):
        for o in self.observes:
            o.notify(self)


class DefaultFormatter(Publisher):
    def __init__(self, name):
        Publisher.__init__(self)
        self.name = name
        self._data = 0

    def __str__(self):
        return "{}: '{}' has data = {}".format(type(self).__name__, self.name, self._data)

    @property
    def data(self):
        return self._data

    def set_data(self, new_value):
        '''
        定义当消息发布者Publisher的_data属性发生变化时，调起观察者的机制
        :param new_value:
        :return:
        '''
        try:
            self._data = int(new_value)
        except ValueError as e:
            print('Error: {}'.format(e))
        else:
            self.notify()


class HexFormatter:
    def notify(self, publisher):
        '''
        当该观察者被唤醒时，执行的响应操作：以二进制打印Publisher的_data属性
        :param publisher: 该观察者注册的发布者
        :return: 无
        '''
        print("{}: '{}' has now hex data = {}".format(type(self).__name__,
                                                      publisher.name, hex(publisher.data)))


class BinaryFormatter:
    def notify(self, publisher):
        '''
        当该观察者被唤醒时，执行的响应操作：以二进制打印Publisher的_data属性
        :param publisher: 该观察者注册的发布者
        :return: 无
        '''
        print("{}: '{}' has now binary data = {}".format(type(self).__name__,
                                                         publisher.name, bin(publisher.data)))


def main():
    df = DefaultFormatter('default formatter')
    print(df)

    hf = HexFormatter()
    bf = BinaryFormatter()

    df.add(hf)
    df.add(bf)

    df.add(bf)

    df.set_data(10)

    df.remove(hf)
    df.remove(hf)


main()
