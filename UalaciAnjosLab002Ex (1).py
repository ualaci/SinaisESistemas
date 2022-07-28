# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 18:15:09 2021

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
    nRange = 10
    n = np.arange(-nRange, nRange,1)
    h=np.zeros(nRange*2)
    x=np.zeros(nRange*2)
    h[np.logical_and(n >= 0, n <= 2)]=1
    x[n==0]=0.5
    x[n==1]=2
    y = np.convolve(h,x)
    y2 = []
    lenY=len(y)
    
    for i in range(int((lenY/2)-nRange),int((lenY/2)+nRange)):
        y2.append(y[i])
    
    plotaSinal(y2, n, "y(n)")
    ###################################################
    #descomente essas linhas caso queira ver as funções h e x geradas
    #plotaSinal(h, n, "h(n)")
    #plotaSinal(x, n, "x(n)")
main()