from collections import namedtuple

SurName = ["zhangsan", "lisi", "wangwu"]
NickName = ["zhangxiaosan", "lixiaosi", "wangxiaowu"]

Wcalender = ["1990.09.09", "1992.09.09", "1995.09.09"]
Ccalender = ["1990.02.02", "1992.02.02", "1995.05.05"]
Name = namedtuple("name", ["surName","nickName"])
Birthday = namedtuple("birthday", ["wcalender", "ccalender"])

user = namedtuple("user", ["name", "sex", "birthday"])

for i in range(3):
    User = user(name = Name(SurName[i], NickName[i]), sex = "male", birthday = Birthday(Wcalender[i], Ccalender[i]))

    print("大名:", User.name.surName)
    print("小名:", User.name.nickName)
    print("性别:", User.sex)
    print("阳历生日:", User.birthday.wcalender)
    print("阴历生日:", User.birthday.ccalender)