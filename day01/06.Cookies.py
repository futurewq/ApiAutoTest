'''
Coolie:
http协议：无状态，无连接，媒体独立。
每个请求都是独立的。有些接口登录后才能访问，需要使用Cookies验证用户是否登录。
account/dashboard 用户没有登录时，返回登录的页面。
account/dashboard 如果登录了，返回用户的详细信息。浏览器登录后，获取到的cookies直接放到自动化来用。
如果cookies失效或者换其他用户登录，就不能继续访问了。
'''
import requests

# 百格网站，有一些接口登录之后才能访问
print("未登录时，返回结果为")
url = "https://www.bagevent.com/account/dashboard"
r = requests.get(url)
print(r.text)

# 用Fiddler抓到的包，将里面的头设置到这里
head = {
    "Cookie": '__auc=8fcf353117627635b3be51dcacc; _ga=GA1.2.910905789.1606978592; __asc=67237be21762cbcd2ebf5f00872; Hm_lvt_1fc37bec18db735c69ebe77d923b3ab9=1606978591,1607068341; MEIQIA_TRACK_ID=1lBR90Nju2U2zIH25hAYnBV81bn; MEIQIA_VISIT_ID=1lBR93AMkUKcobTEgz60qgL50IX; _gid=GA1.2.277978482.1607068345; BAGSESSIONID=feaa63ab-66bd-4c1c-a9a3-505108dc483b; JSESSIONID=4FE9320CE945DA1BC377DE3E373F4891; Hm_lpvt_1fc37bec18db735c69ebe77d923b3ab9=1607069164'
}
print("登录后，返回的结果为：")
r = requests.get(url, headers=head)
print(r.text)
