#!/usr/bin/python3

import pymysql
import datetime
from termcolor import colored

db = pymysql.connect("localhost","root","","TODO" )
cursor = db.cursor()

print "WELCOME"
print "1.ADD 2.EDIT 3.UPDATE 4.DELETE 5.VIEW"
num=input()

if(num==1):
	while(1):
		day = input("Enter the date:")
		if(day<=31):
			d=str(day)
			break
		else:
			print "Enter correctly"
	while(1):
		month = input("Enter the month:")
		if(month<=12):
			m=str(month)
			break
		else:	
			print "Enter correctly"
	while(1):
		year = input("Enter the year:")
		if(year<=9999):
			y=str(year)
			break
		else:
			print "Enter correctly"
	dat=y+"-"+m+"-"+d
	while(1):
		hour = input("Enter the hour:")
		if(hour<=24):
			h=str(hour)
			break
		else:	
			print "Enter correctly"
	while(1):
		mins = input("Enter the minutes:")
		if(mins<=60):
			mi=str(mins)
			break
		else:
			print "Enter correctly"
	tim=h+":"+mi+":"+"00"
	cont = raw_input("ENTER THE WORK:")
	while(1):
		prior = input("Enter the priority 1.high 2.mid 3.low:")
		if(prior<=3):
			break
		else:
			print "Enter correctly"
	sql ="INSERT INTO TODO(date,time,content,priority,checked)VALUES('%s','%s','%s','%d', 0)" %(dat,tim,cont,prior)
	cursor.execute(sql)
	db.commit()

if(num==2):
	i=0
	j=0
	count=0
	sql="SELECT * FROM TODO"
	cursor.execute(sql) 
	results = cursor.fetchall()
	while(i == 0):
		while(1):
			day = input("Enter the date:")
			if(day<=31):
				d=str(day)
				break
			else:
				print "Enter correctly"
		while(1):
			month = input("Enter the month:")
			if(month<=12):
				m=str(month)
				break
			else:	
				print "Enter correctly"
		while(1):
			year = input("Enter the year:")
			if(year<=9999):
				y=str(year)
				break
			else:
				print "Enter correctly"
		if(month >=10):
			if(day >=10):
				dat=y+"-"+m+"-"+d
			else:
				dat=y+"-"+m+"-0"+d
		else:
			if(day >=10):
				dat=y+"-0"+m+"-"+d
			else:
				dat=y+"-0"+m+"-0"+d
		for row in results:
			da = row[0]
			da = str(da)
			if(dat == da):
				i = 1
				print row[1]
		if(i == 0):
			print "Enter the date u have already entered"
	while(j == 0):
		while(1):
			hour = input("Enter the hour:")
			if(hour<=24):
				h=str(hour)
				break
			else:	
				print "Enter correctly"
		while(1):
			mins = input("Enter the minutes:")
			if(mins<=60):
				mi=str(mins)
				break
			else:
				print "Enter correctly"
		if(mins >=10):
			tim=h+":"+mi+":00"
		else:
			tim=h+":0"+mi+":00"
		for row in results:
			da = row[1]
			da = str(da)
			if(tim == da):
				j = 1
				content = raw_input("Enter the work to be changed:")
				sql="UPDATE TODO SET content = '%s'WHERE date= '%s' and time = '%s'" %(content,dat,tim)
				cursor.execute(sql)
				db.commit()
				n = input("want to edit priority...press 1")
				if(n == 1):
					while(1):
						prior = input("Enter the priority 1.high 2.mid 3.low:")
						if(prior<=3):
		       					 break
						else:
		        				print "Enter correctly"
					sql="UPDATE TODO SET priority = '%d'WHERE date= '%s' and time = '%s'" %(prior,dat,tim)
					cursor.execute(sql)
					db.commit()
				print "\n---------EDITED--------\n"
		if(j == 0):
			print "Enter the time from above"

if(num==3):
	i=0
	j=0
	print "UPDATE THE WORKLIST AS DONE......\n"
	count=0
	sql="SELECT * FROM TODO"
	cursor.execute(sql) 
	results = cursor.fetchall()
	while(i == 0):
		while(1):
			day = input("Enter the date:")
			if(day<=31):
				d=str(day)
				break
			else:
				print "Enter correctly"
		while(1):
			month = input("Enter the month:")
			if(month<=12):
				m=str(month)
				break
			else:	
				print "Enter correctly"
		while(1):
			year = input("Enter the year:")
			if(year<=9999):
				y=str(year)
				break
			else:
				print "Enter correctly"
		if(month >=10):
			if(day >=10):
				dat=y+"-"+m+"-"+d
			else:
				dat=y+"-"+m+"-0"+d
		else:
			if(day >=10):
				dat=y+"-0"+m+"-"+d
			else:
				dat=y+"-0"+m+"-0"+d
		for row in results:
			da = row[0]
			da = str(da)
			if(dat == da):
				i = 1
				print row[2]
		if(i == 0):
			print "Enter the date u have already entered"
	while(j == 0):
		work = raw_input("Enter the work from above to be marked as done:")
		for row in results:
			da = row[2]
			if(work == da):
				j = 1
				sql="UPDATE TODO SET checked = '1'WHERE date= '%s' and content = '%s'" %(dat,work)
				cursor.execute(sql)
				db.commit()
			print "\n----------UPDATED--------------\n"
		if(j == 0):
			print "Enter the work from above"

if(num==4):
	i=0
	j=0
	count=0
	sql="SELECT * FROM TODO"
	cursor.execute(sql) 
	results = cursor.fetchall()
	while(i == 0):
		while(1):
			day = input("Enter the date:")
			if(day<=31):
				d=str(day)
				break
			else:
				print "Enter correctly"
		while(1):
			month = input("Enter the month:")
			if(month<=12):
				m=str(month)
				break
			else:	
				print "Enter correctly"
		while(1):
			year = input("Enter the year:")
			if(year<=9999):
				y=str(year)
				break
			else:
				print "Enter correctly"
		if(month >=10):
			if(day >=10):
				dat=y+"-"+m+"-"+d
			else:
				dat=y+"-"+m+"-0"+d
		else:
			if(day >=10):
				dat=y+"-0"+m+"-"+d
			else:
				dat=y+"-0"+m+"-0"+d
		for row in results:
			da = row[0]
			da = str(da)
			if(dat == da):
				i = 1
				print row[1]
		if(i == 0):
			print "Enter the date u have already entered"
	while(j == 0):
		while(1):
			hour = input("Enter the hour:")
			if(hour<=24):
				h=str(hour)
				break
			else:	
				print "Enter correctly"
		while(1):
			mins = input("Enter the minutes:")
			if(mins<=60):
				mi=str(mins)
				break
			else:
				print "Enter correctly"
		if( mins >=10):
			tim = h+":"+mi+":"+"00"
		else:
			tim = h+":"+"0"+mi+":"+"00"
		for row in results:
			da = row[1]
			da = str(da)
			if(tim == da):
				j = 1
				sql="DELETE FROM TODO WHERE date= '%s' and time = '%s'" %(dat,tim)
				cursor.execute(sql)
				db.commit()
				print "\n------DELETED-----\n"
		if(j == 0):
			print "Enter the time from above"
if(num==5):
	i=0
	j=0
	count=0
	sql="SELECT * FROM TODO"
	cursor.execute(sql) 
	results = cursor.fetchall()
	while(i == 0):
		while(1):
			day = input("Enter the date:")
			if(day<=31):
				d=str(day)
				break
			else:
				print "Enter correctly"
		while(1):
			month = input("Enter the month:")
			if(month<=12):
				m=str(month)
				break
			else:	
				print "Enter correctly"
		while(1):
			year = input("Enter the year:")
			if(year<=9999):
				y=str(year)
				break
			else:
				print "Enter correctly"
		if(month >=10):
			if(day >=10):
				dat=y+"-"+m+"-"+d
			else:
				dat=y+"-"+m+"-0"+d
		else:
			if(day >=10):
				dat=y+"-0"+m+"-"+d
			else:
				dat=y+"-0"+m+"-0"+d
		print "\n\nDATE : ",colored(dat,'cyan')
		print "TIME ------WORK------------PRIORITY-----WORKDONESTATUS"
		for row in results:
			da = row[0]
			da = str(da)
			if(dat == da):
				i = 1
				if(row[4] == False):
					print colored(row[1],'red'),"-----",colored(row[2],'blue'),"-----",row[3],"-----NO"
				else:
					print colored(row[1],'red'),"-----",colored(row[2],'blue'),"-----",row[3],"-----YES" 
		if(i == 0):
			print "Enter the date correctly"
db.close()
