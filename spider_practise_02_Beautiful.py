from bs4 import BeautifulSoup
from urllib.request import urlopen

# if has Chinese, apply decode()
html = urlopen("https://nba.hupu.com/wiki/%E7%A7%91%E6%AF%94-%E5%B8%83%E8%8E%B1%E6%81%A9%E7%89%B9").read().decode('utf-8')
#print(html)

soup=BeautifulSoup(html,features='lxml')
# print('\n----------------------------\n',soup.h1)

# print('\n------------------\n',soup.p)

# print('\n---------------------------\n',soup.body)


all_href=soup.find_all('a')
print('\n----------------------------\n',all_href)
all_href=[l['href'] for l in all_href]
#all_href = [l['href'] for l in all_href]
print('\n11111111111111111111111111111111\n',all_href)

##自我练习

all_link=soup.find_all('link')
print('\n-==========\n',all_link)
all_link=[m['href'] for m in all_link]#用字典的形式href=‘*****’输出href的值
print('\n0000000000000000000000000\n',all_link)