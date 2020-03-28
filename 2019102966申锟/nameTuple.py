from collections import namedtuple

User = namedtuple('User', ['Name', 'Sex', 'Birth'])
Name = namedtuple('name', ['surName', 'nickName'])
Birth = namedtuple('birth', ['wcalender', 'ccalender'])

User1 = User(Name('后羿','太阳的后裔'), '男的', Birth('20200328','20200328'))
User2 = User(Name('李白','李白不太白'), '男的', Birth('20200328','20200328'))
User3 = User(Name('孙悟空','猴崽子'), '公的', Birth('20200328', '20200328'))
userlist = [User1,User2,User3]

for user in userlist:
    print(user.Name.surName)
    print(user.Name.nickName)
    print(user.Sex)
    print(user.Birth.wcalender)
    print(user.Birth.ccalender)
    print("----------我是华丽分割线----------")