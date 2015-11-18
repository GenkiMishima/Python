#!/usr/bin/python
import scipy as sp
import numpy as np
import matplotlib.pyplot as plt

data = sp.genfromtxt("Ast_Doller.d")
x=data[:,0]
y=data[:,1]
plt.subplot(241)
plt.plot(x,y)
plt.title("Ast")
plt.tick_params(labelbottom='off')
plt.grid()

data = sp.genfromtxt("Bri_Pound.d")
x=data[:,0]
y=data[:,1]
plt.subplot(242)
plt.plot(x,y)
plt.title("Bri")
plt.tick_params(labelbottom='off')
plt.grid()


data = sp.genfromtxt("Chi_Yuan.d")
x=data[:,0]
y=data[:,1]
plt.subplot(243)
plt.plot(x,y)
plt.title("Chi")
plt.tick_params(labelbottom='off')
plt.grid()

data = sp.genfromtxt("EU_Euro.d")
x=data[:,0]
y=data[:,1]
plt.subplot(244)
plt.plot(x,y)
plt.title("EU")
plt.tick_params(labelbottom='off')
plt.grid()

data = sp.genfromtxt("Ind_Rupee.d")
x=data[:,0]
y=data[:,1]
plt.subplot(245)
plt.plot(x,y)
plt.title("Ind")
plt.tick_params(labelbottom='off')
plt.grid()

data = sp.genfromtxt("Jap_Yen.d")
x=data[:,0]
y=data[:,1]
plt.subplot(246)
plt.plot(x,y)
plt.title("Jap")
plt.tick_params(labelbottom='off')
plt.grid()

data = sp.genfromtxt("Rus_Ruble.d")
x=data[:,0]
y=data[:,1]
plt.subplot(247)
plt.plot(x,y)
plt.title("Rus")
plt.tick_params(labelbottom='off')
plt.grid()

data = sp.genfromtxt("Swi_Franc.d")
x=data[:,0]
y=data[:,1]
plt.subplot(248)
plt.plot(x,y)
plt.title("Swi")
plt.tick_params(labelbottom='off')
plt.grid()
plt.show()
