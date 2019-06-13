#coding:utf-8
#任务目的：抓取淘宝的商品信息（名称和价格）
#步骤：1，获取页面；2，分析页面，3，打印信息

import re
import requests
def getHTML(url):
	try:
		r=requests.get(url,timeout=30)
		r.raise_for_status()
		r.encoding=r.apparent_encoding
		#print(r.text)
		return r.text
	except :
		return "get_url failed\n"
def praseHTML(itemlist,html):
	try:
		plt=re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)
		print(len(plt))
		tlt=re.findall(r'\"raw_title\"\:\".*?\"',html)
		print(len(tlt))
		# for i in range(len(plt)):
		# 	price=eval(plt(i).split(':')[1])#在一些程序语言中，eval 是一个把字符串当作表达式执行而返回一个结果的函数
		# 	print(price)
		# 	title=eval(tlt(i).split(':')[1])
		# 	itemlist.append([price,title])
		# 	print (itemlist)
		for i in range(len(plt)):
			price = eval(plt[i].split(':')[1])
			title = eval(tlt[i].split(':')[1])
			ilt.append([price , title])        	
	except :
		print('praseHTML failed\n')
def printGoods(itemlist):
	print("{:4}\t{:15}\t{:5}\t".format("序号","商品","价格"))
	count=0
	for g in itemlist:
		count=count+1
		print("{:4}\t{:15}\t{:5}\t".format("count","g[1]","g[0]"))
def main():
	goods='篮球'
	pre_url='https://s.taobao.com/search?q='
	infoList=[]
	try:
		url=pre_url+goods
		html=getHTML(url)
		praseHTML(infoList,html)
	except :
		print('main failed')
	printGoods(infoList)
main()