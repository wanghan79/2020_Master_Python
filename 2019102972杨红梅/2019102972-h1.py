from collections import namedtuple

user = namedtuple('user',['name','sex','birthday'])
name = namedtuple('name',['surname','nikename'])
birthday = namedtuple('birthday',['wcalender','ccalender'])

user1 = user(name('杨红梅','May'),'female',birthday('10.13','9.2'))
user2 = user(name('张利飒','Lisa'),'female',birthday('9.22','9.10'))
user3 = user(name('邬伟业','叶子'),'female',birthday('11.05','10.25'))

userinfo = [user1,user2,user3]
#print(user1.name.surname)
print("userinfo as follows:")

for item in userinfo:
    print("surname is {}".format(item.name.surname))  # 这里需要注意format()的用法。
    print("nikename is {}".format(item.name.nikename))
    print("wcalender is {0}".format(item.birthday.wcalender))
    print("ccalender is {0}".format(item.birthday.ccalender))
    print("sex is {0}".format(item.sex))
    print("----------分割线----------")














