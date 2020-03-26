from collections import namedtuple

Name = namedtuple('name', ('surname', 'nickname'))
Birth = namedtuple('birth', ('wbirth', 'cbirth'))
Info = namedtuple('info', ('Name', 'sex', 'Birth'))

name1 = Name(surname='fu', nickname='FU')
name2 = Name(surname='yu', nickname='YU')
name3 = Name(surname='ze', nickname='ZE')
birth1 = Birth(wbirth='0525', cbirth='0409')
birth2 = Birth(wbirth='0526', cbirth='0410')
birth3 = Birth(wbirth='0527', cbirth='0411')
info1 = Info(name1, 'male', birth1)
info2 = Info(name2, 'male', birth2)
info3 = Info(name3, 'male', birth3)
List = [info1, info2, info3]
for iter in List:
    print("大名：" + iter[0][1], "小名：" + iter[0][0], "性别：" + iter[1], "阳历生日：" + iter[2][0], "阴历生日：" + iter[2][1])
