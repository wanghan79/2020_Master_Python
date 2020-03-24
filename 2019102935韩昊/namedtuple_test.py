from collections import namedtuple

user = namedtuple("user", ['name','sex', 'age'])
name = namedtuple("name", ["surName", "nickName"])
birth = namedtuple("birth", ["wcalender", "ccalender"])

people_one = user._make([name('张', '三'), '男', birth('1','10')])
people_two = user._make([name('李', '四'), '女', birth('2','20')])
people_three = user._make([name('王', '五'), '男', birth('3','30')])
userlist = [people_one, people_two, people_three]
#创建一个userlist

for i in userlist:
    #循环输出userlist中的对象
    print("surName:", i.name.surName)
    print("nickName:", i.name.nickName)
    print("Sex:", i.sex)
    print("wcalender:", i.age.wcalender)
    print("ccalender:", i.age.ccalender)
    print('------------------')



