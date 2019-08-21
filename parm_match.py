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

# output = u'''<JHQGJZXN15F-WM-ACC-42>dis ver
# Huawei Versatile Routing Platform Software
# VRP (R) software, Version 5.170 (S5720 V200R010C00SPC600)
# Copyright (C) 2000-2016 HUAWEI TECH CO., LTD
# HUAWEI S5720S-52P-SI-AC Routing Switch uptime is 0 week, 5 days, 19 hours, 15 minutes
#
# ES5D2T52S003 0(Master)  : uptime is 0 week, 5 days, 19 hours, 14 minutes
# DDR    Memory Size      : 512        M bytes
# FLASH  Memory Size      : 241        M bytes
# Pcb           Version   : VER.B
# BootROM       Version   : 020a.0001
# BootLoad      Version   : 020a.0001
# CPLD          Version   : 010f
# Software      Version   : VRP (R) Software, Version 5.170 (V200R010C00SPC600)
# <JHQGJZXN15F-WM-ACC-42>dis patch
# Patch Package Name   :flash:/s5720si-v200r010sph012.pat
# Patch Package Version:V200R010SPH012
# The state of the patch state file is: Running
# The current state is: Running
#
# ************************************************************************
# *           Information about hot patch errors is as follows:          *
# ************************************************************************
#
#      Slot            CurrentVersion
# ------------------------------------------------------------
#
# No hot patch error occurs on any board.
#
#
# ************************************************************************
# *                The hot patch information, as follows:                *
# ************************************************************************
#
#  Slot       Type           State     Count Time(YYYY-MM-DD HH:MM:SS)
# ------------------------------------------------------------------------
#  0          C              Running   290   2019-08-15 15:19:18+08:00
#
# <JHQGJZXN15F-WM-ACC-42>dis dev
# S5720S-52P-SI-AC's Device status:
# Slot Sub  Type                  Online    Power    Register     Status   Role
# -------------------------------------------------------------------------------
# 0    -    S5720S-52P-SI         Present   PowerOn  Registered   Normal   Master
# <JHQGJZXN15F-WM-ACC-42>dis esn
# ESN of slot 0: 2102350DLQDMHC002400
# <JHQGJZXN15F-WM-ACC-42>
# '''.encode('utf-8')
# sw1 = parm_match(output)
# parm = sw1.five_tuple()
# print(parm)


