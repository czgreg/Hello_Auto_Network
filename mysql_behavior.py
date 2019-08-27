#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import pymysql

class mysql_behavior():

    def __init__(self,host='host_ip',username='root',password='pwd_***',db='db_name_***',table='table_name_**'):
        self.db = db
        self.table=table
        self.dbaes = pymysql.connect(
            host,
            username,
            password,
            db,
            charset='utf8')
        self.dbcursor = self.dbaes.cursor()
        print('MySQL数据库{}连入成功'.format(self.db))

    def insert(self,ip,log):
        hostname = log[0]
        device = log[1]
        sn = log[2]
        version = log[3]
        patch = log[4]
        print('{}——信息准备录入数据库'.format(ip))
        sql = """ insert into {} values("{}", "{}", "{}",  "{}", "{}","{}") """.format(self.table,hostname,ip,device,sn,version,patch)
        try:
            self.dbcursor.execute(sql)
            self.dbaes.commit()
        except Exception as e:
            self.dbaes.rollback()
            if '(1062' in str(e).split(','):
                print('{}——查询到重复录入，录入失败'.format(ip))
            else:
                print('{}——信息录入数据库失败，录入失败原因:{}'.format(ip,e))
        else:
            print('{}——录入数据库成功'.format(ip))


    def select(self):
        ip = input('请输入需要查询的设备IP信息：')
        sql = """ select * from {} where ip = "{}" """.format(self.table,ip)
        try:
            self.dbcursor.execute(sql)
            results = self.dbcursor.fetchall()
        except:
            print('Error: unable to fetch data about ip_{}'.format(ip))
        else:
            if bool(results) == False:
                print('未查询到相关信息。')
            else:
                for row in results:
                    hostname = row[0]
                    ip = row[1]
                    device = row[2]
                    sn = row[3]
                    version = row[4]
                    patch = row[5]
                    print('''查询信息如下：
                    \rhostname_{} , ip_{} , device_{} , sn_{} , version_{} , patch_{} '''.format(hostname,ip,device,sn,version,patch))

    def close(self):
        self.dbcursor.close()
        self.dbaes.close()






