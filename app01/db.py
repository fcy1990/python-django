# -*- coding:utf-8 -*-

import pymysql

class DBConnect():

    def Connect(self):
        conn=pymysql.connect(host='127.0.0.1',port=3307,user='root',passwd='123456',db='test')
        #返回字典
        # cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        # conn.commit()
        # if fetchone is True:
        #     data = cursor.fetchone()
        # else:
        #     data = cursor.fetchall()
        return conn
        # cursor.close()
        # conn.close()
        # return data

    def Fetchone(self,sql):
        conn = self.Connect()
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute(sql)
        data = cursor.fetchone()
        return data

    def Fetchall(self,sql):
        conn = self.Connect()
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute(sql)
        data = cursor.fetchall()
        return data

    def Add(self,sql):
        conn = self.Connect()
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute(sql)
        conn.commit()

    def Edit(self,sql):
        conn = self.Connect()
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute(sql)
        conn.commit()

    def Del(self,sql):
        conn = self.Connect()
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute(sql)
        conn.commit()

    def CloseDB(self):
        cursor,conn = self.Connect()
        cursor.close()
        conn.close()

if __name__ == '__main__':
    db=DBConnect()
    sql = 'select * from t_books where bno=1'
    data = db.Fetchall(sql)
    print(data)