from urllib.request import urlopen
import re
# if has Chinese, apply decode()
html = urlopen(
    #'https://www.baidu.com/'
    "https://morvanzhou.github.io/static/scraping/basic-structure.html"
).read().decode('utf-8')
print(html)

res=re.findall(r'<title>(.+?)</title>',html)
print('\nPage title is:',res[0])

res1=re.findall(r'<p>(.+?)</p>',html,flags=re.DOTALL)
print('\nPage paragraph is ',res1[0])



res2=re.findall(r'href="(.*?)"',html)
print('\nAll links :',res2)


res3=re.findall(r'<h1>(.*?)</h1>',html)
print('\nPage h1 is: ',res3[0])