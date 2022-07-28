# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 19:52:00 2021

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
    h=np.zeros(abs(lowerLimit)+upperLimit)
    x=np.zeros(abs(lowerLimit)+upperLimit)
    h[np.logical_and(n >= 0, n <= 9)]=1
    x[np.logical_and(n >= 2, n <= 6)]=1
    y = np.convolve(h,x)
    y2 = []
    lenY=len(y)
    
    for i in range(abs(lowerLimit)-1,int((lenY/2)+abs(lowerLimit))):
        y2.append(y[i])
    
    print(len(y2))
    ###################################################
    #descomente essas linhas caso queira ver as funções h e x geradas
    #plotaSinal(h, n, "h(n)")
    #plotaSinal(x, n, "x(n)")
    plotaSinal(y2, n, "y(n)")
    
main()