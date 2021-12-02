#!/usr/bin/python3
# -*- coding: UTF-8 -*-    
# Author:liweixin
# FileName:mysql_demo
# DateTime:2021/12/2 15:41
# SoftWare: PyCharm
from pymysql import cursors, connect

# 连接数据库
conn = connect(host='10.197.236.190',
               user='root',
               password='123456',
               db='test',
               charset='utf8mb4',
               cursorclass=cursors.DictCursor,
               port=3306)
try:
    with conn.cursor() as cursor:
        # 创建嘉宾列表数据
        sql = 'insert into myapp_guest (realname, phone, email, sign, create_time, event_id) ' \
              'VALUES ("tom",18811112222, "tom@mail.com", 0, NOW(),2);'
        cursor.execute(sql)
        conn.commit()

    with conn.cursor() as cursor:
        sql1 = "select * from myapp_guest where phone=%s"
        cursor.execute(sql1, ('18811112222',))
        result = cursor.fetchone()
        print(result)
finally:
    conn.close()

