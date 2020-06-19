import numpy as np
import pandas as pd
from sklearn.manifold import MDS
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

data = pd.read_csv("globalHotCalendar.csv",encoding="UTF-8")
data = data.where(data.notnull(), 0)
data1 = data.T
df=pd.DataFrame(data1)
rowdata=df.iloc[1:,1:]
rowdata
mds = MDS(n_components=1,random_state=488).fit_transform(rowdata)
# X_tsne = TSNE(n_components=1,perplexity=30).fit_transform(rowdata)
#df["1d"] =mds[:,0]
rowdata["1d"] =mds[:,0]
estimator = KMeans(n_clusters=5)#构造聚类器
estimator.fit(rowdata)#聚类
label_pred = estimator.labels_ #获取聚类标签
#df["label"] =label_pred
rowdata["label"] =label_pred
df

#b=df.sort_values(by="1d" , ascending=False)
b=rowdata.sort_values(by="1d" , ascending=False)
b

rowdata
mds = MDS(n_components=2,random_state=506).fit_transform(rowdata)
# X_tsne = TSNE(n_components=1,perplexity=30).fit_transform(rowdata)
#df["x"] =mds[:,0]
#df["y"] =mds[:,1]
rowdata["x"] =mds[:,0]
rowdata["y"] =mds[:,1]
rowdata

b.to_csv("global_dailyAddSort1d_5.csv",encoding="gbk")
