#!/usr/bin/python
# -*- encoding: utf-8 -*-
from lxml.html import parse
from urllib2 import urlopen

parsed = parse(urlopen('http://www.x-rates.com/table/?from=USD&amount=1.00'))
doc = parsed.getroot()

tables = doc.findall('.//tbody')
calls = tables[1]
rows = calls.findall('.//tr')

def _unpack(row, kind='td'):
	elts = row.findall('.//%s' % kind)
	return [val.text_content() for val in elts]

original = _unpack(rows[0], kind='th')

compare = _unpack(rows[0], kind='td')
print original
print compare
