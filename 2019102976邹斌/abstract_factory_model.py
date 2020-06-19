"""
by zoubin
模拟抽象工厂类：该程序有两组类，分别为　１．人(Person)和人的朋友(PFriend)，２．动物(Animal)和动物朋友(AFriend)，主要执行规则是：
模拟生物和他的朋友的简单交互过程，该过程采用调用生物的play()方法打印字符串方式实现．在这里存在两个抽象工厂(PRelation和ARelation)，
用于根据用户的输入(A: 动物，P: 人类)，创造不同的对象．之后模拟对象之间的交互．World类负责接受用户输入并启动该交互场景和交互过程

Person: 人类
PFriend:　人类朋友，与人类交互
Animal:　动物
AFriend:　动物朋友，与动物交互
PRelation:　抽象工厂，用于生成人类和人类朋友对象
ARelation:　抽象工厂，用于生成动物和动物朋友对象
World:　场景启动，根据用户输入，使用不同的抽象工厂，生成不同的对象后，执行对象间交互动作
"""


class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def play(self, friend):
        '''
        定义人与人的朋友交互的动作
        :param friend: 人的朋友对象 (PFriend)
        :return: 无
        '''
        print('A person {} with {} to {}'.format(self, friend, friend.action))


class PFriend:
    def __str__(self):
        return 'they friend'

    @property
    def action(self):
        '''
        定义与人交互的动作
        :return: 交互动作字符串
        '''
        return 'play basketball'


class PRelation:
    def __init__(self, name):
        self.name = name

    def get_a_creature(self):
        '''
        生成人类实例的工厂方法
        :return: Person
        '''
        return Person(self.name)

    def get_a_friend(self):
        '''
        生成人类朋友实例的工厂方法
        :return: PFriend
        '''
        return PFriend()


class Animal:
    def __init__(self, kind):
        self.kind = kind

    def __str__(self):
        return self.kind

    def play(self, friend):
        '''
        定义与动物朋友交互的动作
        :param friend: 动物的朋友对象 (PFriend)
        :return: 无
        '''
        print('A {} with {} to {}'.format(self, friend, friend.action))


class AFriend:
    def __str__(self):
        return 'it friend'

    @property
    def action(self):
        '''
        定义与动物交互的动作
        :return: 交互动作字符串
        '''
        return 'get food'


class ARelation:
    def __init__(self, kind):
        self.kind = kind

    def get_a_creature(self):
        '''
        生成动物实例的工厂方法
        :return: Animal
        '''
        return Animal(self.kind)

    def get_a_friend(self):
        '''
        生成动物朋友实例的工厂方法
        :return: AFriend
        '''
        return AFriend()


class World:
    def __init__(self, abstract_factory):
        '''
        根据用户输入信息，使用对应抽象工厂创建对应对象
        :param abstract_factory:
        '''
        self.creature = abstract_factory.get_a_creature()
        self.friend = abstract_factory.get_a_friend()

    @property
    def go_on(self):
        '''
        根据创建的抽象工厂创建的对象，来模拟启动对象间的交互过程
        :return:
        '''
        self.creature.play(self.friend)


def main():
    kind = input('Animal or Person?[animal: a, person: p]')
    creature = None
    factory = None
    if kind == 'a':
        creature = input('type the kind of animal: ')
        factory = ARelation
    elif kind == 'p':
        creature = input('type a name of person: ')
        factory = PRelation
    world = World(factory(creature))
    world.go_on


main()
