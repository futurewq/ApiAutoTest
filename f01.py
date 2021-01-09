'''
使用locust进行性能测试
'''
from locust import HttpUser, task, between


# 为什么要展开性能测试的功能创建一个类，从HttpUser继承
class CarRental(HttpUser):
    # 设置思考时间，在1～5秒之间取随机数
    # wait_time是HttpUser中定义的属性，名字不能写错
    # between 是HttpUser中定义的方法
    wait_time = between(1,5)

    @task  # 用task修饰，表示声明了一个任务
    def loadAllMenu(self):
        # HttpUser 中有一个client属性，使用这个属性发送get/post方法
        # 用法跟requests中的get/post一样
        ret =self.client.get("/carRental/desk/toDeskManager.action")
        assert ret.status_code == 200

    @task
    def loadAllNews(self):
        ret =self.client.get("/carRental/news/loadAllNews.action?page=1&limit=10")
        assert ret.status_code ==200

    @task
    def loadAllrent(self):
        ret = self.client.get("/carRental/rent/loadAllRent.action?page=1&limit=10")
        assert ret.status_code ==200
