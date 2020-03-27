from collections import namedtuple

User = namedtuple("User", ["name", "sex", "birth"])
name = namedtuple("name", ["surname", "nickname"])
birth = namedtuple("birth", ["wcalender", "ccalender"])

firstuser = User(name("王一", "小一一"), "男", birth("20110101", "20110202"))
seconduser = User(name("王二", "小二二"), "男", birth("20120101", "20120202"))
thirduser = User(name("王三", "小三三"), "男", birth("20130101", "20130202"))
Userlist = [firstuser, seconduser, thirduser]
for i in Userlist:
    print("大名:{}\n小名:{}\n性别:{}\n阳历生日:{}\n阴历生日:{}".format(i.name.surname,\
i.name.nickname, i.sex, i.birth.wcalender, i.birth.ccalender))
    print("*" * 20)