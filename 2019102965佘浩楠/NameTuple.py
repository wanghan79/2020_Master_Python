import collections

user = collections.namedtuple("user",['name','sex','age'])
name = collections.namedtuple("name",["surName" ,"givenName"])
birth = collections.namedtuple("birth",["solarcalender", "lunarcalender"])

user_one = user._make([name('王','大锤'),'女',birth('20200101','十二月初七')])
user_two = user._make([name('李','二锤'),'女',birth('20150101','十一月二十二')])
user_three = user._make([name('张','三锤'),'男',birth('20100101','十一月十七')])
userlist = [user_one,user_two,user_three]

for i in userlist:
    print('--------------')
    print("surName:",i.name.surName)
    print("nickName:",i.name.givenName)
    print("Sex:",i.sex)
    print("wcalender:",i.age.solarcalender)
    print("ccalender:",i.age.lunarcalender)
    print('--------------')