#!/usr/bin/python3

import pymysql
from datetime import date
from termcolor import colored


print "\n\n\n"
db = pymysql.connect("localhost","root","","TODO" )
cursor = db.cursor()
today = date.today()
print "DATE:",today
print "KIND REMAINDER ----->"
print "\n"
sql = "SELECT * FROM TODO"
cursor.execute(sql)
results = cursor.fetchall()
i = 0
today = str(today)
print "WORK TO DO TODAY\n"
for row in results:
	date = row[0]
	date = str(date)
	if(date == today):
		i = 1
       		time = row[1]
		content = row[2]
		checked = row[4]
		if(checked == False):
			priority = row[3]
			if(priority==1):
				print colored(time,'red'), "----->",colored(content,'red')

			if(priority==2):
				print colored(time,'blue'), "----->",colored(content,'blue')

			if(priority==3):
				print colored(time,'yellow'), "----->",colored(content,'green')

if( i == 0):
	print colored('NO REMAINDERS TODAY','cyan')
print "\n\n\n"
db.close()
