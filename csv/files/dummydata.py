# make four differently formatted transaction csv files
# for SOPs ETL demo, by c.p.brown, 2019

from datetime import datetime
import random
import string
import os

cdr = os.path.split(os.path.realpath(__file__))[0]

def padstr(instr, pad, padlen) :
	dif = (padlen - len(instr)) + 1
	o = instr
	for i in range(1,dif) :
		o = o + pad
	return(o)

def prepadstr(instr, pad, padlen) :
	dif = (padlen - len(instr)) + 1
	o = ''
	for i in range(1,dif) :
		o = o + pad
	o = o + instr
	return(o)

def prepret(y,m,d,l) :
	ds = prepadstr(str(d),'0',2)
	ms = prepadstr(str(m),'0',2)
	dn = (str(y)[2:] + prepadstr(str(m),'0',2) + ds)
	lds = (str(y) + l + ms + l + ds)
	return([dn,lds])

# one

o = []
head = "date,amount,description,balance"

startdate = "010101"
dt = datetime.strptime(startdate,'%y%m%d')
oo = datetime.toordinal(dt)

for i in range(10000) :
	random.seed(i)
	vnd = ''.join([random.choice(string.ascii_uppercase) for _ in range(4)])
	d = random.random()
	oo = oo + int(d * 15.0)
	dt = datetime.fromordinal(oo)
	damt = "{0:.2f}".format(d * -1000.0)
	amt = "\"" + str(damt) + "\""
	o.append([prepret(dt.year,dt.month,dt.day,'/')[1],amt,("\"TRANSACTION DESCRIPTION FROM VENDOR: " + vnd + "\""),"\"\""])

f = open( cdr +'/one.csv','w')
for i in o :
	f.write(i[0] + ', ' + i[1] + ', ' + i[2] + ', ' + i[3] + '\n')
f.close()

# two

o = []
head="Date,Description,Debit,Credit,Balance"

startdate = "010101"
dt = datetime.strptime(startdate,'%y%m%d')
oo = datetime.toordinal(dt)

for i in range(10000) :
	random.seed(i*20010)
	vnd = ''.join([random.choice(string.ascii_uppercase) for _ in range(4)])
	d = random.random()
	oo = oo + int(d * 15.0)
	dt = datetime.fromordinal(oo)
	damt = "{0:.2f}".format(d * -1000.0)
	amt = str(damt)
	o.append([prepret(dt.year,dt.month,dt.day,'/')[1],("TRANSACTION DESCRIPTION FROM VENDOR: " + vnd),'',amt,''])

f = open( cdr +'/two.csv','w')
for i in o :
	f.write(i[0] + ', ' + i[1] + ', ' + i[2] + ', ' + i[3] + ', ' + i[4] + '\n')
f.close()

# three

o = []
head = "account,date,description,debit,credit,cat,serial"

startdate = "010101"
dt = datetime.strptime(startdate,'%y%m%d')
oo = datetime.toordinal(dt)

for i in range(10000) :
	random.seed(i*30010)
	vnd = ''.join([random.choice(string.ascii_uppercase) for _ in range(4)])
	d = random.random()
	oo = oo + int(d * 15.0)
	dt = datetime.fromordinal(oo)
	damt = "{0:.2f}".format(d * -1000.0)
	amt = str(damt)
	o.append(['0394',prepret(dt.year,dt.month,dt.day,'/')[1],("TRANSACTION DESCRIPTION FROM VENDOR: " + vnd),amt,'','OTHER',''])

f = open( cdr +'/three.csv','w')
for i in o :
	f.write(i[0] + ', ' + i[1] + ', ' + i[2] + ', ' + i[3] + ', ' + i[4] + ', ' + i[5] + ', ' + i[6] + '\n')
f.close()

# four

o = []
head = "date;amount;description;balance"

startdate = "010101"
dt = datetime.strptime(startdate,'%y%m%d')
oo = datetime.toordinal(dt)

for i in range(10000) :
	random.seed(i*40010)
	vnd = ''.join([random.choice(string.ascii_uppercase) for _ in range(4)])
	d = random.random()
	oo = oo + int(d * 15.0)
	dt = datetime.fromordinal(oo)
	damt = "{0:.2f}".format(d * -1000.0)
	amt = str(damt)
	o.append([prepret(dt.year,dt.month,dt.day,'-')[1],amt,("TRANSACTION DESCRIPTION FROM VENDOR: " + vnd),''])

f = open( cdr +'/four.csv','w')
for i in o :
	f.write(i[0] + '; ' + i[1] + '; ' + i[2] + '; ' + i[3] + '\n')
f.close()
