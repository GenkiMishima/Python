#!/usr/bin/python

def test(num1,num2,operation):

	if operation == 1:
		print "summention"
		print num1+num2

	elif operation == 2:
		print "defferation"
		print num1-num2

	elif operation == 3:
		print "multiply"
		print num1*num2

	elif operation == 4:
		print "waru"
		print num1/num2

	else:
		print "No operation"

if __name__== "__main__":
	test(100,10,4)
