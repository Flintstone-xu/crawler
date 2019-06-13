from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

# if has Chinese, apply decode()
html = urlopen("https://morvanzhou.github.io/static/scraping/table.html").read().decode('utf-8')
print(html)

soup=BeautifulSoup(html,features='lxml')
#任务：匹配jpg文件
jpg=soup.find_all('img',{'src':re.compile('.*?jpg')})
for j in jpg:
	print('\n jpg list blow :\n',j['src'])
