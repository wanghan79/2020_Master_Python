from collections import namedtuple

Name = namedtuple('Name', 'surName nickName')
Birth = namedtuple('Birth', 'sCalendar lCalendar')
User = namedtuple('User', 'name sex birth')

one = (Name('熊大', '大大'), 'female', Birth('0101', '0202'))
two = (Name('熊二', '二二'), 'female', Birth('0303', '0404'))
three = (Name('光头强', '强强'), 'male', Birth('0505', '0606'))
users = [one, two, three]
for i in users:
    i = User._make(i)
    print('大名：' + i.name.surName)
    print('小名：' + i.name.nickName)
    print('性别：' + i.sex)
    print('阳历生日：' + i.birth.sCalendar)
    print('阴历生日：' + i.birth.lCalendar)