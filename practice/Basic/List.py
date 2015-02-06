#!/usr/bin/python
# -*- coding: utf-8 -*-
test_tple = ('python','-','izm','.','tple')
test_list = ['python','-','izm','.','list']
#for i in test_tple:
#	print i
#for i in test_list:
#	print i
print test_list
print "------------------------"
test_list.append('append')
print test_list
print "------------------------"
test_list.insert(3,'pythonian')
print test_list
print "------------------------"
print test_list.index('pythonian')
print "------------------------"
test_list.remove('pythonian')
print test_list
