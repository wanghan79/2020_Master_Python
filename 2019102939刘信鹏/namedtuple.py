from collections import namedtuple

Name = namedtuple('Name', ['surName', 'nickName'])
Birth = namedtuple('Birth', ['wCalender', 'cCalender'])
User = namedtuple('User', ['name', 'sex', 'birth'])

for i in range(1, 4):
    # 这里简化初始化过程，每次循环将nickName设置为循环次数
    name = Name('Liu', i)
    birth = Birth('0513', '0322')
    # 此处为实现二级namedtuple的关键代码，将namedtuple中的属性值同样设置为namedtuple类型的实例
    user = User(name=name, sex='male', birth=birth)
    print(user.name.surName)
    print(user.name.nickName)
    print(user.birth.wCalender)
    print(user.birth.cCalender)