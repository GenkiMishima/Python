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
from xml.etree.ElementTree import Element, SubElement, Comment
#from ElementTree_pretty import prettify

def _unpack(row, kind='th'):
	elts = row.findall('.//%s' % kind)
	return [val.text_content() for val in elts]
def _unpack(row, kind='td'):
	elts = row.findall('.//%s' % kind)
	return [val.text_content() for val in elts]

#HTMLSetting
f = open("get.xml","w")
f.write('<?xml version="1.0" encoding="utf-8" ?>')
f.write('\n')
f.close()

elem = ['Date','Type','BPMax','BPMin','BPulse','ALT','GTP','TP','ALB','AG','CHOL','GA','RBC','Hb','Ht','MCV','MCH','MCHC','WBC','PLT']

for n in range(0,9):
	#print n
	#print 'No'+str(n+1)+'.xml'
	root = parse('No'+str(n+1)+'.xml')
	doc = root.getroot()
	rows = doc.findall('.//tr')
	
	
	f = open("get.xml","a")
	num = range(2,7)
	for j in reversed(num):
		print j
		for i in range(0,20):
			compare = _unpack(rows[i], kind='td')
			f.write('<'+elem[i]+'>'+compare[j].encode('utf-8')+'</'+elem[i]+'>')
			f.write('\n')
		f.write('\n')
f.close()


