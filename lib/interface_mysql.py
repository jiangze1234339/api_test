import pymysql
import sys
sys.path.append('..')
# from config.config import *
from config.config import *


class Mysql(object):
    def __init__(self):
        self.conn = pymysql.connect(
            host=db_host,
            port=3306,
            user=db_user,
            password=db_password,
            db=db,
            charset='utf8'
        )
        self.cur = self.conn.cursor()

    def __dir__(self):
        self.cur.close()
        self.conn.close()

    def exec(self, sql):
        try:
            self.cur.execute(sql)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            print(str(e))

    def add(self, name, password):
        self.exec("insert into user(name,password)values('{}','{}')".format(name, password))

    def delete(self, name):
        self.exec("delete from user where name='{}'".format(name))

    def select(self, name):
        self.cur.execute("select *from user where name='{}'".format(name))
        result = self.cur.fetchall()
        return result

    def select_all(self, sql):
        self.cur.execute(sql)
        result = self.cur.fetchall()
        return result

    # def change(self, price, name):
    #     self.exec("update user set salary = '{}' where name='{}'".format(price, name))

    def check_user(self, name):
        result = self.cur.execute("select *from user where name='{}'".format(name))
        return True if result else False


m = Mysql()
# m.add('jiangzhe222',25,8000)
print(m.select('张三'))
