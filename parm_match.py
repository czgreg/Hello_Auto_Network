#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import re

class parm_match():

    def __init__(self,log):
        self.log=log

#hostname,ip,device,sn,version,patch

    def hostname(self):
        hostname = re.search(r"<.*>",self.log)
        self.realhost = hostname.group()[1:-1]

    def ip(self):
        ip = re.search(r"\d{2,3}.\d{2,3}.\d{2,3}.\d{2,3}",self.log)
        self.realip = ip.group()

    def device(self):
        #device = re.search(r"S\d{4}\w?-\d{2}\w?P(-PWR)?-\wI-\wC", self.log)
        device = re.search(r"\n.*'s Device status:", self.log)
        if device == None:
            print('{}匹配失败'.format(self.realhost))
            self.realtype = '未知型号'
        else:
            self.realtype = device.group()[1:-17]

    def sn(self):
        sn = re.search(r"21\w{18}", self.log)
        self.realsn = sn.group()

    def version(self):
        version = re.search(r"V\d{3}R\d{3}C\w{2,}", self.log)
        self.realver = version.group()

    def patch(self):
        patch = re.search(r"V\d{3}R\d{3}SPH\d{2,}", self.log)
        if bool(patch) == False:
            self.realpatch = 'No patch exists'
        else:
            self.realpatch = patch.group()

    def five_tuple(self):
        self.hostname()
        self.device()
        self.sn()
        self.version()
        self.patch()
        return self.realhost,self.realtype,self.realsn,self.realver,self.realpatch
