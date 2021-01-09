'''
监控服务器的cpu、内存、磁盘、网络
'''
from time import sleep
from datetime import datetime

import psutil

print(psutil.cpu_percent())  # cpu
print(psutil.virtual_memory())  # 内存
print(psutil.virtual_memory().percent)  # 内存百分比
print(psutil.disk_usage("d:/"))  # 监控磁盘
print(psutil.disk_usage("d:/").percent)  # 监控磁盘的百分比
print(psutil.net_io_counters())  # 网络IO
print(psutil.net_io_counters().bytes_sent)  # 发送的字节数
print(psutil.net_io_counters().bytes_recv)  # 接收的字节数

# 死循环，每隔3秒获取数据，把数据写到文件里面
# 首行： 时间 CPU百分比 内存百分比 磁盘百分比 发送字节数 接收字节数


with open("监控.txt", 'a', encoding='utf-8') as file:
    file.write("时间\tCPU百分比\t内存百分比\t磁盘百分比\t发送字节数\t接收字节数\n")
    i = 3
    while i == 3:
        ticks = datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S")
        file.write("%s\t%s\t%s\t%s\t%s\t%s\n" % (
        ticks, psutil.cpu_percent(), psutil.virtual_memory(), psutil.disk_usage("d:/").percent,
        psutil.net_io_counters().bytes_sent, psutil.net_io_counters().bytes_recv))
        file.flush()
        sleep(i)
