import requests
from bs4 import BeautifulSoup
import pandas as pd
url='https://tophub.today/n/mproPpoq6O'
headers={'user-Agent':url}  #自定义headers请求页面
r=requests.get(url,headers=headers)
r.raise_for_status()  #异常捕捉
r.encoding=r.apparent_encoding
#print(r.text)  打印出html页面
soup=BeautifulSoup(r.content,'html.parser')
#获取数据
title=soup.find_all("td",{"class":"al"})
val=soup.find_all("td")
list_title=[]
list_val=[]
index = 1
for val in val[:80]:
    if index==1  or index==2 or index==3:
        str = val.get_text()
        if index==3:
            str = str.replace("万热度","")
        list_val.append(str)
    if index == 4:
        list_title.append(list_val)
        list_val=[]
        index = 0
    index+=1
#保存数据到csv文件
df=pd.DataFrame(list_title,columns=['排名','标题','热度(万)'])
#print(df)
filename="知乎今日热榜"
df.to_csv('D:\\zhihu\\aaa.csv',encoding="utf-8")
