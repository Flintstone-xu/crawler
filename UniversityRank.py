import requests
from bs4 import BeautifulSoup
import bs4
##步骤1：从网页获取大学排名内容
##步骤2：提取内容到特定的数据结构
##步骤3：利用数据结构来展示数据
def getHTMLText(url):
	try:
		r=requests.get(url,timeout=30)
		r.raise_for_status
		r.encoding=r.apparent_encoding
		return r.text
	except :
		return ""

def fillUniList(ulist,html):
	soup=BeautifulSoup(html,'html.parser')
	for tr in soup.find('tbody').children:
		if isinstance(tr,bs4.element.Tag):
			tds=tr('td')
			ulist.append([tds[0].string,tds[1].string,tds[4].string])
def printUniList(ulist,num):
	print('{0:^10}\t{1:^10}\t{2:^10}'.format('排名','学校','评分',chr(12288)))
	for i in range(num):
		u=ulist[i]
		print('{:^10}\t{:^10}\t{:^10}'.format(u[0],u[1],u[2],chr(12288)))

def main():
	uinfo=[]
	url='http://www.zuihaodaxue.cn/zuihaodaxuepaiming2018.html'
	html=getHTMLText(url)
	fillUniList(uinfo,html)
	printUniList(uinfo,10)
main()