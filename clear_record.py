#coding: utf-8

import os
import sys
import re
import subprocess
import datetime

reload(sys)  
sys.setdefaultencoding('utf8')

def system(cmd):
    print cmd
    ret = os.system(cmd)
    if ret!=0:
        sys.exit(ret)

def rm(filename):
    os.system("rm -Rf %s" % filename.replace("\\","/") )

def copy(src,dst):
    system("cp %s %s" % (src,dst) )


def displaymatch(match):
    if match is None:
        return None
    print('<Match: %r, groups=%r>' % (match.group(), match.group(1)))

system('redis-cli -h 10.235.102.208 -p 6381 -n 0 keys "*" > 111')
