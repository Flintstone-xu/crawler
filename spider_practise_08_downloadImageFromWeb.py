from bs4 import BeautifulSoup
import requests
import os
#地址
URL = "http://www.nationalgeographic.com.cn/animals/"

html = requests.get(URL).text
soup = BeautifulSoup(html, 'lxml')
img_ul = soup.find_all('ul', {"class": "img_list"})
os.makedirs('./img_nationalGeographic',exist_ok=True)
for ul in img_ul:
	imags=ul.find_all('img')
	for img in imags:
		url=img['src']
		#使用chunk下载
		r=requests.get(url,stream=True)
		imag_name=url.split('/')[-1]#取出用‘/’分隔的最后一个项，用以给image命名
		with open('./img_nationalGeographic/%s' % imag_name,'wb') as f:
			for chunk in r.iter_content(chunk_size=128):
				f.write(chunk)
		print('Saved as %s'% imag_name)
