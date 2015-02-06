#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import traceback

def exception_test(value1,value2):
	print "--------"
	result = 0
	try:
		result = value1+value2
	except:
		print "Cancel"
	finally:
		print "End"
	return result
def calc(list1,list2):
	try:
		print exception_test(list1[0],list2[0])
		print exception_test(list1[1],list2[1])
		print exception_test(list1[2],list2[2])
	except:
		print 'conform error'
if __name__ == "__main__":
	try:
		print exception_test(100,"200")
	except:
		print "------------------"
		print traceback.format_exc(sys.exc_info()[2])
		print "------------------"

	#print 'raise'
	#list1 = [100,200,300]
	#list2 = [100,200,'300']
	#calc(list1,list2)
