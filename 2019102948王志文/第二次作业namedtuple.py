from collections import namedtuple
Name = namedtuple('Name', 'surName nickName')
Birth = namedtuple('Birth', 'sCalendar lCalendar')
User = namedtuple('User', 'name sex birth')

first = (Name('小明', '明明'), 'male', Birth('0102', '0304'))
second = (Name('小红', '红红'), 'female', Birth('0506', '0708'))
third = (Name('小华', '华华'), 'female', Birth('0910', '1112'))
users = [first, second, third]
for i in users:
    i = User._make(i)
    print('大名：' + i.name.surName)
    print('小名：' + i.name.nickName)
    print('性别：' + i.sex)
    print('阳历生日：' + i.birth.sCalendar)
    print('阴历生日：' + i.birth.lCalendar)