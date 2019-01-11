#! /usr/bin/env python
# -*- encoding: utf-8 -*-

import sys,os,re

print '\n.......................Code Style Checking....................\n'

#the count of level, like ERROR,WARN
def get_level(content, level):
    return len(re.compile(r"\[%s\]" % level).findall(content))

#get the commit file name (whole path)
def get_file_name(content, postfix=None):
    content = content.replace("\t", " ")
    line_divided = content.split("\n")
    space_divided = [[j for j in i.split(" ") if j.strip()]for i in line_divided]
    filenames = [i[5] for i in space_divided if i]
    if not postfix:
        return filenames
    return [i for i in filenames if ".%s" % postfix in i]

jarpath = os.popen('git config --get checkstyle.jar').read()
checkfilepath = os.popen('git config --get checkstyle.checkfile').read()

#check code command
command = 'java -jar ' + jarpath[:-1] + ' -c ' + checkfilepath[:-1]

#the file to check
files = os.popen('git diff-index --cached HEAD').read()

#the result of command
content = get_file_name(files, 'java')

resultsum = 0

for i in content:
    result = os.popen(command + ' ' + i).read()
    print result
    resultsum += get_level(result,'ERROR')
    resultsum += get_level(result,'WARN')

if resultsum > 0:
    print '\n.......................You must fix the errors and warnings first, then excute commit command again...........\n'
    sys.exit(-1)
else:
    print '\n.................................Code is very good...................\n'
    sys.exit(0)
