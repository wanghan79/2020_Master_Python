from collections import namedtuple
Name = namedtuple('Name', ['surName', 'nickName'])
Birth = namedtuple('Birth', ['wCalender', 'cCalender'])
User = namedtuple('User', ['name', 'sex', 'birth'])
User1 = (Name('zhangsan', 'zhang'), 'male', Birth('0709', '0521'))
User2 = (Name('lisi', 'li'), 'male', Birth('0809', '0711'))
User3 = (Name('wangerma', 'wang'), 'male', Birth('0928', '0733'))
users = [User1, User2, User3]
for i in range(0, 3):
print(user[i].name.surName)
print(user[i].name.nickName)
print(user[i].sex)
print(user[i].birth.wCalender)
print(user[i].birth.cCalender)
print() 