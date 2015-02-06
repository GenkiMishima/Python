#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib2
from HTMLParser import HTMLParser

class TESTParser:
	def __init__(self):
		HTMLParser.__init__(self)
	def handle_starttag(self,tagname,attribute):
		if tagname.lower() == "a":
			for i in attribute:
				if i[0].lower() == "href":
					print i[1]

if __name__ == "__main__":
	url = "http://blog.livedoor.jp/morning77/"
	htmldata = urllib2.urlopen(url)

	parser = TESTParser()
	parser.feed(htmldata.read())
	parser.close()


	OBJ = open("test.html","w")
	print unicode(htmldata.read(),"utf-8")
	htmldata.close()

