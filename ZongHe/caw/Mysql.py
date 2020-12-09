'''
数据库的操作
'''

import pymysql

def connect(db):
    '''
    连接数据库
    :param db: 数据库相关的信息，字典格式
    :return: 连接对象
    '''
    host =db['host']
    port =db['port']
    user =db['user']
    pwd  =db['pwd']
    name =db['name']
    try:
        conn = pymysql.connect(host=host,port=port,user=user,
                               password=pwd,database=name,charset='utf8')
        print("数据库连接成功")
        return conn
    except Exception as e:
        print(f"数据库连接失败,异常信息为:{e}")
# 断开连接
def disconnect(conn):
    '''
    断开数据库连接
    :param conn: connect方法返回的连接对象
    :return: 无
    '''
    try:
        conn.close()
    except Exception as e:
        print(f"断开数据库连接失败，异常信息为:{e}")

# 查询用户
def select_user(conn,sql2):
    try:
        c =conn.cursor() #  获取游标
        c.execute(sql2) # 使用游标执行sql语句
        conn.commit()  #  提交
        x =c.fetchall()
        c.close()  # 关闭游标
        print(f"执行查询sql语句成功:{sql2}")
        return list(x)
    except Exception as e:
        print(f"执行查询sql语句失败，异常信息为:{e}")
# 清除数据
def execute(conn,sql):
    '''
    执行sql语句
    :param conn: connect返回的连接对象
    :param sql: 要执行的aql语句
    :return: 无
    '''
    try:
        c =conn.cursor() #  获取游标
        c.execute(sql) # 使用游标执行sql语句
        conn.commit()  #  提交
        c.close()  # 关闭游标
        print(f"执行sql语句成功:{sql}")
    except Exception as e:
        print(f"执行sql语句失败，异常信息为:{e}")

# 测试代码，用完删除
if __name__ == '__main__':
    db ={"host": "jy001", "port": 4406, "name": "future", "user": "root", "pwd": "123456"}
    print("dbdbdbdbdbdbddbdbdbdbdbddbdbdbddbdbdbddb",type(db))
    mobile = "18620740248"
    sql2 = f"select mobilephone from member"
    sql  = f"delete from member where mobilephone={mobile}"
    conn =connect(db)
    a= select_user(conn, sql2)
    print(a)
    execute(conn,sql)
    disconnect(conn)
