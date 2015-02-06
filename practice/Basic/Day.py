#!/usr/bin/python
# -*- coding: utf-8 -*-
import datetime

if __name__ == "__main__":
	today       = datetime.date.today()
	todaydetail = datetime.datetime.today()
	print today,"Year,Month,Day"
	print todaydetail,"Year,Month,Day,Hour,Minute,Second,Microsecond"
	print today.year
	print today.month
	print today.day
	print todaydetail.year
	print todaydetail.month
	print todaydetail.day

