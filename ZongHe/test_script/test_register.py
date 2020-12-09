'''
注册的脚本
'''
import pytest

from ZongHe.baw import Member, DbOp
from ZongHe.caw import DataRead
from ZongHe.caw import Mysql
# 测试数据
from ZongHe.test_script.conftest import baserequests


@pytest.fixture(params=DataRead.read_yaml(r"data_case\register_fail.yaml"))
def fail_data(request):  # 固定写法，参数必须是request，获取params中的每一个param
    return request.param

# 测试逻辑
def test_register_fail(fail_data,url,baserequests):
    print(f"测试数据：{fail_data}")
    # 下发注册的请求
    # fixture session级别conftest.py(放置脚本层的公共方法，就是一个测试前置）
    r = Member.register(url,baserequests,fail_data['data'])
    # 校验结果
    assert r.json()['msg'] == fail_data['msg']

# 注册成功
@pytest.fixture(params=DataRead.read_yaml(r"data_case\register_pass.yaml"))
def success_data(request):
    return request.param

def test_register_success(success_data,url,db,baserequests):
    print(f"测试数据:{success_data}")
    # 获取手机号码
    mobile =success_data['data']['mobilephone']
    # 下发注册的请求
    # 检查结果，1.检查结果应与预期结果一致
    DbOp.delete_user(db, mobile)
    r =Member.register(url,baserequests,success_data['data'])
    assert r.json()['msg']==success_data['expect']['msg']
    assert r.json()['code']==success_data['expect']['code']
    # 检查结果，2，检查系统中用户注册成功
    # 查询用户，检查手机号在返回的结果中。
    sql2 = f"select mobilephone from member"
    conn =Mysql.connect(db)
    Mysql.select_user(conn,sql2)
    Mysql.disconnect(conn)
    # 清理环境：删除注册用户
    # 方式1：查询用户，检查手机号在返回的结果中。
    # r = Member.list(url, baserequests)
    # assert mobile in r.text
    # 方式2：从数据库中查询注册用户。
    r = DbOp.select_User(db, mobile)
    print(r)
    assert len(r) == 1
    # # 清理环境：删除注册用户
    # DbOp.delete_user(db, mobile)
