
class TestQuery:
    def test_001(self):
        print("查询：用例1")
    def test_002(self,login): #这里执行前置
        print("查询：用例2")
    def test_003(self):
        print("查询：用例3")
    def test_004(self):#这里执行后置
        print("查询：用例4")