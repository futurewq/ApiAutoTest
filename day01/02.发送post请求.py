'''
发送post请求
'''

import requests

# 登录的接口：
url = "http://192.168.150.54:8089/futureloan/mvc/api/member/login"
user = {
    "mobilephone": "18610750327",
    "pwd": "1234567"
}
# data传表单参数,content-type:appliction/x-www-form-urlencoded
r = requests.post(url, data=user)
print(r.text)

#
url = "http://www.httpbin.org/post"
user = {
    "mobilephone": "18610750327",
    "pwd": "1234567"
}
r = requests.post(url, data=user)
print(r.text)
print("*" * 25)  # 分割线
# 用json传参数，数据类型为contrnt-type:application/json
r = requests.post(url, json=user)
print(r.text)
print("&" * 50)

# 练习：充值接口，给注册的用户充值
url = "http://192.168.150.54:8089/futureloan/mvc/api/member/recharge"
user = {
    "mobilephone": "18610750327",
    "amount": 300000.00
}
r = requests.post(url, data=user)
# r =requests.post(url,json=user)


print(r.text)
r=r.json()
assert r['status'] == 1
assert r['code'] == '10001'
assert r['msg'] =="充值成功"
assert r['data']['id']==1146