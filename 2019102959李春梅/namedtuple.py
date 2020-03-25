from collections import namedtuple

User = namedtuple('User', ['Name', 'Sex', 'Birth'])# 定义一个namedtuple类型User,并包含Name,Sex和Birth属性
Name = namedtuple('name', ['surName', 'nickName'])# 定义一个namedtuple类型Name,并包含surName和nickName属性
Birth = namedtuple('birth', ['wcalender', 'ccalender'])# 定义一个namedtuple类型Birth,并包含wcalender和ccalender属性

users = [
    (Name('李春梅','李漂亮'), 'female', Birth('19940614','19940722')),
    (Name('孙红雷','孙漂亮'), 'male', Birth('19700816','19700715')),
    (Name('张艺兴','小绵羊'), 'male', Birth('19911007', '19940830'))
]

for user in users:
    user = User._make(user)

    print('大名：' + user.Name.surName)
    print('小名：' + user.Name.nickName)
    print('性别：' + user.Sex)
    print('阳历生日：' + user.Birth.wcalender)
    print('阴历生日：' + user.Birth.ccalender)
