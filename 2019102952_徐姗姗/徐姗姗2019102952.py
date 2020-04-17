import numpy as np
import tensorflow as tf
import random

num = set()
for i in range(1000):
    a = np.random.rand() * 100
    num.add(a)

for temp_num in num:
    if temp_num >= 20 and temp_num <= 50:
        #         pass
        print(temp_num)

str=set()
for i in range(1000):
    len=np.random.randint(2,10)
    alphabet='abcdefghijklmnopqrstuvwxyz'
    temp_str=" "
    for j in range(len):
        temp_str+=random.choice(alphabet)
    str.add(temp_str)

for i in str:
    if "at" in i:
        print(i)