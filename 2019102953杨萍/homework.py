from collections import namedtuple
Name = namedtuple('name',['surName','nickName'])
Age = namedtuple('age',['wcalender','ccalender'])
User =namedtuple('user',['Name','sex','Age'])
User1 =User._make([Name('小明','明明'),'man',Age('17','18')])
User2 =User._make([Name('小红','红红'),'woman',Age('16','17')])
User3 =User._make([Name('小美','美美'),'woman',Age('15','16')])

print("大名:"+User1.Name.surName,"小名:"+User1.Name.nickName,"性别:"+User1.sex,"周岁:"+User1.Age.wcalender,"虚岁:"+User1.Age.ccalender)
print("大名:"+User2.Name.surName,"小名:"+User2.Name.nickName,"性别:"+User2.sex,"周岁:"+User2.Age.wcalender,"虚岁:"+User2.Age.ccalender)
print("大名:"+User3.Name.surName,"小名:"+User3.Name.nickName,"性别:"+User3.sex,"周岁:"+User3.Age.wcalender,"虚岁:"+User3.Age.ccalender)
