from collections import namedtuple

Name = namedtuple('Name', ['surName', 'nickName'])
Birth = namedtuple('Birth', ['wCalender', 'cCalender'])
User = namedtuple('User', ['name', 'sex', 'birth'])

name = Name('wangkefei', 'wang')
birth = Birth('0310', '0202')
user1 = User(name=name, sex='female', birth=birth)

name = Name('Jackson', 'Jackie')
birth = Birth('0901', '0729')
user2 = User(name=name, sex='male', birth=birth)

name = Name('Hathaway', 'Hath')
birth = Birth('1211', '1102')
user3 = User(name=name, sex='female', birth=birth)

user = [user1, user2, user3]

for i in range(0, 3):
    print(user[i].name.surName)
    print(user[i].name.nickName)
    print(user[i].sex)
    print(user[i].birth.wCalender)
    print(user[i].birth.cCalender)
    print()