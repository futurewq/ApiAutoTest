'''
接口的功能是上传文件，比如上传头像，附件等。
'''

import requests

url = "http://www.httpbin.org/post"
# 将本地的文件上传到服务器
file = "d:/test.txt"
with open(file, 'r', encoding='utf-8') as f:
    # 字典，上传的文件：文件相关参数组成的元组
    # text/plain是文件的类型
    load = {
        'file1': (file, f)  # "text/plain"
    }
    r = requests.post(url, files=load)
    print(r.text)

# 上传图片
file2 = r"D:\workspace\logo.png"
with open(file2, "rb") as f:
    load = {
        # 文件名：file-tuple
        # file-tuple 可以是二元组，三元组，四元组
        # image/png MIME类型，文件类型，application/josn application/...文件类型不是系统默认的，就要写明，我不知道系统默认的类型是啥，所以最好写上。
        'file2': (file2, f, "image/png")
    }
    r = requests.post(url, files=load)
    print(r.text)

# 可以一次上传多个文件，文本和图片一起上传
with open(file, "r", encoding='utf-8') as f1:
    with open(file2, 'rb') as f2:
        load = {
            "file1": (file, f1),
            "file2": (file2, f2, "image/png")
        }
        r = requests.post(url, files=load)
        print(r.text)
