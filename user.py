from collections import namedtuple

Name=namedtuple('Name','surName nickName')
Birth=namedtuple('Birth','wcalender ccalender')
User=namedtuple('User','name sex birth')

userlist=[]

name1=Name('daming','da')
birth1=Birth(1,2)
user1=User(name1,'male',birth1)
userlist.append(user1)

name2=Name('sam','sa')
birth2=Birth(3,4)
user2=User(name2,'male',birth2)
userlist.append(user2)

name3=Name('amy','am')
birth3=Birth(5,6)
user3=User(name3,'female',birth3)
userlist.append(user3)

for i in range(0,3):
  print(userlist[i].name.surName)
  print(userlist[i].name.nickName)
  print(userlist[i].sex)
  print(userlist[i].birth.wcalender)
  print(userlist[i].birth.ccalender)
  print('\n')