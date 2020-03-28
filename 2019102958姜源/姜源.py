from collections import namedtuple
Name = namedtuple('Name', ['surName', 'nickName'])
Birth = namedtuple('Birth', ['wCalender', 'cCalender'])
User = namedtuple('User', ['name', 'sex', 'birth'])
User1 = (Name('liming', 'li'), 'male', Birth('0712', '0524'))
User2 = (Name('zhanghong', 'zhang'), 'male', Birth('0819', '0721'))
User3 = (Name('zhaoliang', 'zhao'), 'male', Birth('0908', '0713'))
users = [User1, User2, User3]
for i in range(0, 3):
print(user[i].name.surName)
print(user[i].name.nickName)
print(user[i].sex)
print(user[i].birth.wCalender)
print(user[i].birth.cCalender)
print() 