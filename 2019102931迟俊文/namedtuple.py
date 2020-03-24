from collections import namedtuple

Name = namedtuple('Name', 'surName nickName')
Birth = namedtuple('Birth', 'wCalender cCalender')
User = namedtuple('User', 'name sex birth')

for each in range(1, 4):
    # 循环 并且 将Name，Birth，User对象实例化
    name = Name('Liu', each)
    birth = Birth('0513', '0322')
    user = User._make([name,'male', birth])
    
    print(user.name.surName)
    print(user.name.nickName)
    print(user.birth.wCalender)
    print(user.birth.cCalender)
