#!/usr/bin/python
# -*- encoding: utf-8 -*-
from lxml.html import parse
from urllib2 import urlopen
import numpy as np
import os
import datetime
import locale

d = datetime.datetime.today()

date = str(d.year).zfill(4)+str(d.month).zfill(2)+str(d.day).zfill(2)+str(d.hour).zfill(2)+str(d.minute).zfill(2)+str(d.second).zfill(2)
print date

parsed = parse(urlopen('http://www.x-rates.com/table/?from=USD&amount=1.00'))
doc = parsed.getroot()

tables = doc.findall('.//thead')
calls = tables[1]
rows = calls.findall('.//tr')

def _unpack(row, kind='th'):
	elts = row.findall('.//%s' % kind)
	return [val.text_content() for val in elts]

original = _unpack(rows[0], kind='th')

tables = doc.findall('.//tbody')
calls = tables[1]
rows = calls.findall('.//tr')

def _unpack(row, kind='td'):
	elts = row.findall('.//%s' % kind)
	return [val.text_content() for val in elts]

#Output{{{
f = open("rates/Ast_Doller.d","a")
compare = _unpack(rows[1], kind='td')
f.write(date+' '+compare[1])
f.write('\n')
f.close()
f = open("rates/Bri_Pound.d","a")
compare = _unpack(rows[53], kind='td')
f.write(date+' '+compare[1])
f.write('\n')
f.close()
f = open("rates/Chi_Yuan.d","a")
compare = _unpack(rows[9], kind='td')
f.write(date+' '+compare[1])
f.write('\n')
f.close()
f = open("rates/EU_Euro.d","a")
compare = _unpack(rows[14], kind='td')
f.write(date+' '+compare[1])
f.write('\n')
f.close()
f = open("rates/Ind_Rupee.d","a")
compare = _unpack(rows[18], kind='td')
f.write(date+' '+compare[1])
f.write('\n')
f.close()
f = open("rates/Jap_Yen.d","a")
compare = _unpack(rows[22], kind='td')
f.write(date+' '+compare[1])
f.write('\n')
f.close()
f = open("rates/Rus_Ruble.d","a")
compare = _unpack(rows[41], kind='td')
f.write(date+' '+compare[1])
f.write('\n')
f.close()
f = open("rates/Swi_Franc.d","a")
compare = _unpack(rows[47], kind='td')
f.write(date+' '+compare[1])
f.write('\n')
f.close()
#}}}


