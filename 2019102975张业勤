import collections
from collections import namedtuple

Name = namedtuple('Name', ['surName', 'nickName'])
Birth = namedtuple('Birth', ['wCalender', 'cCalender'])
Student = namedtuple('Student', ['name', 'sex', 'birth'])
name = Name('张业勤', 'Jack')
birth = Birth('0311', '0222')
stu1 = Student(name=name, sex='男', birth=birth)
name = Name('张亚勤', 'Tom')
birth = Birth('0801', '0605')
stu2 = Student(name=name, sex='男', birth=birth)
name = Name('张业谨', 'Antoine')
birth = Birth('1111', '1001')
stu3 = Student(name=name, sex='男', birth=birth)
student = [stu1, stu2, stu3]
for i in range(0, 3):
    print(student[i].name.surName)
    print(student[i].name.nickName)
    print(student[i].sex)
    print(student[i].birth.wCalender)
    print(student[i].birth.cCalender)
    print()
