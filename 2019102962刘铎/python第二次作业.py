import collections

user=collections.namedtuple("user","name sex age")
name=collections.namedtuple("name","surName nickName")
birth=collections.namedtuple("birth","wcalender ccalender")

liu1=user(name('刘','铎'),'男',birth('24','25'))
liu2=user(name('刘','一'),'男',birth('13','14'))
liu3=user(name('刘','二'),'女',birth('30','31'))
list=[liu1,liu2,liu3]

#print(user.name)
#print(user.sex)
#print(user.age)
#print(liu1.name.surName)
#print(liu2.age.wcalender)

for i in list:
    print("Surname is {}".format(i.name.surName))
    print("nickname is {}".format(i.name.nickName))
    print("wcalender is {}".format(i.age.wcalender))
    print("ccalender is {}".format(i.age.ccalender))
    print("sex is {}".format(i.sex))
    print("----------------------------")

