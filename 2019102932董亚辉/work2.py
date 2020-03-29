from collections import namedtuple

Name = namedtuple('Name', ['surName', 'nickName'])
Birth = namedtuple('Birth', ['wCalender', 'cCalender'])
User = namedtuple('User', ['name', 'sex', 'birthday'])

#第一位同学个人信息
name1 = Name(surName='WangEr', nickName='XiaoWang')
birthday1 = Birth(wCalender='07-08', cCalender='06-23')
user1 = User(name=name1, sex='female',  birthday=birthday1)

#第二位同学个人信息
name2 = Name(surName='ZhaoSi', nickName='XiaoZhao')
birthday2 = Birth(wCalender='01-02', cCalender='12-03')
user2 = User(name=name2, sex='male',  birthday=birthday2)

#第三位同学个人信息
name3 = Name(surName='MaZi', nickName='XiaoM')
birthday3 = Birth(wCalender='03-23', cCalender='02-20')
user3 = User(name=name3, sex='female',  birthday=birthday3)

StuList = [user1, user2, user3]

for user in StuList:
    print(user.name.surName)
    print(user.name.nickName)
    print(user.sex)
    print(user.birthday.wCalender)
    print(user.birthday.cCalender)