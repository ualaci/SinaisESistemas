# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 14:21:49 2021

@author: Uálaci dos Anjos
"""

import numpy as np
from numpy import pi
import matplotlib.pyplot as plt

#Suponha que um sistema H do tipo LTI com resposta impulso h[n] é aplicado um sinal x[n].
def plotaSinal(f,t,titulo):
    fig, ax1 = plt.subplots()
    ax1.stem(t, f, linefmt='r-',use_line_collection=True)
    #ax1.plot(t, f, 'c-', linewidth=2)
    ax1.axhline(y=0, color='k')
    ax1.axvline(x=0, color='k')
    ax1.set_xlabel("amostra")
    ax1.set_ylabel("Amplitude")
    ax1.grid(True)
    ax1.set_title(titulo)
    fig.tight_layout()
    plt.show()
    
def main():
    upperLimit = 100
    lowerLimit=-10
    n = np.arange(lowerLimit, upperLimit,1)
    h=(0.96**n)*np.sin((pi/16)*n)
    h[np.logical_and(n >= -10, n <= 0)]=0
    h[np.logical_and(n >= 11, n <= 100)]=0
    x=np.zeros(abs(lowerLimit)+upperLimit)
    x[np.logical_and(n >= 2, n <= 100)]=1
    y = np.convolve(h,x)
    y2 = []
    lenY=len(y)
    
    for i in range(abs(lowerLimit)-1,int((lenY/2)+abs(lowerLimit))):
        y2.append(y[i])
        
    ###################################################
    #descomente essas linhas caso queira ver as funções h e x geradas
    #plotaSinal(h, n, "h(n)")
    #plotaSinal(x, n, "x(n)")
    plotaSinal(y2, n, "y(n)")
    
main()