from bs4 import BeautifulSoup
from urllib.request import urlopen

# if has Chinese, apply decode()
html = urlopen("https://morvanzhou.github.io/static/scraping/list.html").read().decode('utf-8')
print(html)
#任务1：找在li模块中，以class=‘mouth’的对象
soup=BeautifulSoup(html,features='lxml')
mouth=soup.find_all('li',{'class':'month'})
for m in mouth:
	print('\n------\n',m.get_text())

#任务2：找在ur模块中，以class=‘jan’的对象
jan=soup.find_all('ul',{'class':'jan'})
Feb=soup.find_all('li',{'class':'feb month'})
for j in jan:
	print('\nabove all are the projects which class：jan\n',j.get_text())
for F in Feb:
	print('\nabove all are the projects which class：feb month\n',F.get_text())

