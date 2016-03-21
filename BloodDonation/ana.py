#!/usr/bin/python
#{{{
import subprocess as subcmd
import re
import scipy as sp
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import lines
import math
import sys
import csv
from string import *
from scipy import interpolate
#Length:m
#Mass:kg
#Time:s
#}}}

def plotdata(DATA,NAME,COUNTER):
	
	#Flight{{{
	#Number     = DATA[:, 0]
	#Time       = DATA[:, 1]
	#Type       = DATA[:, 2]
	#BldPresMax = DATA[:, 3]
	#BldPresMin = DATA[:, 4]
	#HeartRate  = DATA[:, 5]
	#ALTGPT    = DATA[:, 6]
	#GammaGTP   = DATA[:, 7]
	#TP         = DATA[:, 8]
	#ALB        = DATA[:, 9]
	#AG        = DATA[:,10]
	#CHOL       = DATA[:,11]
	#GA         = DATA[:,12]
	#RBC        = DATA[:,13]
	#Hb         = DATA[:,14]
	#Ht         = DATA[:,15]
	#MCV        = DATA[:,16]
	#MCH        = DATA[:,17]
	#MCHC       = DATA[:,18]
	#WBC        = DATA[:,19]
	#PLT        = DATA[:,20]

	plt.plot(DATA[:,0],DATA[:,COUNTER],label=NAME[COUNTER])
	plt.grid()
	plt.xlabel('Number')
	plt.legend(loc = 'upper left')
	#plt.ylim([0,100])
	#plt.savefig("Thrust.png")
	#plt.close()
	plt.show()

	#}}}

if __name__ == "__main__":
	COUNTER = int(sys.argv[1])
	
	DATA = sp.genfromtxt('ALLDATA.csv',delimiter=',')
	NAME = np.array(['Number','Time','Type','BldPresMax','BldPresMin','HeartRate','ALTGPT','GammaGTP','TP','ALB','AG','CHOL','GA','RBC','Hb','Ht','MCV','MCH','MCHC','WBC','PLT'])
	plotdata(DATA,NAME,COUNTER)
