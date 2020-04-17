import random
def randomnumble():
 Setnumble=set()
 for i in range(1000):
    Setnumble.add(random.uniform(0,100))
 for i in Setnumble:
    if (i>=20 and i<=50):
      print(i)
def randomstr():
 Setstr=set()
 for j in range(1000):
    Setstr.add(random.choice('abcdefghijklmnopqrstuvwxyz'))
 for j in Setstr:
    if 'at' in j:
        print(j)
if  __name__ == '__main__':
 randomnumble()
 randomstr()



