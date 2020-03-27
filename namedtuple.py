from collections import namedtuple

SurName = ["小明", "小红", "小白"]
NickName = ["mingming", "honghong", "baibai"]

Wcalender = ["2020.03.01", "2020.03.02", "2020.03.03"]
Ccalender = ["2020.02.08", "2020.02.09", "2020.02.10"]
Name = namedtuple("name", ["surName","nickName"])
Birthday = namedtuple("birthday", ["wcalender", "ccalender"])

user = namedtuple("user", ["name", "sex", "birthday"])

for i in range(3):
    User = user(name = Name(SurName[i], NickName[i]), sex = "female", birthday = Birthday(Wcalender[i], Ccalender[i]))

    print("大名:", User.name.surName)
    print("小名:", User.name.nickName)
    print("性别:", User.sex)
    print("阳历生日:", User.birthday.wcalender)
    print("阴历生日:", User.birthday.ccalender)