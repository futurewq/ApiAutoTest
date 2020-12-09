'''
fixture 作用域，类级别
'''

import pytest

@pytest.fixture(scope='class')
def login():
    print("登录系统")
    yield
    print("退出系统")

class TestQuery:
    def test_001(self):
        print("查询：用例1")
    def test_002(self,login): #这里执行前置
        print("查询：用例2")
    def test_003(self,login):
        print("查询：用例3")
    def test_004(self,login):#这里执行后置
        print("查询：用例4")

class TestAdd:
    def test_001(self,login):#这里执行前置
        print("添加：用例1")
    def test_002(self):
        print("添加：用例2")
    def test_003(self): # 这里执行后置
        print("添加：用例3")
