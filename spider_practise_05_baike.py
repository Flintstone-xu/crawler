from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import random

##任务：爬取百度百科

#爬虫的目标网址
base_url = "https://baike.baidu.com"
#his为存放地址的历史数组
his=['/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB/5162711']
for i in range(20):
	url=base_url+his[-1]
	html = urlopen(url).read().decode('utf-8')
	soup = BeautifulSoup(html, features='lxml')
	print(i,soup.find('h1').get_text(),'	url:',his[-1])

	#查找所有的href，随机选取其中一个，然后爬取，如果没有，返回上一个网页爬取
	sub_url=soup.find_all('a',{'target':'_blank','href':re.compile('/item/(%.{2})+$')})
	if len(sub_url) != 0:
		his.append(random.sample(sub_url,1)[0]['href'])#随机选取其中一个，放入his历史列表中
	else:
		his.pop()
	print(his)