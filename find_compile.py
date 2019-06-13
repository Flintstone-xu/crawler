import os
import codecs
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

#r =requests.get ('http://movie.douban.com/top250/')
html = urlopen('http://movie.douban.com/top250/')
soup=BeautifulSoup(html,features='lxml')
for link in soup.find_all('a'):#注意，find——all返回的是一个列表
	print(link.get('href'))
	#url=link.get('href')
for link in soup.find_all(re.compile('a')):
	print(link.get('href'))


#url通过查找find(compile('href'))与find('href')来查看差别