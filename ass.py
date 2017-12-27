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

#re_package = re.compile(r"Effect,({.*})*(.*)\\N{.*}{.*}{.*}{.*}{.*}{.*}{.*}(.*)")
#re_package = re.compile(r"Dialogue(.*),(.*),(.*),(.*),(.*),(.*),(.*),(.*),(.*),(.*)({.*})*(.*)")
#re_package = re.compile(r"Dialogue(.*),(.*),(.*),(.*),(.*),(.*),(.*),(.*),(.*),(.*)({.*})({.*})({.*})({.*})({.*})({.*})(.*)")
#re_package = re.compile(r"Dialogue(.*),(.*),(.*),(.*),(.*),(.*),(.*),(.*),(.*),({.*})(.*)({.*})\\N({.*})(.*)({.*})")
#re_package = re.compile(r"Dialogue(.*),(.*),(.*),(.*),(.*),(.*),(.*),(.*),(.*),(.*)\\N(.*)")
#re_package = re.compile(r"Dialogue(.*),(.*),(.*),(.*),(.*),(.*),(.*),(.*),(.*),(.*)\\N({.*})({.*})({.*})({.*})({.*})({.*})({.*})(.*)")
re_package = re.compile(r"Dialogue(.*),(.*),(.*),(.*),(.*),(.*),(.*),(.*),(.*),({.*})(.*)({.*})\\N({.*})(.*)({.*})")
file_name_re = re.compile(r"(.*)\.ass")

for root, dir, files in os.walk("."):
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
                        continue
                    str1 = match.group(11)
                    dest.write('%s%s\n' % ('\t', str1.rstrip('\n')))
                    str2 = match.group(14)
                    dest.write('%s%s\n' % ('\t', str2.rstrip('\n')))
