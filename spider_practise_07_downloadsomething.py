
##本次任务是下载图片
import os
import requests
from urllib.request import urlretrieve
os.makedirs('./img/', exist_ok=True)

IMAGE_URL = "https://morvanzhou.github.io/static/img/description/learning_step_flowchart.png"
#urlretrieve download
urlretrieve(IMAGE_URL,'./img/flinstone01.png')#存放地址

#requests download
r=requests.get(IMAGE_URL)
with open('./img/flinstone02.png','wb') as f:
	f.write(r.content)

#chunck download
r1=requests.get(IMAGE_URL,stream=True)#流媒体断点下载
with open('./img/flinstone03.png','wb') as f:
	for chunk in r1.iter_content(chunk_size=32):
		f.write(chunk)