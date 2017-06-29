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


re_package = re.compile(r"Effect,{.*}(.*)\\N{.*}{.*}{.*}{.*}{.*}{.*}{.*}(.*)")

with open('The.Lord.of.the.Rings.The.Fellowship.of.the.Ring.2001.EXTENDED.1080p.BluRay.H264.AAC-RARBG.ass', 'r') as src:
    with open('The.Lord.of.the.Rings.The.Fellowship.of.the.Ring.2001.EXTENDED.1080p.BluRay.H264.AAC-RARBG.md', 'w') as dest:
       for line in src:
           match = re_package.search(line)
           if match is None:
               continue
           str1 = match.group(1)
           dest.write('%s%s\n' % ('\t', str1.rstrip('\n')))
           str2 = match.group(2)
           dest.write('%s%s\n' % ('\t', str2.rstrip('\n')))



