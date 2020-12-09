'''
注册接口
'''

import pytest
import requests

url = "http://192.168.150.54:8089/futureloan/mvc/api/member/register"


@pytest.fixture(params=[{"data":{"Mobilephone": '18610210310', "pwd": '123456789123456789'},"msg":'手机号码已被注册'},
                        {"data":{"Mobilephone": '13454785815', "pwd": '123456', "regname": '曹贼'},'msg':'手机号码已被注册'},
                        {"data":{"Mobilephone": '13156782375', "pwd": '123456789123456789', "regname": '曹贼'},'msg':'手机号码已被注册'},
                        {"data":{"pwd": '1234567'},'msg':'手机号不能为空'},  # 失败
                        {"data":{"pwd": '1234567', "regname": '闪电'},'msg':'手机号不能为空'},
                        {"data":{"Mobilephone": '1357189655', "pwd": '1234567'},'msg':'手机号码格式不正确'},
                        {"data":{"Mobilephone": '135718965523', "pwd": '1234567}', "regname": '曹贼'},'msg':'手机号码格式不正确'},
                        {"data":{"Mobilephone": '@1234567890', "pwd": '1234567', "regname": '曹贼'},'msg':'手机号码格式不正确'},
                        {"data":{"Mobilephone": '23571896552', "pwd": '1234567', "regname": '遭贼'},'msg':'手机号码格式不正确'},
                        {"data":{"Mobilephone": '13567890987', "pwd": '12345', "regname": '诸葛村夫'},'msg':'密码长度必须为6~18'},
                        {"data":{"Mobilephone": '13567890987', "pwd": '1234567890123456789', "regname": '闪电'},'msg':'密码长度必须为6~18'},
                        {"data":{"Mobilephone": '13567890987', "regname": '闪电'},'msg':'密码不能为空'},
                        {"data":{"Mobilephone": '18610750327', "pwd": '123456789', "regname": '闪电'},'msg':'手机号码已被注册'}
                        ])
def regist_data(request):
    return request.param


def test_regist(regist_data):
    print(f"测试：",regist_data['data'])
    # print(f"结果",regist_data['msg'])
    r = requests.post(url, params=regist_data['data'])
    assert r.json()['msg']==regist_data['msg']
    print(r.json())
