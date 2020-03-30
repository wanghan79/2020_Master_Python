from collections import namedtuple

User=namedtuple('user', ['Name', 'Sex', 'Birth'])
Name=namedtuple('name',['surName','nickName'])
Birth=namedtuple('birth',['wcalender','ccalender'])

users=[ (Name('洪伟华1','洪伟华2'), 'male', Birth('19971010','19971010')),
    (Name('洪伟华3','洪伟华4'), 'female', Birth('19961230','19961230')),
    (Name('洪伟华5','洪伟华6'), 'male', Birth('18890206', '18890206'))]

for user in users:
    user=User._make(user)
    print('大名:'+user.Name.surName)
    print('小名：' + user.Name.nickName)
    print('性别：' + user.Sex)
    print('阳历生日：' + user.Birth.wcalender)
    print('阴历生日：' + user.Birth.ccalender)