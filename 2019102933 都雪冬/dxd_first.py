import collections

user = collections.namedtuple("user",['name','sex','age'])
name = collections.namedtuple("name",["surName" ,"nickName"])
birth = collections.namedtuple("birth",["wcalender", "ccalender"])

people_one = user._make([name('张','三'),'女',birth('3','24')])
people_two = user._make([name('李','四'),'女',birth('3','24')])
people_three = user._make([name('王','二'),'男',birth('4','25')])
peoplelist = [people_one,people_two,people_three]

for i in peoplelist:
    print("surName:",i.name.surName)
    print("nickName:",i.name.nickName)
    print("Sex:",i.sex)
    print("wcalender:",i.age.wcalender)
    print("ccalender:",i.age.ccalender)
    print('--------------')
