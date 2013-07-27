#!/usr/bin/python
#Filename:backup_ver1.py

import os
import time

#1.The files and directiories to backed uo are specified in a list.
source = ['/Users/cjh/work/shell/littletool', '/Users/cjh/Dev/python/learn']
#if you are using Windows, use source = [r'C:\Documents', r'D:\Work']

#2.The back up must be stored in a main backup directory
target_dir = '/Users/cjh/Dev/python/practice/backup/'

#3.The files are backed uo into a zip file.
#4.The name of the zip archives is the current date and time
target = target_dir + time.strftime('%Y%m%d%H%M%S') + '.zip'

#5.we use the zip command(in Unix/Liunx) to put the files in a zip archive
zip_command = "zip -qr '%s' %s" %(target, ' '.join(source))

#Run the backup
if os.system(zip_command) == 0:
	print 'Successful back up to', target
else:
	print 'Back up FAILED'



