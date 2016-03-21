#!/usr/bin/python
# coding: UTF-8
from lxml.html import parse
from lxml import etree
from urllib2 import urlopen
import numpy as np
import os
import datetime
import locale
import time
import sys
import csv
from xml.etree.ElementTree import Element, SubElement, Comment
#from ElementTree_pretty import prettify

def _unpack(row, kind=''):
	elts = row.findall('.//%s' % kind)
	return [val.text_content() for val in elts]
def _unpack(row, kind='td'):
	elts = row.findall('.//%s' % kind)
	return [val.text_content() for val in elts]

#HTMLSetting
#f = open("ana.d","w")
out = open("ana.csv","w")
csvOUT = csv.writer(out)
outarray = np.array([])
element = np.array([])

#f.write('<?xml version="1.0" encoding="utf-8" ?>')
#f.write('\n')
#f.close()

#{{{
elem = [
'Date',
'Type',
'BPMax',
'BPMin',
'BPulse',
'ALT',
'GTP',
'TP',
'ALB',
'AG',
'CHOL',
'GA',
'RBC',
'Hb',
'Ht',
'MCV',
'MCH',
'MCHC',
'WBC',
'PLT']
#}}}

for n in range(0,9):
	#print n
	#print 'No'+str(n+1)+'.xml'
	root = parse('No'+str(n+1)+'.xml')
	doc = root.getroot()
	rows = doc.findall('.//tr')
	
	#{{{	
	#f = open("ALT.xml","a")
	#Date    = _unpack(rows[ 0], kind='td')
	#Type    = _unpack(rows[ 1], kind='td')
	#BPMax   = _unpack(rows[ 2], kind='td')
	#BPMin   = _unpack(rows[ 3], kind='td')
	#BPulse  = _unpack(rows[ 4], kind='td')
	#ALT     = _unpack(rows[ 5], kind='td')
	#GTP     = _unpack(rows[ 6], kind='td')
	#TP      = _unpack(rows[ 7], kind='td')
	#ALB     = _unpack(rows[ 8], kind='td')
	#AG      = _unpack(rows[ 9], kind='td')
	#CHOL    = _unpack(rows[10], kind='td')
	#GA      = _unpack(rows[11], kind='td')
	#RBC     = _unpack(rows[12], kind='td')
	#Hb      = _unpack(rows[13], kind='td')
	#Ht      = _unpack(rows[14], kind='td')
	#MCV     = _unpack(rows[15], kind='td')
	#MCH     = _unpack(rows[16], kind='td')
	#MCHC    = _unpack(rows[17], kind='td')
	#WBC     = _unpack(rows[18], kind='td')
	#PLT     = _unpack(rows[19], kind='td')
	#}}}

	num = range(2,7)
	for j in reversed(num):
		for i in range(0,20):
			compare = _unpack(rows[i], kind='td')
			element = np.append(element,compare[j].encode('utf-8'))
			
			#f.write(compare[j].encode('utf-8'))
		csvOUT.writerow(element)
		##print j
		##f.write('<'+elem[i]+'>'+compare[j].encode('utf-8')+'</'+elem[i]+'>')
		##f.write(compare[j].encode('utf-8'))
		#f.write(str(Date)+' '+str(Type)+' '+str(BPMax)+' '+str(BPMin)+' '+str(BPulse)+' '+str(ALT)+' '+str(GTP)+' '+str(TP)+' '+str(ALB)+' '+str(AG)+' '+str(CHOL)+' '+str(GA)+' '+str(RBC)+' '+str(Hb)+' '+str(Ht)+' '+str(MCV)+' '+str(MCH)+' '+str(MCHC)+' '+str(WBC)+' '+str(PLT))
		##f.write('\n')
#f.close()


