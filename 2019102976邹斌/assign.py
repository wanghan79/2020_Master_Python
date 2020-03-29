# !python3.8
# assign.py: namedtuple example
from collections import namedtuple
Students = namedtuple('Students', ['name', 'age'])

list_students = []

zhangsan = Students._make([{'name':'张三', 'nickname':'小张'}, {'G_calendar':'1996-06-16', 'L_calendar':'1996-05-01'}])
list_students.append(zhangsan)
liming = Students(name = {'name':'李明', 'nickname':'小李'}, age = {'G_calendar':'1997-06-10', 'L_calendar':'1997-05-06'})
list_students.append(liming)
hanmeimei = Students._make([{'name':'韩梅梅', 'nickname':'小韩'}, {'G_calendar':'1998-06-12', 'L_calendar':'1998-05-08'}])
list_students.append(hanmeimei)

for student in list_students:
    print('学生的大名: %s, 小名: %s.' %(student.name['name'], student.name['nickname']))
    print('学生的生日(公历): %s, 农历: %s' %(student.age['G_calendar'], student.age['L_calendar']))
