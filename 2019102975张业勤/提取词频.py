import numpy as np
import pandas as pd
import jieba
from collections import Counter

datelist = ['01_23','05_18']
wordlist = ''
for i in range(len(datelist)):
#     filename = datelist[i]
    data = pd.read_csv(datelist[i]+'_11.csv',encoding="gbk").iloc[:,1:]
    df=pd.DataFrame(data)
    a=df["热搜标题"].tolist()
    b=','.join([str(i) for i in a])
    wordlist+=b
# wordlist

cut_words = ""
temp = jieba.cut_for_search(wordlist)
cut_words += (" ".join(temp))
all_words=cut_words.split()
while ',' in all_words:
    all_words.remove(',')#replace不好使
counter = Counter(all_words)
dictionary=dict(counter)
df = pd.DataFrame.from_dict(dictionary, orient='index',columns=['词频'])
df = df.reset_index().rename(columns = {'index':'热搜词'})
dff = df.sort_values(by="词频" , ascending=False)
dff
