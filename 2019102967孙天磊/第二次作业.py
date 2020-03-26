from collections import namedtuple

stu=namedtuple('stu',['name','sex','birthday'])
name=namedtuple('name',['CName','EName'])
sex=namedtuple('sex',['gender','age'])
birthday=namedtuple('birthday',['wcalender','ccalender'])

stu1=stu(name('赵','zhao'),sex('男','23'),birthday('1月1日','一月初一'))
stu2=stu(name('钱','qian'),sex('女','24'),birthday('2月2日','二月初二'))
stu3=stu(name('孙','sun'),sex('男','25'),birthday('3月3日','三月初三'))
student=[stu1,stu2,stu3]

print("学生信息如下：\n")
i=1
for j in student:
    z = str(i)
    print('第' + z + '个学生信息：')
    print('中文名：' + j.name.CName)
    print('英文名：' + j.name.EName)
    print('性别：' + j.sex.gender)
    print('年龄：' + j.sex.age)
    print('阳历生日：' + j.birthday.wcalender)
    print('阴历生日：' + j.birthday.ccalender)
    print('\n')
    i=i+1
print("全部学生信息显示完毕!")