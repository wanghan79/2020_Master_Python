'''
by zoubin
模拟适配器模式：该程序模拟适配器模式：在main函数中只能调用对象的speak函数，采用适配器类Adapter包装B类，实现在不改变main函数和A类的前提下main函数兼容B类

Ａ：类为老类，假设无法修改．
B：类为需兼容类，他需要兼容当前API的方法为execute
main方法：　已存在API为main函数．假设无法修改，只会调用speak方法．
通过dict: 适配器相当于是一个原始API模板，我们要做的就是如何利用语言自身的特性，把新的功能，转化为适合这个模板

已解决书中问题：　为什么在main函数中的for循环中调用obj.name会报错?
                原因：Adapter类中没有name属性，因为对象数组中保存的是一个A类和一个Adapter类．解决方法：利用Adapter的__dict__属性建立name属性到B.name的映射．
'''


class A:
    def __init__(self, name):
        self.name = name
        self.zb = 'zoubin'

    def __str__(self):
        return self.name

    def speak(self):
        return 'my name is {}'.format(self.name)


class B:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def execute(self):
        return 'They name is {}'.format(self.name)


class Adapter:
    def __init__(self, obj, adapted_method):
        '''

        :param obj: 需要适配的类
        :param adapted_method: 需要适配的类的方法
        '''
        self.obj = obj
        self.__dict__.update(adapted_method)

    def __str__(self):
        return str(self.obj)


def main():
    objects = [A('Alis')]
    b = B('Bob')
    objects.append(Adapter(b, dict(speak=b.execute, name=b.name)))

    for ob in objects:
        print('{} {}'.format(ob.name, ob.speak()))

    print(dir(objects[1]))


main()
