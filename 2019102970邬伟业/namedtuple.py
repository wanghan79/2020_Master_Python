from collections import namedtuple

user = namedtuple('user', ['name', 'sex', 'birthday'])
name = namedtuple('name', ['surname', 'nikename'])
birthday = namedtuple('birthday', ['solarcalendar', 'lunarcalendar'])

user1 = user(name('wuweiye', 'yezi'), 'female', birthday('11.08', '10月初9'))
user2 = user(name('yangjiaxue', 'xiaoxue'), 'female', birthday('11.16', '10月17'))
user3 = user(name('wuweihao', 'haozi'), 'male', birthday('7.23', '6月24'))

ulist = [user1, user2, user3]

for users in ulist:
    print("surname:",users.name.surname)
    print("nikename:",users.name.nikename)
    print("sex:",users.sex)
    print("solarcalendar:",users.birthday.solarcalendar)
    print("lunarcalendar:",users.birthday.lunarcalendar)