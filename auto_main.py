import parm_match
import mysql_behavior
import ssh_behavior
import sys
import csv

ip_list=sys.argv[1]
command_list = sys.argv[2]

switch_connect = ssh_behavior.ssh_behavior('pinduoduo@system','mko0MKO)')

with open(ip_list) as ip_list_o:
    ip_list_r = csv.reader(ip_list_o)
    for ip_r in ip_list_r:
        ip = ip_r[0]
        log= switch_connect.connect(ip,command_list)
        if log == False:
            print('登陆失败')
        else:
            switch_search = parm_match.parm_match(log)
            five_tuple=switch_search.five_tuple()
            print(five_tuple)
            switch_register = mysql_behavior.mysql_behavior()
            switch_register.insert(ip,five_tuple)
switch_connect.close()


