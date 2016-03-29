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

def PlotDataChoice(DATA,NAME,COUNTER):
	#INDEX{{{
	#Number     = DATA[:, 0]
	#Time       = DATA[:, 1]
	#Type       = DATA[:, 2]
	#PulseTest
	#BldPresMax = DATA[:, 3]
	#BldPresMin = DATA[:, 4]
	#HeartRate  = DATA[:, 5]
	#BioChemistryTest
	#ALTGPT     = DATA[:, 6]
	#GammaGTP   = DATA[:, 7]
	#TP         = DATA[:, 8]
	#ALB        = DATA[:, 9]
	#AG         = DATA[:,10]
	#CHOL       = DATA[:,11]
	#GA         = DATA[:,12]
	#BloodCellCountTest
	#RBC        = DATA[:,13]
	#Hb         = DATA[:,14]
	#Ht         = DATA[:,15]
	#MCV        = DATA[:,16]
	#MCH        = DATA[:,17]
	#MCHC       = DATA[:,18]
	#WBC        = DATA[:,19]
	#PLT        = DATA[:,20]
	#}}}
	plt.plot(DATA[:,0],DATA[:,COUNTER],label=NAME[COUNTER])
	plt.grid()
	plt.xlabel('Number')
	plt.legend(loc = 'upper left')
	plt.show()
def PlotDataAll(DATA,NAME):
	#INDEX{{{
	#Number     = DATA[:, 0]
	#Time       = DATA[:, 1]
	#Type       = DATA[:, 2]
	#BldPresMax = DATA[:, 3]
	#BldPresMin = DATA[:, 4]
	#HeartRate  = DATA[:, 5]
	#ALTGPT     = DATA[:, 6]
	#GammaGTP   = DATA[:, 7]
	#TP         = DATA[:, 8]
	#ALB        = DATA[:, 9]
	#AG         = DATA[:,10]
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
	#}}}

	#Pulse
	#fig, ax1 = plt.subplots()
	#plt.title('PulseData')
	#ax1.plot(DATA[:,0],DATA[:,3],'b-',label=NAME[3])
	#ax1.plot(DATA[:,0],DATA[:,4],'b-',label=NAME[4])
	#ax2 = ax1.twinx()
	#ax2.plot(DATA[:,0],DATA[:,5],'r-',label=NAME[5])
	plt.title('PulseData')
	plt.plot(DATA[:,0],DATA[:,3],'b-',label=NAME[3])
	plt.plot(DATA[:,0],DATA[:,4],'r-',label=NAME[4])
	plt.plot(DATA[:,0],DATA[:,5],'g-',label=NAME[5])
	plt.legend()
	plt.show()
	plt.close()
	#BioChemicalData
	plt.title('BioChemicalData')
	plt.plot(DATA[:,0],DATA[:,6],'b-',label=NAME[6])
	plt.plot(DATA[:,0],DATA[:,7],'r-',label=NAME[7])
	plt.plot(DATA[:,0],DATA[:,8],'g-',label=NAME[8])
	plt.plot(DATA[:,0],DATA[:,9],'y-',label=NAME[9])
	plt.plot(DATA[:,0],DATA[:,10],'m-',label=NAME[10])
	plt.plot(DATA[:,0],DATA[:,12],'k-',label=NAME[12])
	plt.legend()
	plt.show()
	plt.close()
	#BloodCellNumber
	plt.title('BloodCellNumber')
	plt.plot(DATA[:,0],DATA[:,14],'b-',label=NAME[14])
	plt.plot(DATA[:,0],DATA[:,15],'r-',label=NAME[15])
	plt.plot(DATA[:,0],DATA[:,16],'g-',label=NAME[16])
	plt.plot(DATA[:,0],DATA[:,17],'y-',label=NAME[17])
	plt.plot(DATA[:,0],DATA[:,18],'m-',label=NAME[18])
	plt.plot(DATA[:,0],DATA[:,19],'k-',label=NAME[19])
	plt.legend()
	plt.show()
	plt.close()
	#fig, ax1 = plt.subplots()
	#ax1.title('BloodCellNumber')
	#ax1.plot(DATA[:,0],DATA[:,3],'b-',label=NAME[3])
	#ax1.plot(DATA[:,0],DATA[:,4],'b-',label=NAME[4])
	#ax2 = ax1.twinx()
	#ax2.plot(DATA[:,0],DATA[:,5],'r-',label=NAME[5])
	#plt.show()
	#plt.close()

	#plt.plot(DATA[:,0],DATA[:,COUNTER],label=NAME[COUNTER])
	#plt.grid()
	#plt.xlabel('Number')
	#plt.legend(loc = 'upper left')
	#plt.show()

if __name__ == "__main__":
	#COUNTER = int(sys.argv[1])
	DATA = sp.genfromtxt('ALLDATA.csv',delimiter=',')
	NAME = np.array(['Number','Time','Type','BldPresMax','BldPresMin','HeartRate','ALTGPT[IU/L]','GammaGTP[IU/L]','TP[g/dL]','ALB[g/dL]','AG','CHOL[mg/dL]','GA','RBC[*10^-4/$\mu$L]','Hb[g/dL]','Ht[%]','MCV[fL]','MCH[pg]','MCHC[%]','WBC[*10^2/$\mu$L]','PLT[*10^4/$\mu$L]'])
	#PlotDataChoice(DATA,NAME,COUNTER)
	PlotDataAll(DATA,NAME)
