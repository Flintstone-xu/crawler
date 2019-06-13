##查看html结构
from bs4 import BeautifulSoup
soup=BeautifulSoup('<p>中文</p>','html.parser')
soup.prettify()
print(soup.prettify())

##提取html中所有url链接
soup=BeautifulSoup.(demo,lxml)
for link in soup.find_all('a'):#注意，find——all返回的是一个列表
	pint(link.get('href'))
	url=link.get('href')

