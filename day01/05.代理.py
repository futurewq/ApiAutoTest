'''
设置代理
1.如果想抓包分析自动化发出去的报文，可以通过设置代理抓包
2.用一台电脑频繁访问某个网站，被网站认为是攻击，将Ip地址禁用了，设置代理，换一个Ip地址去访问。
'''

import requests
# proxy = {
#     "http": "http://127.0.0.1:8888",  # http协议，使用xxx代理
#     "https": "http://127.0.0.1:8888"  # https协议，使用xxx代理
# }
proxy = {
    "http": None,  # http协议，使用xxx代理
    "https": None  # https协议，使用xxx代理
}
url = "http://192.168.150.54:8089/futureloan/mvc/api/member/list"
r = requests.get(url,proxies=proxy)  # 给需要抓包的接口，设置代理
print(r.json())

url = "http://192.168.150.54:8089/futureloan/mvc/api/member/login?mobilephone=18610750327&pwd=1234567"
r = requests.get(url)
print(r.json())
