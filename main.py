import urllib2
from bs4 import BeautifulSoup
import datetime
import re

responce = urllib2.urlopen('http://clist.by/')
html = responce.read()
soup =  BeautifulSoup(html,"lxml")
d = soup.find_all('div',{ "class" : "row contest running"}) 
print "\n---------------------------------------------------------------------------------------------"
print "---------------------------------------------------------------------------------------------"
print "\n\nEnd Time          End Date          Contest Name                                         Hosted by\n\n"
for i in d:
	s=""
	for j in i.find_all('a',href=re.compile('https://www\.timeanddate\.com/')):
		s+=(j.string.lstrip().rstrip())
	h = s[10:12]
	m = s[13:15]
	date = s[0:2]
	month = s[3:5]
	year = datetime.datetime.now().year	
	h=int(h)
	m=int(m)
	date = int(date)
	month=int(month)
	
	m=m+30;
	if m>=60:
		m=m-60
		h=h+1
	h = h+5
	if h>=24:
		h=h-24
		date = date+1
	if (m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12 ) and date>31:
		date=date-31
	elif m==2 and date>28:
		date=date-28
	elif date>30:
		date=date-30
	
	print '%-10s' % ((str(h)+":"+str(m)),)	,
	print "      ",	
	print '%-10s' % ((str(date)+"-"+str(month)+"-"+str(year)),),
	print "      ",
			
	for j in i.find_all('div',{ "class": "title" } ):
		hr=""
		ur=""
		for x in j.find_all('a',title=True):
			ur=x['href']
			hr+=x.string
		print '%-50s' % (hr ,),
	
	for j in i.find_all('small',{ "class":"text-muted"}):
		print '%30s' % (j.getText(),)		
	
	print ur
	print "\n\n"		
print "\n---------------------------------------------------------------------------------------------"
print "         Upcoming               "
print "---------------------------------------------------------------------------------------------"	
d = soup.find_all('div',{ "class" : "row contest coming"})	
for i in d:
	s=""
	for j in i.find_all('a',href=re.compile('https://www\.timeanddate\.com/')):
		s+=(j.string.lstrip().rstrip())
	h = s[10:12]
	m = s[13:15]
	date = s[0:2]
	month = s[3:5]
	year = datetime.datetime.now().year	
	h=int(h)
	m=int(m)
	date = int(date)
	month=int(month)
	
	m=m+30;
	if m>=60:
		m=m-60
		h=h+1
	h = h+5
	if h>=24:
		h=h-24
		date = date+1
	if (m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12 ) and date>31:
		date=date-31
	elif m==2 and date>28:
		date=date-28
	elif date>30:
		date=date-30
	
	print '%-10s' % ((str(h)+":"+str(m)),)	,
	print "      ",	
	print '%-10s' % ((str(date)+"-"+str(month)+"-"+str(year)),),
	print "      ",
			
	for j in i.find_all('div',{ "class": "title" } ):
		hr=""
		ur=""
		for x in j.find_all('a',title=True):
			hr+=x.string
			ur=x['href']
		print '%-50s' % (hr ,),
	
	for j in i.find_all('small',{ "class":"text-muted"}):
		print '%30s' % (j.getText(),)
	print ur
	print "\n\n" 

			
