'''from collections import namedtuple

Name = namedtuple('name', ['surName', 'nickName'])
Birth = namedtuple('Birth', ['Lunar_calendar', 'Solar_calendar'])
star = namedtuple('star', ['Name', 'sex', 'Birth'])

name1 = Name(surName='潘', nickName='长江')
name2 = Name(surName='周', nickName='杰伦')
name3 = Name(surName='贾', nickName='玲')
name4 = Name(surName='沈', nickName='腾')
name5 = Name(surName='贾', nickName='乃亮')
Birth1 = Birth(Lunar_calendar='6/23', Solar_calendar='7/1')
Birth2 = Birth(Lunar_calendar='12/26', Solar_calendar='1/18')
Birth3 = Birth(Lunar_calendar='3/19', Solar_calendar='4/29')
Birth4 = Birth(Lunar_calendar='9/13', Solar_calendar='10/23')
Birth5 = Birth(Lunar_calendar='2/27', Solar_calendar='4/12')
star1 = star(name1, '男', Birth1)
star2 = star(name2, '男', Birth2)
star3 = star(name3, '女', Birth3)
star4 = star(name4, '男', Birth4)
star5 = star(name5, '男',Birth5)
List = [star1, star2, star3,star4,star5]
for iter in List:
    print("大名：" + iter[0][0], "小名：" + iter[0][1], "性别：" + iter[1], "阴历生日：" + iter[2][0], "阳历生日：" + iter[2][1])
'''
from collections import namedtuple
User = namedtuple('User', ['Name', 'Sex', 'Birth'])
Name = namedtuple('Name', ['surName', 'nickName'])
Birth = namedtuple('Birth', ['Lunar_calendar', 'Solar_calendar'])

allUsers = ([Name('贾玲','贾小胖'),'女',Birth('4/27','3/12')],
            [Name('华晨宇','花花'),'男',Birth('3/19','1/27')],
            [Name('于震','大长脸'),'男',Birth('5/17','4/2')],
            [Name('机器猫','蓝胖子'),'男',Birth('10/1','9/5')]
            )

for user in allUsers:
    user = User._make(user)
    #print(user)
    print('大名：'+user.Name.surName+'\t'+'小名：'+user.Name.nickName+
          '\t'+'性别：'+user.Sex+'\t'+'阳历生日：'+user.Birth.Solar_calendar+
          '\t'+'阴历生日：'+user.Birth.Lunar_calendar)







