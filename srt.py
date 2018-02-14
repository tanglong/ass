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

def rm(filename):
    os.system("rm -Rf %s" % filename.replace("\\","/") )

def copy(src,dst):
    system("cp %s %s" % (src,dst) )



re_package = re.compile(r"-->")
re_package_num = re.compile(r"\d+")


file_name_re = re.compile(r"(.*)\.srt")

for root, dir, files in os.walk("."):
   if root != ".":
       continue
   for name in files:
        file_name_match = file_name_re.match(name)
        if file_name_match is None:
            continue
        newfilename =  file_name_match.group(1)+".md"
        with open(name, 'r') as src:
            with open(newfilename, 'w') as dest:
                for line in src:
                    match = re_package.search(line)
                    if match is None:
                        line = line.rstrip('\n')
                        line = line.rstrip('\r')
                        line = line.rstrip()
                        if line == "":
                            continue
                        match2 = re_package_num.match(line)
                        if match2 is None:
                            dest.write('%s%s\n' % ('\t', line))
                        else:
                            continue
                    else:
                        continue
