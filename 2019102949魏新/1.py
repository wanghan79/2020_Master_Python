from collections import namedtuple

Name = namedtuple('Name', ['surName', 'nickName'])
Birth = namedtuple('Birth', ['wCalender', 'cCalender'])
User = namedtuple('User', ['name', 'sex', 'birth'])

User1 = User._make([Name('小明', '明子'), 'man', Birth('0122', '二月初一')])
User2 = User._make([Name('小强', '强子'), 'man',Birth('0215', '三月初一')])
User3 = User._make([Name('小美', '美子'), 'woman',Birth('0301', '四月初一')])

print(User1.name.surName, User1.name.nickName, User1.birth.wCalender, User1.birth.cCalender, User1.sex)
print(User2.name.surName, User2.name.nickName, User2.birth.wCalender, User2.birth.cCalender, User2.sex)
print(User3.name.surName, User3.name.nickName, User3.birth.wCalender, User3.birth.cCalender, User3.sex)