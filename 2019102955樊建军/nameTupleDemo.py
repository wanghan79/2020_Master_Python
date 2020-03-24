from collections import namedtuple

Name = namedtuple('name',['surName','nickName'])
Birthday = namedtuple('birthday', ['wcalender','ccalender'])
User = namedtuple('User',['Name','sex', 'Birthday'])

userList = [
    [['王','一博'],'男',["1992-12-1","1993-1-2"]],
    [['肖','战'], '男', ["1995-5-1","1995-5-27"]],
    [['陈','钰琪'], '女', ["1996-3-1","1996-4-2"]]
]


for iter in userList:
    iter[0] = Name._make(iter[0])
    iter[2] = Birthday._make(iter[2])

userInfo = []
for user in userList:
    userInfo.append(User._make(user))

for num in range(0,3):
    print("姓： " + userInfo[num].Name.surName)
    print("名： " + userInfo[num].Name.nickName)
    print("性别 " + userInfo[num].sex)
    print("出生年月（公历）：" + userInfo[num].Birthday.wcalender)
    print("出生年月（农历）：" + userInfo[num].Birthday.ccalender)
    print("***************************")
