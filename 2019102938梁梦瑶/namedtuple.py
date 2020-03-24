from collections import namedtuple
User=namedtuple('User',['name','sex','birth'])
class name():
    def __init__(self,surName,nickName):
        self.surName=surName
        self.nickName=nickName
class birth():
    def __init__(self,wcalendar,ccalendar):
        self.wcalendar=wcalendar
        self.ccalendar=ccalendar
users=[(name('Dell Curry','pupil'),'male',birth('0625','0701')),
       (name('zhangjike','keke'),  'male',birth('0216','0445')),
       (name('jindong','jinsisui'),  'male',birth('1222','1111'))]
for user in users:
    user=User._make(user)
    print(user)
    print(user.name.surName)
    print(user.name.nickName)
    print(user.sex)
    print(user.birth.wcalendar)
    print(user.birth.ccalendar)
