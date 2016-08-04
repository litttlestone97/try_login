#-*-coding:utf8-*-
'''
功能描述：
+ 抓取知乎主话题,单页

编写日期：20160702
编写人：little_Stone
'''

import requests
import math
from openpyxl import load_workbook
from openpyxl import Workbook 
import re      #正则表达式的库

#hea是我们自己构造的一个字典，里面保存了user-agent
header = {'X-Requested-With': 'XMLHttpRequest',
           'Referer': 'https://www.zhihu.com/topic/20052088/followers',
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; '
                         'Trident/7.0; Touch; LCJB; rv:11.0)'
                         ' like Gecko',
           'Host': 'https://www.zhihu.com/topic/20052088/followers'}

html = requests.get('https://www.zhihu.com/topic/20052088/followers',headers = header)
#print (html.text)
#写入文档
fp = open('try.txt','w',encoding='utf-8')
fp.write(html.text)
fp.close()

