'''
使用request 发送get请求
'''

import requests  # 导入包

# 发送一个get请求，返回一个响应，将响应存到变量r中
r = requests.get("http://www.baidu.com")
print(r.text)

# list 获取用户列表。http://192.168.150.54:8089/
url = "http://192.168.150.54:8089/futureloan/mvc/api/member/list"
r = requests.get(url)  # 发送请求
print(r.json())
r = r.json()
assert r['status'] == 1  # 对结果进行检查
assert r['code'] == '10001'
assert r['msg'] == '获取用户列表成功'

# get请求带参数，拼接到url后面，？参数名1=参数值1&参数名2=参数值2
# 注册接口
url1 = "http://192.168.150.54:8089/futureloan/mvc/api/member/register?mobilephone=18610750327&pwd=1234567&regname=futurewq"
r = requests.get(url1)  # 发送请求
r = r.json()
print(r)
assert r['status'] == 0  # 对结果进行检查
assert r['code'] == '20110'
assert r['msg'] == '手机号码已被注册'

# get请求带参数，方式2：使用params参数
url = "http://192.168.150.54:8089/futureloan/mvc/api/member/register"
user = {
    "mobilephone": "18610750327",
    "pwd": "1234567",
    "regname": "wq"
}
r = requests.get(url, params=user)
r = r.json()
print(r)
assert r['status'] == 0  # 对结果进行检查
assert r['code'] == '20110'
assert r['msg'] == '手机号码已被注册'

# 练习
# 接口功能：查询手机号码归属地
# 接口地址：https://tcc.taobao.com/cc/jison/mobile_tel_segment.htm
# 方法：get
# 参数名：tel
# 参数值：手机号
url = "https://tcc.taobao.com/cc/json/mobile_tel_segment.htm"
tel = {"tel": "13571896552"}
r = requests.get(url, params=tel)
print(r.text)
print(type(r))
print(r.status_code)  # 状态码
print(r.reason)  # 状态信息
print(r.cookies)  # cookies
print(r.encoding)  # 编码方式
print(r.headers)  # 响应头

# 发送请求时，带请求头
# 有些网站，对自动化发出的请求不处理或者处理结果与实际结果不一致。
# 通过设置请求头，伪装成浏览器发的请求。
# httpbin是一个测试网站，发送的请求，这个网站将请求转成json格式的返回。
url = "http://www.httpbin.org/get?user=root&pwd=123213"
r = requests.get(url)
print(r.text)
# 使用request发送的请求，“User-Agent"为”python-requests/2.18.4“
# 设置请求头
head ={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
}
r=requests.get(url,headers=head)
print(r.text)
