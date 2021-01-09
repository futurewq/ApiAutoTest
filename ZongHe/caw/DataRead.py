'''
文件读写类的操作
'''
import configparser
import os

import yaml


def get_project_path():
    '''
    获取工作路径
    :return: 当前工程路径，比如E:\Lenjava\python\ApiAutoTest\ZongHe
    '''
    # __file__存储着当前文件的路径
    path = os.path.realpath(__file__)
    # 上级目录
    path = os.path.dirname(path)
    # 再上级目录
    path = os.path.dirname(path)
    return path+"\\"

def read_ini(file_path, key):
    '''
    读取ini配置文件
    :param file_path: ini文件路径
    :param key: 要读取的key值
    :return: key值对应的value
    '''
    file_path = get_project_path() + file_path
    config = configparser.ConfigParser()
    config.read(file_path) #读文件
    # 通过key取value，“env”是section,与ini中[env]对应
    value = config.get("env",key)
    return value
def read_yaml(file_path):
    '''
    读取yaml文件
    :param file_path: yaml文件路径
    :return: 文件内容，列表格式的
    '''
    file_path=get_project_path()+file_path
    print(file_path)
    with open(file_path,"r",encoding='utf-8') as f:
        content = yaml.load(f,Loader =yaml.FullLoader)
        return content

# 测试代码，用完可以直接删掉
if __name__ == '__main__':
    # 绝对路径，把代码放到别的电脑上，可能就执行不了了
    # 绝对路径换成相对路径，E:\Lenjava\python\ApiAutoTest\ZongHe 通过代码自动获取
    a =read_ini(r"data_env\env.ini","url")
    print(a)
    b =read_ini(r"data_env\env.ini","db")
    print(b)
    c =read_yaml(r"data_case\register_pass.yaml")
    print(c)
    d =read_yaml(r"data_case\register_fail.yaml")
    print(d)