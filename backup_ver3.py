#!/usr/bin/python
#Filename:backup_ver3.py

import os
import time

#1.The files and directiories to backed uo are specified in a list.
source = ['/Users/cjh/work/shell/littletool', '/Users/cjh/Dev/python/learn']
#if you are using Windows, use source = [r'C:\Documents', r'D:\Work']

#2.The back up must be stored in a main backup directory
target_dir = '/Users/cjh/Dev/python/practice/backup/'#Remember to change this to what you will be using

#3.The files are backed uo into a zip file.
#4.The current day is the name of the subdirectory in the main directory
today = target_dir + time.strftime('%Y%m%d')
#The current time is the name of the zip archive
now = time.strftime('%H%M%S')

#Take a comment from the user to create the name of the zip file
comment = raw_input('Enter a comment-->')
if len(comment) == 0:#check if a comment was entered
	target = today + os.sep + now + '.zip'
else:
	target = today + os.sep + now + '_' + \
			 comment.replace(' ', '_') + '.zip'
#Create the subdirectory if it isn't already there
if not os.path.exists(today):
	os.mkdir(today) #make dirctory
	print 'Successfully created directory', today

#5.We use the zip command (in Unix/Liunx) to put the files in a zip archive
zip_command = "zip -qr '%s' %s" %(target, ' '.join(source))

#Run the backup
if os.system(zip_command) == 0:
	print 'Successful back up to', target
else:
	print 'Back up FAILED'
