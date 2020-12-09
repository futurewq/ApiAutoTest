'''
登录接口测试
'''

import pytest
from ZongHe.caw import DataRead
from ZongHe.baw import Member, DbOp

# 读取yaml数据
@pytest.fixture(params=DataRead.read_yaml(r"data_case\login_setup.yaml"),scope='module')
def setup_data(request):
    return request.param

@pytest.fixture(params=DataRead.read_yaml(r"data_case\login_data.yaml"))
def login_data(request):
    return request.param

@pytest.fixture(scope='module')
def register(url, baserequests, setup_data,db):
    print(f"测试数据：{setup_data}")
    #注册用户
    mobile = setup_data['casedata']['mobilephone']
    t =Member.register(url, baserequests, setup_data['casedata'])
    yield
    #删除注册用户
    DbOp.delete_user(db,mobile)
def test_login(register,login_data,url,baserequests):
    # 下发登录的请求
    r= Member.login(url,baserequests,login_data['casedata'])
    print("------------",r.json())
    # 检查结果
    assert r.json()['msg'] ==login_data['expect']['msg']



