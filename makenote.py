#!/usr/bin/env python
import os
import time 

dirPath, dirName = os.path.split(os.getcwd())
date = time.strftime("%d/%m/%y %H:%M")

print "Course/Project: ", dirName
print "Date:           ", date
print 
print
