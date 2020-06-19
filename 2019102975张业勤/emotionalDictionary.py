# 调用要使用的包
from datetime import datetime,timedelta
import re
from openpyxl import Workbook
import requests

workbook = Workbook()
url = 'https://www.enlightent.cn/research/rank/weiboSearchRank#'
headers = {'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0',
        "Cookie":"JSESSIONID=4749CA5CE3B5F60A1449098ED51F43FC; Hm_lvt_030f908df5513cb0a704c88c5da2bc37=1590025832,1590045092; Hm_lpvt_030f908df5513cb0a704c88c5da2bc37=1590046754",
        "Connection":"close"}
proxies = {
    "http": "220.249.149.107"
    }

#获取要爬取的日期列表
def gen_dates(b_date, days):
    day = timedelta(days=1)
    for i in range(days):
        yield b_date + day*i
def get_date_list():
    """
    获取日期列表
    :param start: 开始日期
    :param end: 结束日期
    :return:
    """
    start = datetime.strptime("2019-12-31", "%Y-%m-%d").date()
    #.date()可以只截取日期
    end = datetime.now().date()
    datelist = []
    for d in gen_dates(start, (end-start).days):
        datelist.append(d)
    return datelist

#获取数据的文字部分（热搜词条）
def GetMiddleStr(content,startStr,endStr):
    patternStr = r'%s(.+?)%s'%(startStr,endStr)
    p = re.compile(patternStr,re.IGNORECASE)
    m= re.match(p,content)
    if m:
        return m.group(1)

#导出数据到excel
def export(result_list):
    excel = open('2019-12-31.csv', 'w', encoding='gbk')
    for a in result_list:
        # excel.write(a.replace(u'\xa0', u' '))
        excel.write('\n')
    excel.close()

#两个循环，外层是日期，内层是热搜
i = 0
j = 0
#存储结果的列表
final_list = []

while i<len(get_date_list()):
    date_str = str(get_date_list()[i].year)+'/'+str(get_date_list()[i].month)+'/'+str(get_date_list()[i].day)
    data = {
        'type': 'realTimeHotSearchList',
        't': '151385084',
        'accessToken': 'HYfcS6EQ3JyJCSxU6P/sQmb5KVLIm4qbIxRCEInE6RIr4TnHJtYG0F2ZOCqIjuWiQkhLjXVPYoQPGUKlpyvVfg==',
        'date': date_str
        }
    r = requests.get(url, proxies=proxies, headers=headers)
    # 发送post请求
    r = requests.post(url, data=data, headers=headers)
    result = r.content.decode('utf-8')
    # print(i)
    #获取到的字符串进行分片，此时result由一长串字符串变成列表
    result = result.split('},{')
    #去除首部两个字符以便后面的正则匹配
    result[0] = result[0].strip('[{')
    j = 0
    while j<len(result):
        final_list.append(GetMiddleStr(result[j], '"keyword":"','","url"'))
        j+=1
    i+=1
export(final_list)
