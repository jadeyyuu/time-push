# # -*- coding: utf-8 -*-
import http.client, urllib
import json      #引入json库
# conn = http.client.HTTPSConnection('api.tianapi.com')  #接口域名
# params = urllib.parse.urlencode({'key':'07f3ff462d23e459ab1fb28288cdf221'})
# headers = {'Content-type':'application/x-www-form-urlencoded'}
# conn.request('POST','/caihongpi/index',params,headers)
# res = conn.getresponse()
# data = res.read()
# data = json.loads(data)  #转换成字典
# # data=data.get("result", "未找到值")[0]
# # data=data.get("content","未找到值")
# print (data)
# print(data['newslist'][0]['content'])
conn = http.client.HTTPSConnection('api.tianapi.com')  # 接口域名
params = urllib.parse.urlencode({'key': '07f3ff462d23e459ab1fb28288cdf221', 'city': '101020100', 'type':'1'})
headers = {'Content-type': 'application/x-www-form-urlencoded'}
conn.request('POST', '/tianqi/index', params, headers)
res = conn.getresponse()
data = res.read()
data = json.loads(data)
# pop = data["newslist"][0]["content"]
tips = data["newslist"][0]["tips"]
# print(pop)
print(tips)

