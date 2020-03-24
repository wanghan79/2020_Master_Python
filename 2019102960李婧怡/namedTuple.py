from collections import namedtuple

user = namedtuple('user', ['name', 'sex', 'birthday'])
name = namedtuple('name', ['surname', 'nikename'])
birthday = namedtuple('birthday', ['solarcalendar', 'lunarcalendar'])

user1 = user(name('李婧怡', '萌萌'), 'female', birthday('03.11', '二月初三'))
user2 = user(name('李妈妈', '荣荣'), 'female', birthday('03.11', '二月十五'))
user3 = user(name('李爸爸', '海海'), 'male', birthday('10.13', '九月二十五'))

userlist = [user1, user2, user3]     #用户列表

for i in userlist:
    print("surname:",i.name.surname)
    print("nikename:",i.name.nikename)
    print("sex:",i.sex)
    print("solarcalendar:",i.birthday.solarcalendar)
    print("lunarcalendar:",i.birthday.lunarcalendar)
    print("******************************")