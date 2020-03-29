# !python3.8
# assign.py: tuple example
zhangsan = ({'name': ('张三', '小张')}, {'age' : ('1996-05-06', '1992-08-10')})
print('张三的大名: %s, 张三的小名: %s.' %(zhangsan[0]['name'][0], zhangsan[0]['name'][1]))
print('张三的生日:')
print('公历: %s, 农历: %s.' %(zhangsan[1]['age'][0], zhangsan[1]['age'][1]))
print()
liming = ({'name': ('李明', '小李')}, {'age' : ('1995-08-16', '1995-07-21')})
print('李明的大名: %s, 李明的小名: %s.' %(liming[0]['name'][0], liming[0]['name'][1]))
print('李明的生日:')
print('公历: %s, 农历: %s.' %(liming[1]['age'][0], liming[1]['age'][1]))
print()
hanmeimei = ({'name': ('韩梅梅', '小韩')}, {'age' : ('1997-09-06', '1997-08-05')})
print('韩梅梅的大名: %s, 韩梅梅的小名: %s.' %(hanmeimei[0]['name'][0], hanmeimei[0]['name'][1]))
print('韩梅梅的生日:')
print('公历: %s, 农历: %s.' %(hanmeimei[1]['age'][0], hanmeimei[1]['age'][1]))

