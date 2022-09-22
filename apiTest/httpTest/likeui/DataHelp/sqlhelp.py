# coding:utf-8
from pymysql import cursors, connect
from httpTest.likeui.conftest import MYSQL_HOST, MYSQL_User, MYSQL_PWD, MYSQL_DB

#pymysql菜鸟教程

def getSqlData(sql, *values):
    """根据sql获取数据"""
    with connect(host=MYSQL_HOST,
                 user=MYSQL_User,
                 password=MYSQL_PWD,
                 db=MYSQL_DB) as db:
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # 使用execute方法执行SQL语句
        cursor.execute(sql, args=values)
        # 使用 fetchone() 方法获取一条数据
        data = cursor.fetchall()

        return data
