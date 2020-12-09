'''
测试前置和后置
测试前置：测试环境的初始化、测试脚本执行前的准备
测试后置：环境的清理。
'''


# 模块级与函数级配合使用
# 模块级：前置在模块开始执行一次，后置在模结束后执行一次
# 函数级：前置在每个函数开始前置性一次，后置在每个函数结束后执行一次
def setup_module():  # 名字不能写错
    print("测试前置：module级别的")


def teardown_module():  # 名字不能写错
    print("测试后置：module级别的")


def setup_function():  # 名字不能写错
    print("测试前置：function级别的")


def teardown_function():  # 名字不能写错
    print("测试后置：function级别的")


def test_001():
    print("测试脚本1")


def test_002():
    print("测试脚本2")


def test_003():
    print("测试脚本3")
