'''
自动管理cookies
通过requests.session自动管理cookies
'''
import requests

# 登录百格
s = requests.session()
url = "https://www.bagevent.com/user/login"
user = {
    "access_type": "1",
    "loginType": "1",
    "emailLoginWay": "0",
    "account": "2780487875@qq.com",
    "password": "qq2780487875",
    "remindmeBox": "on",
    "remindme": "1"
}
r = s.post(url, data=user)
print(r.text)
print("=="*20)
# 获取账户信息
url = "https://www.bagevent.com/account/dashboard"
r = s.get(url)
print(r.text)
assert "<title>百格活动 - 账户总览</title>"
print("##"*20)
# 退出登录
url = "https://www.bagevent.com/user/login_out"
r = s.get(url)
# print(r.text)
print("========退出登录后的cookies",s.cookies)
