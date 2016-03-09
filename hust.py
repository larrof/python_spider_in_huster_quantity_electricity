import urllib.request
from bs4 import BeautifulSoup
import urllib.error



#请求的链接
url = "http://202.114.18.218/main.aspx"

#请求的头信息
head = {}
head['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36'

#请求所带的数据:

data = {}
data['programId']='东区'
data['txtyq']='沁苑东十舍'
data['txtld']='1层'
data['Txtroom']='120'
data['ImageButton1.x']='56'
data['ImageButton1.y']='13'

data['TextBox2']='2016-3-6 7:08:35'
data['TextBox3']='8.7'

data['__EVENTVALIDATION']='/wEWKgKcy5/7BALorceeCQLc1sToBgL+zqXMDgK50MfoBgKhi6GaBQLdnbOlBgLtuMzrDQLrwqHzBQKX+9a3BALahOrMBwLahO6ZAQLahOLMBwLahMqFAQLahJKFAQLahKrHBwLahI6ZAQLahP6FAQKsioTXAwL4w577DwKH0cqFAQKVre6ZAQKVrZKFAQKVrf6FAQK/yONFArDhhMwNArvghMwNAr/I87wGAqTghMwNApSUsNoIAoOU+OMOAoKU+OMOAoGU+OMOAoCU+OMOAoeU+OMOAoaU+OMOAo+UvJ4CAvrV2qsGAtLCmdMIAtLC1eQCAuzR9tkMAuzRirUFOLHrHczOAnP0f8H0iOrdziJ/rT8='

data['__VIEWSTATE']='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'

	#数据解析
data = urllib.parse.urlencode(data).encode('utf-8')

#生成请求
req = urllib.request.Request(url,data,head)


#获取并解析请求得到的回复
try:
    response = urllib.request.urlopen(req)
        #对回复读取并解码
except urllib.error.URLError as e:
    print(e.reason)

else:

    html = response.read().decode('utf-8')

        #print(html)

        #通过BeautifulSoup来解析html
    soup =BeautifulSoup(html,"html.parser")

    rest2 = soup.findAll('table',attrs={"rules" : "all"})
    r = rest2[0].findAll('td')
    for e in r:
        print(e.string)

