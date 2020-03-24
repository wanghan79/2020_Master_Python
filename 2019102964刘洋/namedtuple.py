from collections import namedtuple
# 定义一个namedtuple类型的Name,birth，分别包含各自的两个属性
Name = namedtuple('Name',['surName','nickName'])
Birth = namedtuple('Birth',['wcalender','ccalender'])
# 定义一个namedtuple类型的User，包含name,sex,birth三个属性
User = namedtuple('User',['name','sex','birth'])
for i in range(0,3):
    # 循环创建对象
    name = Name(surName='sunshangxiang',nickName='xiangxiang')
    birth = Birth(wcalender='0913',ccalender='1024')
    user = User(name=name,sex='female',birth=birth)
# 获取用户属性
print(user.name.surName)
print(user.name.nickName)
print(user.sex)
print(user.birth.wcalender)
print(user.birth.ccalender)