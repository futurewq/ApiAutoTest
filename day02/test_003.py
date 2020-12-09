'''
测试前置后后置
'''


# 类级别和方法
class Test001:
    def setup_class(self):
        print("测试前置：class级别，类开始执行一次")

    def teardown_class(self):
        print("测试后置：class级别，类结束后执行一次")

    def setup_method(self):
        print("测试前置：functio级别")

    def teardown_method(self):
        print("测试后置：function级别")

    def test_001(self):
        print("测试脚本1")

    def test_002(self):
        print("测试脚本2")

    def test_003(self):
        print("测试脚本3")
