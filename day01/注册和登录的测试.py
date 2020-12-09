'''
注册
'''

import requests

# 注册的接口
# 验证用户使用正确的手机号、6位长度的密码、注册名为空时，注册成功
url = "http://192.168.150.54:8089/futureloan/mvc/api/member/register"
user = {
    "Mobilephone": "18610750326",
    "pwd": "123456"
}
r= requests.post(url,data=user)
print(r.json())
# assert r.json()['status'] == 0
# 验证用户使用正确的手机号、18位长度的密码、注册名为空时，注册成功
l=[{"Mobilephone":'18610750326',"pwd":'123456789123456789'},
    {"Mobilephone":'13454785815',"pwd":'123456',"regname":'曹贼'},
    {"Mobilephone":'13156782375',"pwd":'123456789123456789',"regname":'曹贼'},
    {"pwd":'1234567'},#失败
    {"pwd":'1234567',"regname":'闪电'},
    {"Mobilephone":'1357189655',"pwd":'1234567'},
   {"Mobilephone":'135718965523',"pwd":'1234567',"regname":'曹贼'},
   {"Mobilephone":'@1234567890',"pwd":'1234567',"regname":'曹贼'},
   {"Mobilephone":'23571896552',"pwd":'1234567',"regname":'遭贼'},
   {"Mobilephone":'13567890987',"pwd":'12345',"regname":'诸葛村夫'},
   {"Mobilephone":'13567890987',"pwd":'1234567890123456789',"regname":'闪电'},
   {"Mobilephone":'13567890987',"regname":'闪电'},
   {"Mobilephone":'18610750327',"pwd":'123456789',"regname":'闪电'},
]
i=0
while i<=12:
    r = requests.post(url, data=l[i])
    # assert r.json()['msg']==l[i][1]
    print(r.json()["msg"])
    print("user%d"%i)
    print(r.json())
    i =i+1
# 登录
url1 = "http://192.168.150.54:8089/futureloan/mvc/api/member/login"
ll=[{"Mobilephone":'18610750327',"pwd":'1234567'},
    {"Mobilephone":'13567890987',"pwd":'1234567890123456789'},
    {"pwd":'123456789'},
    {"Mobilephone":'1356789098',"pwd":'123456789'},
    {"Mobilephone":'135678909821',"pwd":'123456789'},
    {"Mobilephone":'13567890981',"pwd":'123456789'},
    {"Mobilephone":'13567890981'},
    {"Mobilephone":'13567890981',"pwd":'12345'},
    {"Mobilephone":'13567890981',"pwd":'1234567890123456789'}
]
n=0
while n<=8:
    r = requests.post(url1, data=ll[n])
    # assert r.json()['msg']==l[i][1]
    print(r.json()["msg"])
    print("userlogin%d"%n)
    print(r.json())
    n =n+1

