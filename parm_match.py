#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import re

class parm_match():

    def __init__(self,log):
        self.log=log

#hostname,ip,device,sn,version,patch

    def hostname(self):
        hostname = re.search(r"<\S{3,30}>",self.log)
        self.realhost = hostname.group()[1:-1]

    def ip(self):
        ip = re.search(r"\d{2,3}.\d{2,3}.\d{2,3}.\d{2,3}",self.log)
        self.realip = ip.group()

    def device(self):
        device = re.search(r"S\d{4}\w?-\d{2}\w[-PWR]?-\w{2}-\w{2}", self.log)
        self.realtype = device.group()

    def sn(self):
        sn = re.search("210\w{17}", self.log)
        self.realsn = sn.group()

    def version(self):
        version = re.search(r"V\d{3}R\d{3}C\w{2,}", self.log)
        self.realver = version.group()

    def patch(self):
        patch = re.search(r"V\d{3}R\d{3}SPH\d{3,}", self.log)
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
