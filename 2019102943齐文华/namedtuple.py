from collections import namedtuple
Name = namedtuple('Name', ['surName', 'nickName'])
Birth = namedtuple('Birth', ['sCalendar', 'lCalendar'])
User = namedtuple('User', ['name', 'sex', 'birth'])
User_one = (Name('Wenhua', 'Xiaohua'), 'female', Birth('19950301', '19950331'))
User_two = (Name('liming', 'Lucy'), 'female', Birth('19960501', '19950706'))
User_three = (Name('Xiaoqiang', 'Juhn'), 'male', Birth('19970206', '19970401'))
users = [User_one, User_two, User_three]
for i in users:
    i = User._make(i)
    print('surName：' + i.name.surName)
    print('nickName：' + i.name.nickName)
    print('sex：' + i.sex)
    print('sCalendar：' + i.birth.sCalendar)
    print('lCalender：' + i.birth.lCalendar)