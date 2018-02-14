#coding: utf-8

import os
import sys
import re
import subprocess
import datetime

reload(sys)  
sys.setdefaultencoding('utf8')

def system(cmd):
    ret = os.system(cmd)
    if ret!=0:
        sys.exit(ret)

system("python ass.py")
system("python srt.py")

