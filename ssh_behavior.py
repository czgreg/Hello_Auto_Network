#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import paramiko
import time
import csv

class ssh_behavior():

    def __init__(self,username='1111',password='2222)'): ####可以设置默认账号密码，便于个人调用
        self.username = username
        self.password = password
        self.ssh_client = paramiko.SSHClient()
        self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def connect(self,ip,cfg):
        self.ip = ip
        try:
            self.ssh_client.connect(self.ip,22,self.username,self.password,timeout=5)
        except Exception as e:
            if 'Authentication' in str(e).split(' '):
                print('{}认证失败'.format(ip))
                with open('auth_faile_ip.txt', 'w+') as auth_f:
                    auth_f.write(ip + '\n')
                return False
            elif 'timed' in str(e).split(' '):
                print('{}连接超时'.format(ip))
                with open('connect_faile_ip.txt', 'w+') as connect_f:
                    connect_f.write(ip + '\n')
                return False
            else:
                print('{}无法连接'.format(ip))
                with open('any_faile_ip.txt', 'w+') as any_f:
                    any_f.write(ip + '\n')
                return False
        else:
            print('\nSuccessfully connect to {}'.format(self.ip))
            self.command = self.ssh_client.invoke_shell()
            with open(cfg) as command_list_o:
                command_list_r = csv.reader(command_list_o)
                for c in command_list_r:
                    command_send = c[0]
                    self.command.send(command_send + '\n')
                    time.sleep(0.3)
            output = self.command.recv(65535)
            with open('ok_ip.txt','w+') as ok_w:
                ok_w.write(self.ip+'\n')
            return output.decode('utf-8')

    def close(self):
        self.ssh_client.close()

