# 無法編程 教學網站已無法 編寫新網站更新內容
import urllib.request as req

url= "https://medium.com/_/api/home-feed"
#建立一個request 物件，附加Request Headers
request=req.Request(url,headers={
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"    
})
with req.urlopen(request) as response:

    data=response.read().decode('utf-8')



#解析原始碼. 取得每篇文章的標題
import json
data=data.replace("])}while(1);</x>","")
data=json.loads(data)
#print(data)

posts=data["payload"]["references"]["Post"]
for key in posts:
    post=posts[key]
    print(post["title"])