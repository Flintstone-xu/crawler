##任务：使用request来学习post和get的区别，并且查看cookie和session

import requests
import webbrowser

#get请求
param={'wd':'科比'}#数据结构
request=requests.get('http://www.baidu.com/s',params=param)#传数据
print(request.url)#打印
#webbrowser.open(request.url)#浏览器打开url

#post请求
data={'firstname':'flintstone','lastname':'xu'}
request2=requests.post('http://pythonscraping.com/files/processing.php',data=data)
print(request2.text)
#webbrowser.open(request2.url)#浏览器打开url

#cookies
#数据结构
# payload={'username':'Morvan','password':'password'}
# r=requests.post('http://pythonscraping.com/pages/cookies/welcome.php',data=payload)
# print(r.cookies.get_dict())
# r=requests.get('http://pythonscraping.com/pages/cookies/profile.php',cookies=r.cookies)
# print(r.text)


#session
session=requests.Session()
payload={'username':'Morvan','password':'password'}
r=session.post('http://pythonscraping.com/pages/cookies/welcome.php',data=payload)
print(r.cookies.get_dict())
r=session.get('http://pythonscraping.com/pages/cookies/profile.php')
print(r.text)