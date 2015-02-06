#!/usr/bin/python
# -*- encoding: utf-8 -*-
import mechanize

url1 = 'http://finance.yahoo.com/q/op?s=AAPL+Options'
url2 = 'http://www.x-rates.com/table/?from=USD&amount=1.00'
b = mechanize.Browser()
b.open(url1)

html = b.response().read()

f = open("Yahoo_finance.html","w")
f.write(html)
f.close()
