 #encoding=utf-8
from bs4 import BeautifulSoup
import re
import requests
import os
import urllib.request

##目的：爬取虎扑论坛上杜兰特crossover的GIF
##步骤：1，解析HTML，2，找链接，3，下载

URL='https://bbs.hupu.com/18310437.html'
html=requests.get(URL).text
soup=BeautifulSoup(html,'lxml')
os.makedirs('./杜兰特crossover',exist_ok=True)
gif_table=soup.find('table',attrs={'class':'case'})
#print (gif_table)
#/table/div/a{href}
#gif_divs=gif_table.find_all('div')
#print(gif_divs)
'''找出table标签，然后分析里面的img，最后得到data-url，
	通过url，
'''
gif_url =gif_table.find_all('img',{"class":"img-gif"})
#print(gif_url)
for gifs in gif_url:
	data_url=gifs['data-url']
	print (data_url)
	gif_source=data_url.split('?')[0]
	print (gif_source)
	r=requests.get(data_url,stream=True) 
	gif_name=gif_source.split('/')[-1]
	urllib.request.urlretrieve(data_url,gif_name) 
	#with open('./杜兰特crossover/%s' % gif_name,'wb') as f:
	# 	for chunk in r.iter_content(chunk_size=128):
	# 		f.write(chunk)
	# 	print('saved as %s:'% gif_name)
		

		#尝试不使用chunk后，依然没有保存到gif的动图，应该和chunk无关，f.write（）这个方法有关吗？
		#f.write(r.img_data)
	print('saved as %s'% gif_name)


