from collections import namedtuple

User = namedtuple('User', ['name', 'sex', 'birthday'])
Name = namedtuple('Name', ['surName', 'nickName'])
birthday = namedtuple('birthday', ['wcalendar', 'ccalendar'])

user1 = User(Name('孙尚香', '香香'), 'female', birthday('09.02', '八月初二'))
user2 = User(Name('韩信', '韩跳跳'), 'male', birthday('05.20', '四月初八'))
user3 = User(Name('小乔', '乔妹妹'), 'female', birthday('03.03', '二月初一'))

userlist = [user1, user2, user3]

for i in userlist:
    print("surName:",i.name.surName)
    print("nickName:",i.name.nickName)
    print("sex:",i.sex)
    print("wcalendar:",i.birthday.wcalendar)
    print("ccalendar:",i.birthday.ccalendar)
    print("******************************")