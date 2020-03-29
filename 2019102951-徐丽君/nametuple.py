from collections import namedtuple
SurName = ["xulijun", "lisi", "zhangsan"]
NickName = ["xlj", "ls", "zs"]
Wcalender = ["1994.09.09", "1993.09.09", "1995.08.11"]
Ccalender = ["1994.02.02", "1993.02.02", "1995.07.16"]
Name = namedtuple("name", ["surName", "nickName"])
Birthday = namedtuple("birthday", ["wcalender", "ccalender"])
user = namedtuple("user", ["name", "sex", "birthday"])
for i in range(3):
    User = user(name=Name(SurName[i], NickName[i]), sex="male", birthday=Birthday(Wcalender[i], Ccalender[i]))

    print("大名:", User.name.surName)

    print("小名:", User.name.nickName)

    print("性别:", User.sex)

    print("阳历生日:", User.birthday.wcalender)

    print("阴历生日:", User.birthday.ccalender)
