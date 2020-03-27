from collections import namedtuple

User=namedtuple('User', ['name', 'sex', 'birth'])
name=namedtuple('name', ['surname', 'nickname'])
birth=namedtuple('birth', ['wcalender', 'ccalender'])

user1= User._make([name('wangxiaoming','xiaoming'),'male', birth('19970624','19970721')])
user2= User._make([name('zhangxiaohua','xiaohua'),'female',birth('19941102','19941128')])
user3= User._make([name('lixiaohong','xiaohong'),'female',birth('19960524','19960620')])
userlist=[user1,user2,user3]

for i in userlist:
    print(user1.name.surname)
    print(user2.name.nickname)
    print(user1.sex)
    print(user1.birth.wcalender)
    print(user1.birth.ccalender)
